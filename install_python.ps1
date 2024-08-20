# Set the version and download URL for Python
$version = "3.12.5"
$url = "https://www.python.org/ftp/python/$version/python-$version-amd64.exe"
$logFile = "$env:TEMP\python_install_log.txt"

# Define a function to log messages to the log file and display to the user
function Log-Message {
    param (
        [string]$message
    )
    Add-Content -Path $logFile -Value $message
    Write-Host $message
}

# Notify user and download Python installer
Log-Message "Downloading Python $version from $url..."
Invoke-WebRequest $url -OutFile python-$version.exe
Log-Message "Download completed."

# Notify user and install Python
$installPath = "$($env:ProgramFiles)\Python$version"
Log-Message "Installing Python $version..."
Start-Process python-$version.exe -ArgumentList "/quiet", "InstallAllUsers=1", "PrependPath=1" -Wait
Log-Message "Python installation completed."

# Clean up
Log-Message "Cleaning up..."
Remove-Item python-$version.exe
Log-Message "Cleanup completed."

# Restart the setup batch file and notify user
Log-Message "Restarting setup.bat..."
Start-Process cmd -ArgumentList "/c setup.bat restart" -Wait
Log-Message "Restart of setup.bat completed."

# Exit the script
Log-Message "Exiting PowerShell script."
Exit