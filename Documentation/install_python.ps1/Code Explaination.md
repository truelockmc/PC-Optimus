### ***Here is a detailed Explaination for the Code in install_python.ps1***
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
This PowerShell script automates the process of downloading and installing Python, as well as handling some cleanup and restarting a setup batch file. Here's a breakdown of what each part of the script does:

### **PowerShell Script Breakdown**

#### **1. Define Variables**
```powershell
$version = "3.12.5"
$url = "https://www.python.org/ftp/python/$version/python-$version-amd64.exe"
$logFile = "$env:TEMP\python_install_log.txt"
```
- `$version`: Specifies the Python version to be installed.
- `$url`: Constructs the download URL for the Python installer based on the specified version.
- `$logFile`: Specifies the path to the log file where installation messages will be recorded.

#### **2. Define Logging Function**
```powershell
function Log-Message {
    param (
        [string]$message
    )
    Add-Content -Path $logFile -Value $message
    Write-Host $message
}
```
- `Log-Message`: A custom function that logs messages to both the log file and the console. It takes a string `$message` as input, writes it to the log file, and also displays it in the console.

#### **3. Download Python Installer**
```powershell
Log-Message "Downloading Python $version from $url..."
Invoke-WebRequest $url -OutFile python-$version.exe
Log-Message "Download completed."
```
- `Log-Message "Downloading Python $version from $url..."`: Logs the start of the download process.
- `Invoke-WebRequest $url -OutFile python-$version.exe`: Downloads the Python installer from the specified URL and saves it as `python-$version.exe`.
- `Log-Message "Download completed."`: Logs the completion of the download.

#### **4. Install Python**
```powershell
$installPath = "$($env:ProgramFiles)\Python$version"
Log-Message "Installing Python $version..."
Start-Process python-$version.exe -ArgumentList "/quiet", "InstallAllUsers=1", "PrependPath=1" -Wait
Log-Message "Python installation completed."
```
- `$installPath`: Constructs the installation path for Python.
- `Log-Message "Installing Python $version..."`: Logs the start of the installation process.
- `Start-Process python-$version.exe -ArgumentList "/quiet", "InstallAllUsers=1", "PrependPath=1" -Wait`: Executes the Python installer with silent installation options:
  - `/quiet`: Runs the installer without user interaction.
  - `InstallAllUsers=1`: Installs Python for all users.
  - `PrependPath=1`: Adds Python to the system PATH.
- `Log-Message "Python installation completed."`: Logs the completion of the installation.

#### **5. Clean Up**
```powershell
Log-Message "Cleaning up..."
Remove-Item python-$version.exe
Log-Message "Cleanup completed."
```
- `Log-Message "Cleaning up..."`: Logs the start of the cleanup process.
- `Remove-Item python-$version.exe`: Deletes the installer file.
- `Log-Message "Cleanup completed."`: Logs the completion of the cleanup.

#### **6. Restart Setup Batch File**
```powershell
Log-Message "Restarting setup.bat..."
Start-Process cmd -ArgumentList "/c setup.bat restart" -Wait
Log-Message "Restart of setup.bat completed."
```
- `Log-Message "Restarting setup.bat..."`: Logs the start of the batch file restart.
- `Start-Process cmd -ArgumentList "/c setup.bat restart" -Wait`: Executes the batch file `setup.bat` with the `restart` argument to restart the setup process. `-Wait` ensures the script waits for the batch file to complete.
- `Log-Message "Restart of setup.bat completed."`: Logs the completion of the restart process.

#### **7. Exit Script**
```powershell
Log-Message "Exiting PowerShell script."
Exit
```
- `Log-Message "Exiting PowerShell script."`: Logs the exit of the PowerShell script.
- `Exit`: Exits the PowerShell script.

### **Summary**

1. **Download Python Installer**: The script downloads the specified version of Python from the official Python website.
2. **Install Python**: It runs the installer silently, ensuring Python is available for all users and is added to the system PATH.
3. **Cleanup**: The installer file is deleted after installation.
4. **Restart Batch File**: The script restarts the setup batch file to continue with any further setup steps.
5. **Exit**: The script logs its exit and terminates.

Make sure `setup.bat` is set up to handle the `restart` argument correctly and that the PowerShell script and batch file are in the same directory for proper execution.
