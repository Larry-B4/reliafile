set "params=%*"
cd /d "%~dp0" && ( if exist "%temp%\getadmin.vbs" del "%temp%\getadmin.vbs" ) && fsutil dirty query %systemdrive% 1>nul 2>nul || (  echo Set UAC = CreateObject^("Shell.Application"^) : UAC.ShellExecute "cmd.exe", "/k cd ""%~sdp0"" && %~s0 %params%", "", "runas", 1 >> "%temp%\getadmin.vbs" && "%temp%\getadmin.vbs" && exit /B )
"C:\Users\Nate Widmer\AppData\Local\Microsoft\WindowsApps\python.exe" "C:\Users\Nate Widmer\Documents\TBZ\Informatikmodule\Modul 122\reliafile\watchdogObserver.py"
pause