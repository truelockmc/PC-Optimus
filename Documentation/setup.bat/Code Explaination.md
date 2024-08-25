###***Here is a detailed Explaination for the Code in setup.bat***
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Here’s a detailed breakdown of what each part of the script does:

### **Batch Script Breakdown**

#### **1. Initial Message and Pause**
```batch
@echo off
echo ================================================================================
echo Welcome to PC Optimus, the ultimate open-source multitool for Windows.
echo This script will help you install Python if it is not already installed.
echo ================================================================================
echo.
pause
```
- `@echo off`: Hides the commands being executed, making the output cleaner.
- `echo`: Displays messages to the user.
- `pause`: Waits for the user to press a key before proceeding.

#### **2. Check for Python Installation**
```batch
:: Check if the 'py' command is available
where py >nul 2>&1
if %errorlevel% neq 0 goto :install_python
```
- `where py >nul 2>&1`: Checks if the `py` command (Python executable) is available on the system.
- `if %errorlevel% neq 0 goto :install_python`: If the command is not found (i.e., Python is not installed), it jumps to the `:install_python` label.

#### **3. Python is Installed: Upgrade Pip and Install Modules**
```batch
echo Python is installed. Proceeding with pip and module installation...
py -m ensurepip --upgrade
py -m pip install --upgrade pip
py -m pip install speedtest-cli chardet psutil requests
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
```
- `py -m ensurepip --upgrade`: Ensures that `pip` (Python's package installer) is installed and upgraded.
- `py -m pip install --upgrade pip`: Upgrades `pip` to the latest version.
- `py -m pip install speedtest-cli chardet psutil requests`: Installs necessary Python modules.
- `if %errorlevel% neq 0`: Checks if there was an error during module installation and exits if so.
- `pause`: Waits for the user to press a key before proceeding.
- `cls`: Clears the screen.
- `echo Installation of necessary components completed successfully.`: Notifies the user that the installation is complete.
- `pause`: Waits for the user to press a key before closing the script.
- `exit /b`: Exits the batch script with the current error level.

#### **4. Install Python (If Not Installed)**
```batch
:install_python
echo Python is not installed. Starting PowerShell script to install Python...
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0install_python.ps1"
if %errorlevel% neq 0 (
    echo Failed to execute the PowerShell script to install Python.
    exit /b %errorlevel%
)
echo Python installation script executed successfully.
pause
exit /b
```
- `:install_python`: Label to handle the Python installation.
- `echo Python is not installed. Starting PowerShell script to install Python...`: Informs the user that Python is not installed.
- `powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0install_python.ps1"`: Runs a PowerShell script located in the same directory as the batch file to install Python. `-NoProfile` avoids loading the PowerShell profile, and `-ExecutionPolicy Bypass` allows the script to run regardless of execution policy settings.
- `if %errorlevel% neq 0`: Checks if there was an error running the PowerShell script and exits if so.
- `echo Python installation script executed successfully.`: Notifies the user that the installation script was executed.
- `pause`: Waits for the user to press a key before closing the script.
- `exit /b`: Exits the batch script with the current error level.

### **How It All Works Together:**

1. **Initial Check**: The script first checks if Python is installed by looking for the `py` command.
2. **If Python is Installed**: It upgrades `pip` and installs the necessary Python modules. If this fails, an error message is shown.
3. **If Python is Not Installed**: It invokes a PowerShell script to install Python. If the installation script fails, an error message is shown.

Ensure that your `install_python.ps1` script is properly configured to handle the Python installation and is located in the same directory as the batch file. This script helps in setting up the necessary environment for running Python-based tools or applications.
