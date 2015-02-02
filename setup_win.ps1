# download files
$storageDir = $cwd
$webclient = New-Object System.Net.WebClient
$url = "http://cci.lbl.gov/cctbx_build/results/2013_07_05_0005/cctbx_win_7_vc90_x64_py273_inc.exe"
$file = "$storageDir\cctbx_setup.exe"
$webclient.DownloadFile($url,$file)
$cwd\cctbx_setup.exe
$url = "https://bootstrap.pypa.io/get-pip.py"
$file = "$storageDir\get-pip.py"
$webclient.DownloadFile($url,$file)
$cwd\cctbx_build\bin\cctbx.python get-pip.py
#$url = "http://cci.lbl.gov/cctbx_build/results/2013_07_05_0005/cctbx_win_7_vc90_x64_py273_inc.exe"
#$file = "$storageDir\cctbx_setup.exe"
#$webclient.DownloadFile($url,$file)
