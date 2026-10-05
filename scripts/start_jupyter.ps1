# 备用启动器：配置只写入本课程的 .runtime 目录。
$ErrorActionPreference = 'Stop'
$courseRoot = Split-Path -Parent $PSScriptRoot
$coursePython = 'D:\Anaconda3\envs\HEUhuqiao\python.exe'
if (-not (Test-Path -LiteralPath $coursePython)) {
    throw "Cannot find course Python: $coursePython"
}
$runtimeRoot = Join-Path $courseRoot '.runtime'
$kernelPrefix = Join-Path $runtimeRoot 'jupyter'
$env:JUPYTER_CONFIG_DIR = Join-Path $runtimeRoot 'config'
$env:JUPYTER_DATA_DIR = Join-Path $runtimeRoot 'data'
$env:JUPYTER_RUNTIME_DIR = Join-Path $runtimeRoot 'sessions'
$env:IPYTHONDIR = Join-Path $runtimeRoot 'ipython'
$kernelSearch = Join-Path $kernelPrefix 'share\jupyter'
foreach ($courseDir in @($env:JUPYTER_CONFIG_DIR, $env:JUPYTER_DATA_DIR, $env:JUPYTER_RUNTIME_DIR, $env:IPYTHONDIR, $kernelSearch)) {
    New-Item -ItemType Directory -Path $courseDir -Force | Out-Null
}
if ($env:JUPYTER_PATH) {
    $env:JUPYTER_PATH = $kernelSearch + [IO.Path]::PathSeparator + $env:JUPYTER_PATH
} else {
    $env:JUPYTER_PATH = $kernelSearch
}
& $coursePython -m ipykernel install --prefix $kernelPrefix --name heu-vae --display-name 'Python (HEUhuqiao - VAE)'
if ($LASTEXITCODE -ne 0) { throw 'Kernel configuration failed.' }
& $coursePython -m jupyter notebook --no-browser --ServerApp.ip=127.0.0.1 --ServerApp.root_dir=$courseRoot
if ($LASTEXITCODE -ne 0) { throw 'Jupyter exited with an error.' }
