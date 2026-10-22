from pathlib import Path
import hashlib, json, os, shutil, subprocess, sys, tempfile, atexit

ROOT=Path(__file__).resolve().parent.parent
B=Path(tempfile.mkdtemp(prefix='moss-startup-'))
atexit.register(shutil.rmtree,B,ignore_errors=True)
SOURCE=ROOT/'launchers/windows'
for rel in ('START_HERE - Windows.cmd','app/tools/bootstrap.ps1','AnimaDex-Comparison/app/tools/bootstrap.ps1'):
    p=B/'patched'/rel
    p.parent.mkdir(parents=True,exist_ok=True)
    shutil.copy2(SOURCE/rel,p)
shutil.copytree(B/'patched',B/'release-0.1.1')
p=B/'release-0.1.1/START_HERE - Windows.cmd'
p.write_text(p.read_text().replace('Character ^& Style','Character & Style'),encoding='utf-8')
PY=Path(sys.executable)
PS=Path(os.environ['SystemRoot'])/'System32/WindowsPowerShell/v1.0/powershell.exe'
CMD=Path(os.environ['SystemRoot'])/'System32/cmd.exe'
results=[]

def run(name, command, env, expect=None, marker=None):
    r=subprocess.run(command,env=env,capture_output=True,timeout=60)
    stdout=r.stdout.decode('utf-8',errors='replace')
    stderr=r.stderr.decode('utf-8',errors='replace')
    (B/(name+'.stdout.log')).write_text(stdout,encoding='utf-8')
    (B/(name+'.stderr.log')).write_text(stderr,encoding='utf-8')
    check={'name':name,'exit':r.returncode,'stdout':stdout,'stderr':stderr}
    results.append(check)
    if expect is not None: assert r.returncode==expect,check
    if marker: assert marker in stdout+stderr,check
    print(name, 'exit',r.returncode,flush=True)
    return check

env=os.environ.copy()
for k in ('MOSS_IMAGE_CATALOG_PYTHON','PY_PYTHON','PY_PYTHON3','VIRTUAL_ENV','PYTHONHOME','PYTHONPATH'):
    env.pop(k,None)
env.update(CI='1',MOSS_IMAGE_CATALOG_NO_PAUSE='1',PYTHONDONTWRITEBYTECODE='1',PYTHONIOENCODING='utf-8')
env['PATH']=str(PY.parent)+';'+str(Path(os.environ['SystemRoot']))+';'+str(Path(os.environ['SystemRoot'])/'System32')
stub='import json,sys; print(json.dumps({"python":sys.version.split()[0],"executable":sys.executable,"args":sys.argv[1:]}, ensure_ascii=True)); sys.exit(0)\n'
for v in ('old','new'):
    root=B/('fixture '+v+' & 日本語')
    (root/'app/tools').mkdir(parents=True,exist_ok=True)
    prefix=B/('release-0.1.1' if v=='old' else 'patched')
    shutil.copy2(prefix/'START_HERE - Windows.cmd',root/'START_HERE - Windows.cmd')
    shutil.copy2(prefix/'app/tools/bootstrap.ps1',root/'app/tools/bootstrap.ps1')
    (root/'app/tools/bootstrap.cmd').write_bytes(b'@echo off\r\nexit /b 0\r\n')
    (root/'app/tools/startup.py').write_text(stub,encoding='utf-8')
    # Stop before Python while isolating CMD title parsing.
    title=run('title-'+v,f'"{CMD}" /d /s /c ""{root / "START_HERE - Windows.cmd"}""',env,0)
    assert bool(title['stderr'].strip()) == (v=='old'),title
    # Actual Windows PowerShell 5.1 and PATH Python; installed launcher availability depends on the host.
    direct=run('path-real-py-'+v,[str(PS),'-NoProfile','-ExecutionPolicy','Bypass','-File',str(root/'app/tools/bootstrap.ps1'),'--probe','two words'],env,0 if v=='new' else None)
    assert direct['exit']==0,direct
    assert json.loads(direct['stdout'])['args']==['--probe','two words']

cs=B/'LauncherShim.cs'
cs.write_text(r'''using System;
using System.IO;
class LauncherShim {
 static int Main(string[] args) {
  Console.OutputEncoding=new System.Text.UTF8Encoding(false);
  var exe=System.Reflection.Assembly.GetExecutingAssembly().Location;
  if (Path.GetFileName(exe)=="old-python.exe") return 11;
  var selector=args.Length>0?args[0]:"";
  var mode=Environment.GetEnvironmentVariable("MOSS_TEST_MODE")??"success";
  var log=Environment.GetEnvironmentVariable("MOSS_TEST_LAUNCHER_LOG");
  if(log!=null) File.AppendAllText(log,selector+"\n");
  if (Environment.GetEnvironmentVariable("PYTHON_MANAGER_AUTOMATIC_INSTALL")!="false" || Environment.GetEnvironmentVariable("PYLAUNCHER_ALLOW_INSTALL")!=null || Environment.GetEnvironmentVariable("PYLAUNCHER_ALWAYS_INSTALL")!=null) {
   Console.Error.WriteLine("unsafe installer environment"); return 66;
  }
  if(mode=="missing" || selector=="-0p") { Console.Error.WriteLine("No installed Pythons found!"); return 103; }
  if(mode=="invalid" && selector=="-3") { Console.WriteLine(@"C:\does-not-exist\python.exe"); return 0; }
  if(mode=="old" || mode=="old-default" && selector=="-3") {
    Console.WriteLine(Path.Combine(Path.GetDirectoryName(exe),"old-python.exe")); return 0;
  }
  if(selector!="-3" && selector!="-3.13") { Console.Error.WriteLine("Requested version not installed"); return 103; }
  Console.WriteLine(Environment.GetEnvironmentVariable("MOSS_TEST_PYTHON")); return 0;
 }
}
''',encoding='utf-8')
shim=B/'shim only'
shim.mkdir(exist_ok=True)
subprocess.run([str(Path(os.environ['SystemRoot'])/'Microsoft.NET/Framework64/v4.0.30319/csc.exe'),'/nologo','/target:exe',f'/out:{shim/"py.exe"}',str(cs)],check=True,capture_output=True)
shutil.copy2(shim/'py.exe',shim/'old-python.exe')
newroot=B/'fixture new & 日本語'
command=[str(PS),'-NoProfile','-ExecutionPolicy','Bypass','-File',str(newroot/'app/tools/bootstrap.ps1'),'--probe','two words']
e=env.copy()
e['PATH']=str(shim)+';'+str(Path(os.environ['SystemRoot'])/'System32')
e['MOSS_TEST_PYTHON']=str(PY)
e['PYLAUNCHER_ALLOW_INSTALL']='1' # Must be removed only in discovery child.
e['PYLAUNCHER_ALWAYS_INSTALL']='1'
for mode,expect,marker in [('success',0,None),('invalid',0,None),('old-default',0,None),('old',11,'[PYTHON_OLD]'),('missing',10,'[PYTHON_MISSING]')]:
    e['MOSS_TEST_MODE']=mode
    log=B/('shim-'+mode+'.calls.log')
    log.unlink(missing_ok=True)
    e['MOSS_TEST_LAUNCHER_LOG']=str(log)
    check=run('py-only-'+mode,command,e,expect,marker)
    assert '-0p' not in log.read_text(),check
    if expect==0:
        assert json.loads(check['stdout'])['executable'].casefold()==str(PY).casefold(),check

e=env.copy()
e['PATH']=str(Path(os.environ['SystemRoot'])/'System32')
run('no-python-no-launcher',command,e,10,'[PYTHON_MISSING]')
e['MOSS_IMAGE_CATALOG_PYTHON']=str(B/'nonexistent-python.exe')
run('explicit-invalid',command,e,12,'[PYTHON_PATH]')
e['MOSS_IMAGE_CATALOG_PYTHON']=str(shim/'old-python.exe')
run('explicit-too-old-emulated',command,e,11,'[PYTHON_OLD]')
e['MOSS_IMAGE_CATALOG_PYTHON']=str(PY)
run('explicit-python313',command,e,0,sys.version.split()[0])

# Exercise a real interpreter executable reached through a Unicode/space/ampersand path.
alias=B/'Python & 日本語'
alias.mkdir(exist_ok=True)
subprocess.run([str(PY),'-m','venv','--without-pip',str(alias)],check=True,capture_output=True)
e=env.copy()
e['PATH']=str(shim)
e['MOSS_TEST_PYTHON']=str(alias/'Scripts/python.exe')
e['MOSS_TEST_MODE']='success'
run('py-query-unicode-python',command,e,0,sys.version.split()[0])

# Full CMD -> bootstrap.cmd -> Windows PowerShell -> Python handoff, without a server.
(newroot/'app/tools/bootstrap.cmd').write_bytes(b'@echo off\r\nsetlocal\r\n"%SystemRoot%\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -NoProfile -ExecutionPolicy Bypass -File "%~dp0bootstrap.ps1" %*\r\nexit /b %errorlevel%\r\n')
check=run('full-windows-cmd',f'"{CMD}" /d /s /c ""{newroot / "START_HERE - Windows.cmd"}" --probe "two words""',env,0,sys.version.split()[0])
assert not check['stderr'].strip(),check
assert json.loads(check['stdout'])['args']==['--probe','two words'],check
(newroot/'app/tools/startup.py').write_text('raise SystemExit(7)\n',encoding='utf-8')
run('entry-exit-code-propagation',command,env,7)

report={'python':sys.version,'powershell':'Windows PowerShell 5.1','checks':results,'count':len(results),
        'scope':'Windows startup handoff; py-only/old/missing cases use labelled C# launcher/interpreter fixtures. No installed interpreters or registry were changed. No live catalog or ComfyUI server was stopped.'}
(B/'test-results.json').write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding='utf-8')
print('PASS',len(results),flush=True)
