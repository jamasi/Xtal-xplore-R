# check for PS3+
if ($PSVersionTable.PSVersion.major -lt 3) {
	'This script needs at least PowerShell Version 3'
	exit
}

'Downloading cctbx, pip and other needed files...'
# download files
$mycwd = $PSScriptRoot
Write-Host $mycwd
cd $mycwd
New-Item -ItemType Directory -Force -Path $mycwd\dl

$url = "http://cci.lbl.gov/cctbx_build/results/2013_07_05_0005/cctbx_win_7_vc90_x64_py273_inc.exe"
$file = "\cctbx_setup.exe"
if (Test-Path $mycwd$file) {
	Write-Host "using existing file: ${file}"
} else {
	Invoke-WebRequest -OutFile $mycwd$file $url
}
& $mycwd$file | Out-Host
$url = "https://bootstrap.pypa.io/get-pip.py"
$file = "\dl\get-pip.py"
if (Test-Path $mycwd$file) {
	Write-Host "using existing file: ${file}"
} else {
	
	Invoke-WebRequest -OutFile $mycwd$file $url
}
& $mycwd\cctbx_build\bin\cctbx.python.bat $mycwd$file | Out-Host


# Not sure if needed:
# http://download.microsoft.com/download/7/9/6/796EF2E4-801B-4FC4-AB28-B59FBF6D907B/VCForPython27.msi

# Download pre-compiled Python libs from my mirror
# The original unofficial files are available from:
# http://www.lfd.uci.edu/~gohlke/pythonlibs/ 
# Many thanks to Christoph Gohlke for building those.
$url = "http://mirror.jamasi.nl/whl/numpy-1.9.1+mkl-cp27-none-win_amd64.whl"
$file = "\dl\numpy-1.9.1+mkl-cp27-none-win_amd64.whl"
if (Test-Path $mycwd$file) {
	Write-Host "using existing file: ${file}"
} else {
	Invoke-WebRequest -OutFile $mycwd$file $url
}
& $mycwd\cctbx_build\base\python\Scripts\pip.exe install $mycwd$file | Out-Host

$url = "http://mirror.jamasi.nl/whl/PyQt4-4.11.3-cp27-none-win_amd64.whl"
$file = "\dl\PyQt4-4.11.3-cp27-none-win_amd64.whl"
if (Test-Path $mycwd$file) {
	Write-Host "using existing file: ${file}"
} else {
	Invoke-WebRequest -OutFile $mycwd$file $url
}
& $mycwd\cctbx_build\base\python\Scripts\pip.exe install $mycwd$file | Out-Host

$url = "http://mirror.jamasi.nl/whl/VTK-5.10.1+qt486-cp27-none-win_amd64.whl"
$file = "\dl\VTK-5.10.1+qt486-cp27-none-win_amd64.whl"
if (Test-Path $mycwd$file) {
	Write-Host "using existing file: ${file}"
} else {
	Invoke-WebRequest -OutFile $mycwd$file $url
}
& $mycwd\cctbx_build\base\python\Scripts\pip.exe install $mycwd$file | Out-Host

$url = "http://mirror.jamasi.nl/whl/mayavi-4.3.1+vtk510-cp27-none-win_amd64.whl"
$file = "\dl\mayavi-4.3.1+vtk510-cp27-none-win_amd64.whl"
if (Test-Path $mycwd$file) {
	Write-Host "using existing file: ${file}"
} else {
	Invoke-WebRequest -OutFile $mycwd$file $url
}
& $mycwd\cctbx_build\base\python\Scripts\pip.exe install $mycwd$file | Out-Host

# If running in the console, wait for input before closing.
if ($Host.Name -eq "ConsoleHost")
{ 
	Write-Host "Press any key to continue..."
	$Host.UI.RawUI.FlushInputBuffer()	# Make sure buffered input doesn't "press a key" and skip the ReadKey().
	$Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyUp") > $null
}
