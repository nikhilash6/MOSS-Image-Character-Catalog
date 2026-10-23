"""One-time, verified v0.1.2 package refresh. Never changes image data.

--base ZIP --output DIR builds locally. --publish is for the guarded workflow.
Only --publish uses GitHub credentials, supplied by the Actions job environment.
"""
from pathlib import Path
import argparse
import hashlib
import json
import os
import shutil
import subprocess
import zipfile

REPO = 'ukr8b3g-cmyk/MOSS-Image-Character-Catalog'
RELEASE_ID = 421022122
OLD_ID = 666604514
OLD_SUM_ID = 666608678
BASE_SHA = 'f289da6a56b3ce8f7e6864b0338ec04d56066e8e415ba9059ee51310ad81644c'
OLD_SUM_SHA = '04bf73dcf4c7073d21bed58ebeed3a823692fbcb46ea32b76f79fe1c45d12a36'
NAME = 'MOSS-Image-Character-Catalog-v0.1.2.zip'
TEMP_NAME = 'MOSS-Image-Character-Catalog-v0.1.2-title-link.zip'
PREFIX = 'MOSS-Image-Character-Catalog/'
ROOT = Path(__file__).resolve().parent.parent
TITLE = '<span data-i18n="title">MOSS-Image Character & Style Catalog</span>'
LINK = '<a class="catalog-home" href="https://github.com/' + REPO + '" target="_blank" rel="noopener noreferrer">' + TITLE + '</a>'
CSS = '\nheader h1 .catalog-home{color:inherit;text-decoration:none}\nheader h1 .catalog-home:hover{text-decoration:underline;text-underline-offset:.14em}\nheader h1 .catalog-home:focus-visible{outline:2px solid var(--accent);outline-offset:4px;border-radius:2px}\n'
UI_HASHES = {'app/review/index.html':'6e154e05fe26cb85b18dd2d097e806af0018f38a17e770e9b0a8e40ef9d602ce', 'app/review/review.css':'e98b4c0c5cc24b3a64360ca24272f45b58443607b8b59133b0f10c333db400f2'}
DOCS = ['README.md','README.ja.md','docs/releases/v0.1.2.md','docs/updates/catalog-title-link.md']

def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda:f.read(8*1024*1024),b''): h.update(chunk)
    return h.hexdigest()

def gh(*args):
    result = subprocess.run(['gh',*args],check=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    return json.loads(result.stdout) if result.stdout.strip() else None

def api(path, body=None, work=None):
    args=['api','repos/'+REPO+'/'+path]
    if body is not None:
        p=work/'api-request.json'
        p.write_text(json.dumps(body,ensure_ascii=False),encoding='utf-8')
        args += ['--method','PATCH','--input',str(p)]
    return gh(*args)

def build(base, work, sevenzip):
    if digest(base) != BASE_SHA: raise RuntimeError('Unexpected source ZIP; no update is safe')
    stage = work/'stage'
    replacements={}
    with zipfile.ZipFile(base) as z:
        for rel in UI_HASHES:
            text=z.read(PREFIX+rel).decode('utf-8').replace('\r\n','\n')
            if rel.endswith('.html'):
                assert text.count(TITLE)==1 and 'class="catalog-home"' not in text
                text=text.replace(TITLE,LINK,1)
            else:
                assert '.catalog-home' not in text
                text += CSS
            blob=text.replace('\n','\r\n').encode('utf-8')
            assert hashlib.sha256(blob).hexdigest()==UI_HASHES[rel],rel
            replacements[rel]=blob
    for rel in DOCS:
        replacements[rel]=(ROOT/rel).read_bytes()
    for rel,blob in replacements.items():
        p=stage/PREFIX/rel;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(blob)
    files=work/'update-files.txt'
    files.write_text('\n'.join(PREFIX+r for r in replacements)+'\n',encoding='utf-8')
    target=work/TEMP_NAME
    if target.exists(): raise RuntimeError('Output ZIP already exists')
    shutil.copy2(base,target)
    subprocess.run([sevenzip,'u','-tzip','-mm=Deflate','-mx=5','-scsUTF-8',str(target),'@'+str(files)],cwd=stage,check=True)
    subprocess.run([sevenzip,'t',str(target)],check=True)
    with zipfile.ZipFile(base) as old, zipfile.ZipFile(target) as new:
        a={i.filename:i for i in old.infolist()};b={i.filename:i for i in new.infolist()}
        expected=set(a)|{PREFIX+r for r in replacements}
        assert set(b)==expected and len(new.namelist())==len(b)==136694
        changed=[]
        for name in b:
            rel=name.removeprefix(PREFIX)
            if rel in replacements:
                assert new.read(name)==replacements[rel]
                changed.append(rel)
            else:
                assert (a[name].CRC,a[name].file_size,a[name].compress_size)==(b[name].CRC,b[name].file_size,b[name].compress_size),name
        rows=json.loads(new.read(PREFIX+'app/outputs/user_catalog.json'))['items']
        assert len(rows)==34158
        images={PREFIX+'app/outputs/'+r['files']['image']:r['image_sha256'] for r in rows}
        assert len(images)==34158
        for name,h in images.items(): assert hashlib.sha256(new.read(name)).hexdigest()==h,name
        assert set(changed)==set(replacements)
    checksum=digest(target)
    sums=work/'SHA256SUMS-title-link.txt'
    sums.write_text(checksum+'  '+NAME+'\n',encoding='ascii')
    result={'sha256':checksum,'size':target.stat().st_size,'entries':len(b),'images_verified':34158,'changed_files':list(replacements),'content_sha256':{k:hashlib.sha256(v).hexdigest() for k,v in replacements.items()},'source_sha256':BASE_SHA}
    (work/'verification.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    return target,sums,result

def publish(work, target, sums, result):
    release=api('releases/'+str(RELEASE_ID))
    assert release['tag_name']=='v0.1.2' and not release['draft'] and not release.get('immutable')
    old=api('releases/assets/'+str(OLD_ID));oldsum=api('releases/assets/'+str(OLD_SUM_ID))
    assert old['digest']=='sha256:'+BASE_SHA and old['name']==NAME
    assert oldsum['digest']=='sha256:'+OLD_SUM_SHA and oldsum['name']=='SHA256SUMS.txt'
    assert not any(a['name'] in {TEMP_NAME,sums.name,NAME.replace('.zip','-before-title-link.zip'),'SHA256SUMS-before-title-link.txt'} for a in release['assets'])
    subprocess.run(['gh','release','upload','v0.1.2',str(target),str(sums),'--repo',REPO],check=True)
    release=api('releases/'+str(RELEASE_ID))
    assets={a['name']:a for a in release['assets']}
    new=assets[TEMP_NAME];newsum=assets[sums.name]
    assert new['digest']=='sha256:'+result['sha256'] and new['size']==result['size']
    assert newsum['digest']=='sha256:'+digest(sums)
    # Upload and verify first; retain the earlier assets under explicit names.
    api('releases/assets/'+str(OLD_ID),{'name':NAME.replace('.zip','-before-title-link.zip')},work)
    api('releases/assets/'+str(OLD_SUM_ID),{'name':'SHA256SUMS-before-title-link.txt'},work)
    api('releases/assets/'+str(new['id']),{'name':NAME},work)
    api('releases/assets/'+str(newsum['id']),{'name':'SHA256SUMS.txt'},work)
    url='https://github.com/'+REPO+'/releases/download/v0.1.2/'
    body=f'**[全件版ZIPをダウンロード / Download the complete ZIP]({url}{NAME})** — {result["size"]:,} bytes（約2.05 GB / 1.91 GiB）\n\n'
    body+=f'[SHA256SUMS.txt]({url}SHA256SUMS.txt) · [日本語README](https://github.com/{REPO}/blob/main/README.ja.md) · [English README](https://github.com/{REPO}/blob/main/README.md)\n\n'
    body+='**2026-10-24 refresh / 配布ZIP更新:** 太字タイトルにGitHubリンクを追加し、日英READMEを更新しました。Images are unchanged: 33,937 characters + 221 styles.\n\n'
    notes=(ROOT/'docs/releases/v0.1.2.md').read_text(encoding='utf-8')
    body+=notes.replace('](../updates/catalog-title-link.md)','](https://github.com/'+REPO+'/blob/main/docs/updates/catalog-title-link.md)')
    body+=f'\n\n## Archive verification / ZIP検証\n\n7-Zip archive test passed for all {result["entries"]:,} entries; all 34,158 image SHA256 values match the catalog. Six UI/documentation files were replaced or added. Earlier assets are retained with `before-title-link` in their names; use the main download above.\n\n```text\n{result["sha256"]}  {NAME}\n```\n'
    api('releases/'+str(RELEASE_ID),{'body':body},work)
    final=api('releases/'+str(RELEASE_ID));assets={a['name']:a for a in final['assets']}
    assert assets[NAME]['id']==new['id'] and assets[NAME]['digest']=='sha256:'+result['sha256']
    assert assets['SHA256SUMS.txt']['id']==newsum['id']
    result['published_assets']={n:{'id':a['id'],'digest':a['digest'],'size':a['size']} for n,a in assets.items()}
    (work/'publication.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(result,indent=2))
    if os.environ.get('GITHUB_STEP_SUMMARY'):
        with open(os.environ['GITHUB_STEP_SUMMARY'],'a',encoding='utf-8') as f: f.write(f'Published refreshed v0.1.2 ZIP: {result["size"]:,} bytes\n\nSHA256: `{result["sha256"]}`\n\nAll 34,158 image hashes verified.\n')

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--base',type=Path)
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--sevenzip',default='7z')
    parser.add_argument('--publish',action='store_true')
    args=parser.parse_args();work=args.output.resolve();work.mkdir(parents=True,exist_ok=True)
    if args.publish:
        assert os.environ.get('GITHUB_ACTIONS')=='true' and os.environ.get('GITHUB_REPOSITORY')==REPO
        assert os.environ.get('GITHUB_REF')=='refs/heads/main'
        base=work/'before-title-link.zip'
        with base.open('xb') as f:
            subprocess.run(['gh','api','repos/'+REPO+'/releases/assets/'+str(OLD_ID),'-H','Accept: application/octet-stream'],stdout=f,check=True,timeout=900)
    else:
        if args.base is None: parser.error('--base is required for a local build')
        base=args.base.resolve()
    target,sums,result=build(base,work,args.sevenzip)
    if args.publish: publish(work,target,sums,result)
    else: print(json.dumps(result,indent=2))

if __name__=='__main__': main()
