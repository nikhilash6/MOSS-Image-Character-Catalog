# Native Windows preflight; no Python catalog code runs until a version passes.
$ErrorActionPreference='Stop'
$catalogArguments=@($args)
function Test-CatalogInterpreter([string]$Path) {
    if (!(Test-Path -LiteralPath $Path -PathType Leaf)) { return 12 }
    if ($Path -match '\\Microsoft\\WindowsApps\\') { return 12 }
    try {
        $probe=New-Object System.Diagnostics.Process
        $probe.StartInfo.FileName=$Path
        $probe.StartInfo.Arguments='-c "import sys; sys.exit(0 if sys.version_info >= (3,10) else 11)"'
        $probe.StartInfo.UseShellExecute=$false
        $probe.StartInfo.CreateNoWindow=$true
        $probe.StartInfo.RedirectStandardOutput=$true
        $probe.StartInfo.RedirectStandardError=$true
        [void]$probe.Start()
        if (!$probe.WaitForExit(20000)) { $probe.Kill(); return 12 }
        $result=$probe.ExitCode
        if ($result -eq 0 -or $result -eq 11) { return $result }
        return 12
    } catch { return 12 } finally { if ($probe) { $probe.Dispose() } }
}
function Get-CatalogLauncherInterpreter([string]$Launcher, [string]$Selector) {
    $query=$null
    try {
        $query=New-Object System.Diagnostics.Process
        $query.StartInfo.FileName=$Launcher
        $query.StartInfo.Arguments=$Selector + ' -c "import sys; print(sys.executable)"'
        $query.StartInfo.UseShellExecute=$false
        $query.StartInfo.CreateNoWindow=$true
        $query.StartInfo.RedirectStandardOutput=$true
        $query.StartInfo.RedirectStandardError=$true
        $query.StartInfo.StandardOutputEncoding=[System.Text.Encoding]::UTF8
        $query.StartInfo.EnvironmentVariables['PYTHONIOENCODING']='utf-8'
        $query.StartInfo.EnvironmentVariables['PYTHON_MANAGER_AUTOMATIC_INSTALL']='false'
        $query.StartInfo.EnvironmentVariables.Remove('PYLAUNCHER_ALLOW_INSTALL')
        $query.StartInfo.EnvironmentVariables.Remove('PYLAUNCHER_ALWAYS_INSTALL')
        [void]$query.Start()
        $output=$query.StandardOutput.ReadToEndAsync()
        $errors=$query.StandardError.ReadToEndAsync()
        if (!$query.WaitForExit(20000)) { $query.Kill(); return }
        if ($query.ExitCode -eq 0) {
            $path=$output.Result.Trim()
            if ($path -and (Test-Path -LiteralPath $path -PathType Leaf)) { return $path }
        }
    } catch {
        # A missing/broken launcher must not prevent PATH-based Python discovery.
        return
    } finally { if ($query) { $query.Dispose() } }
}
function Show-CatalogInstall {
    [Console]::Error.WriteLine('Windows: https://www.python.org/downloads/windows/')
    [Console]::Error.WriteLine('Install Python 3.10+ and enable its PATH option, then open this startup file again.')
}
function Finish-Catalog([int]$Code) {
    if ($Code -ne 0 -and !$env:CI -and !$env:MOSS_IMAGE_CATALOG_NO_PAUSE -and ![Console]::IsInputRedirected -and ![Console]::IsOutputRedirected) {
        [Console]::Error.WriteLine('Press Enter to close this window.')
        [void][Console]::ReadLine()
    }
    exit $Code
}
$selected=$null
if ($env:MOSS_IMAGE_CATALOG_PYTHON) {
    $result=Test-CatalogInterpreter $env:MOSS_IMAGE_CATALOG_PYTHON
    if ($result -eq 11) {
        [Console]::Error.WriteLine('[PYTHON_OLD] The specified Python is older than 3.10.')
        Show-CatalogInstall
        Finish-Catalog 11
    } elseif ($result -ne 0) {
        [Console]::Error.WriteLine('[PYTHON_PATH] MOSS_IMAGE_CATALOG_PYTHON cannot run. Correct or unset its executable path.')
        Finish-Catalog 12
    }
    $selected=$env:MOSS_IMAGE_CATALOG_PYTHON
} else {
    $candidates=New-Object 'System.Collections.Generic.List[string]'
    foreach ($folder in ($env:PATH -split ';')) {
        $catalogFolder=$folder.Trim('"')
        if ($catalogFolder -and [System.IO.Directory]::Exists($catalogFolder)) {
            foreach ($name in @('python.exe','python3.exe','python3.12.exe','python3.11.exe','python3.10.exe')) {
                $candidates.Add([System.IO.Path]::Combine($catalogFolder,$name))
            }
        }
    }
    $seenOld=$false
    foreach ($candidate in ($candidates | Select-Object -Unique)) {
        $result=Test-CatalogInterpreter $candidate
        if ($result -eq 0) { $selected=$candidate; break }
        if ($result -eq 11) { $seenOld=$true }
    }
    if (!$selected) {
        $py=Get-Command py.exe -CommandType Application -ErrorAction SilentlyContinue
        if ($py) {
            # Ask Python itself; do not parse version-list text from py.exe.
            foreach ($selector in @('-3','-3.14','-3.13','-3.12','-3.11','-3.10')) {
                $candidate=Get-CatalogLauncherInterpreter $py.Source $selector
                if (!$candidate) { continue }
                $result=Test-CatalogInterpreter $candidate
                if ($result -eq 0) { $selected=$candidate; break }
                if ($result -eq 11) { $seenOld=$true }
            }
        }
    }
    if (!$selected) {
        if ($seenOld) {
            [Console]::Error.WriteLine('[PYTHON_OLD] Only Python versions older than 3.10 were found.')
            $code=11
        } else {
            [Console]::Error.WriteLine('[PYTHON_MISSING] No runnable Python 3.10+ was found on PATH or in the Python launcher.')
            $code=10
        }
        Show-CatalogInstall
        Finish-Catalog $code
    }
}
$catalogEntry=Join-Path $PSScriptRoot 'startup.py'
if (!(Test-Path -LiteralPath $catalogEntry -PathType Leaf)) { $catalogEntry=Join-Path $PSScriptRoot 'launch_catalog.py' }
& $selected $catalogEntry @catalogArguments
Finish-Catalog $LASTEXITCODE
