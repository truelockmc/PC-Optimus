@echo off
echo ================================================================================
echo Welcome to PC Optimus, the ultimate open-source multitool for Windows.
echo This script will help you install the Requirements if not already installed.
echo ================================================================================
echo.
pause

:: Check if the 'py' command is available
where py >nul 2>&1
if %errorlevel% neq 0 goto :install_python

echo Python is installed. Proceeding with pip and module installation...
py -m ensurepip --upgrade
py -m pip install --upgrade pip
py -m pip install speedtest-cli chardet psutil requests pywin32
if %errorlevel% neq 0 (
    echo Error occurred during module installation.
    exit /b %errorlevel%
)
pause
cls
echo Installation of necessary components completed successfully.
echo Open PCOptimus.py to use the tool.
pause
exit /b

:install_python
@echo off

:install_python
echo Python is not installed!
echo Please download the latest version here: https://www.python.org/downloads/ and close this window.
echo Press enter to open the official Downloadsite
pause
start https://www.python.org/downloads/
exit /b
