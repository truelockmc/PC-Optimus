# PC-Optimus

PC-Optimus is a lightweight, open-source Python tool for Windows that offers various Features to clean up, debloat, update, repair, and gather information about your PC, everything without requiring code knowledge. 

If you need help or encounter errors, please join our [Discord server](https://discord.gg/36bPs8cQ5B), ask for assistance, and send your log files or error codes if available.

[![Stargazers repo roster for @truelockmc/PC-Optimus](https://reporoster.com/stars/dark/truelockmc/PC-Optimus)](https://github.com/truelockmc/PC-Optimus/stargazers)

## Setup

### Using the `.py` File

1. Download `PCOptimus(unzip_me).zip` from the [latest release](https://github.com/truelockmc/PC-Optimus/releases)

2. Unzip/unpack `PCOptimus(unzip_me).zip`

3. Run `setup.bat`. This script will automatically install Python (if not already installed) and the necessary modules.

4. If you prefer not to use `setup.bat`, manually install Python and run `pip3 install -r requirements.txt` in the Direcory you downloaded the Files.

5. Run `PC-Optimus.py`.

5. If you ran it once, you can also access it from the Start Menu by searching PCOptimus

6. For help, join our [Discord server](https://discord.gg/36bPs8cQ5B).

### Using the `.exe` File

*Note: The `.exe` file is temporarily unavailable due to errors and false virus alerts.*

1. Download and run the `.exe` file. If Microsoft Defender shows a warning because the source is unknown, you can click on "More Info" and choose to run it anyway. Alternatively, use the `.py` file to review the code.

2. For help, join our [Discord server](https://discord.gg/36bPs8cQ5B).

## Current Features

### Repair
- Scan and fix system file errors.
- Resolve storage, virtual storage, and RAM errors.
- Fix file system errors.
- Repair network connection errors by cleaning up, resetting, and restarting network settings and adapters.

### Updating
- Update all installed apps.
- Run Windows Update.
- Update drivers.

### Cleanup
- Remove bloatware.
- Block Microsoft tracking.
- Clean up Apps that start on PC Startup to make your Computer boot faster.
- Clean up prefetch data.
- Run the Windows Clean Manager.
- Cleanup temporary files.
- Remove File Duplicates
- Remove invisible storage-consuming files.
- Preconfigured cleanup: Temporary Internet Files, file thumbnails, recycle bin, and unnecessary Windows feedback files.
- Defragment/Optimize hard drive.
- Empty recycle bin.

### Information
- Perform an internet speed test.
- View generic system info.
- Check connection info (network name, etc.).
- Advanced system info.
- Monitor current PC resource usage, including resource allocation by apps (extended task manager).

### Help Button
- Explains the function of each button.

## Changelog

### Beta 1.0
- First publish: [Beta 1.0 Release](https://github.com/truelockmc/PC-Optimus/releases/tag/Beta)

### Beta 1.1
- Added System Info.
- Added Network Info.
- Added Internet Speed Test.
- Added Advanced System Info: [Beta 1.1 Release](https://github.com/truelockmc/PC-Optimus/releases/tag/Beta1.1)

### Beta 1.2
- Fixed errors related to running commands like `cleanmgr` and `wsreset.exe`.
- Detailed error messages: [Beta 1.2 Release](https://github.com/truelockmc/PC-Optimus/releases/tag/Beta1.2)

### Beta 1.3
- Created executable (.exe) to avoid needing Python installation: [Beta 1.3 Release](https://github.com/truelockmc/PC-Optimus/releases/tag/Beta1.3)

### Beta 1.4
- Added Defragment function.
- Added Empty Recycle Bin function.
- Temporarily removed `.exe` due to errors and false virus alerts.
- Solved syntax errors and optimized imports: [Beta 1.4 Release](https://github.com/truelockmc/PC-Optimus/releases/tag/Beta1.4)

### Beta 2.0
- Added Resource Monitoring.
- Added Storage Diagnostics.
- Enhanced Advanced System Info functionality.
- Integrated other Windows Services: [Beta 2.0 Release](https://github.com/truelockmc/PC-Optimus/releases/tag/Beta2.0)

### Beta 3.0
- Added loading screen to the "Clean Invis" function.
- Fixed issues with update functions, empty recycle bin, and simplified system info.
- Added System Health Scan.
- Reduced additional file requirements to just the image `logo.png`: [Beta 3.0 Release](https://github.com/truelockmc/PC-Optimus/releases/tag/Beta3.0)

### Beta 4.0
- Added Virtual Storage Cleanup.
- Added Repair Connection and Repair File System features.
- Improved admin command handling: [Beta 4.0 Release](https://github.com/truelockmc/PC-Optimus/releases/tag/Beta4.0)

### Beta 5.0
- Completely overhauled admin command handling.
- Removed Pillow module.
- Simplified code, improved logging, and enhanced Repair Connection.
- Eliminated unnecessary code and temp files.
- Introduced setup.bat for easier component installation.
- Resolved syntax errors: [Beta 5.0 Release](https://github.com/truelockmc/PC-Optimus/releases/tag/Beta5.0)

### 1.0
- Added Debloat features for Windows 10 and 11.
- Added features to disable Microsoft tracking.
- Replaced the Clean Invis loading bar with progress visuals in CMD.
- Fixed Clean Invis errors and cleaned up code.
- Updated imports in `PCOptimus.py` and `setup.bat`.
- Removed unnecessary imports: [1.0 Release](https://github.com/truelockmc/PC-Optimus/releases/tag/1.0)

### 1.1
- Fixxed Error that if you have much bloatware installed you wont be able to click on Uninstall selected: [1.1 Release](https://github.com/truelockmc/PC-Optimus/releases/tag/1.1)

### 1.2
- added automatic shortcut Creation, so you can just search for PCOptimus in the Start Menu
- you can now also create a Shortcut for PCOptimus on your Desktop with one click
- updated required modules in setup.bat: [1.2 Release](https://github.com/truelockmc/PC-Optimus/releases/tag/1.2)

### 1.3
- Fixxed 404 Error with advanced Debloat Function: [1.3 Release](https://github.com/truelockmc/PC-Optimus/releases/tag/1.3)

### 1.4
- Fixxed Error that you couldn`t uninstall some Bloatware because of missing rights
- Fixxed Error that the Internetprovider is "Unknown" when using the Connection Info Feature: [1.4 Release](https://github.com/truelockmc/PC-Optimus/releases/tag/1.4)

## Contributing

Feel free to contribute to the project by submitting issues or pull requests. For more details, refer to the [contributing guidelines](CONTRIBUTING.md).

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/truelockmc/PC-Optimus/blob/main/LICENSE.txt) file for details.

## Contact

For additional support or to report issues, join our [Discord server](https://discord.gg/36bPs8cQ5B) or contact me at anonyson@proton.me .

