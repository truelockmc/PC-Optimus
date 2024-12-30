# PCOptimus Documentation

Here you will find an Explaination to every Part of the Code that is Python.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## PCOptimus.py - Main File

This Python file is the core of the Application

### Imports
```python
import tkinter as tk
from Features.shortcut import create_shortcut
from Features.clean.tiny_clean_features import clean_recycle_bin, clean_vs, defragment
from Features.command_handling import run_command, run_admin_command, run_window_admin_command
from Features.info.connection import show_connection_info
from Features.clean.rm_bloat import rm_Bloatware
from Features.clean.rm_dupe import rm_dupe
from Features.clean.clean_startup import clean_startup
from Features.info.internet_speedtest import open_speedtest_window
from Features.info.pc_info import show_pc_info
from UI.Buttons import create_buttons
```

- **tkinter**: The primary module used to create the graphical user interface (GUI) for the application.
- **create_shortcut**: A function imported from `Features.shortcut` to manage shortcut creation on the system.
- **clean_recycle_bin, clean_vs, defragment**: Functions from the `tiny_clean_features` module that are used to clean the Recycle Bin, clean Windows visual effects, and defragment the hard drive.
- **run_command, run_admin_command, run_window_admin_command**: These functions from `command_handling` are used to run system commands, with some requiring administrative privileges.
- **show_connection_info**: A function that provides information about the system's internet connection.
- **rm_Bloatware**: A function that helps remove bloatware (unnecessary pre-installed applications) from the system.
- **rm_dupe**: A function to remove duplicate files from the system.
- **clean_startup**: A function used to clean and manage startup programs.
- **open_speedtest_window**: A function that opens a window for the user to perform an internet speed test.
- **show_pc_info**: A function that displays detailed information about the user's PC.
- **create_buttons**: A utility function that creates GUI buttons for various actions in the application.

### Menu Functions

#### `show_info_menu()`
```python
def show_info_menu():
    clear_frame()
    buttons['systeminfo_button'].pack(pady=10)
    buttons['advanced_systeminfo_button'].pack(pady=10)
    buttons['resource_monitoring_button'].pack(pady=10)
    buttons['speedtest_button'].pack(pady=10)
    buttons['connection_button'].pack(pady=10)
    buttons['back_button'].pack(pady=10)
```
- This function clears the current frame using `clear_frame()` and then adds buttons related to system information and network connection. These buttons allow the user to access system info, advanced info, resource monitoring, perform a speed test, or view network connection information.

#### `show_clean_menu()`
```python
def show_clean_menu():
    clear_frame()
    buttons['rm_bloatware_button'].pack(pady=10)
    buttons['rm_dupe_button'].pack(pady=10)
    buttons['clean_mngr_button'].pack(pady=10)
    buttons['clean_startup_button'].pack(pady=10)
    buttons['wsreset_button'].pack(pady=10)
    buttons['disk_cleanup_button'].pack(pady=10)
    buttons['temp_cleanup_button'].pack(pady=10)
    buttons['prefetch_clean_button'].pack(pady=10)
    buttons['clean_invis_button'].pack(pady=10)
    buttons['defragment_button'].pack(pady=10)
    buttons['clean_vs_button'].pack(pady=10)
    buttons['Empty_RecycleBin_button'].pack(pady=10)
    buttons['back_button'].pack(pady=10)
```
- This function displays cleaning-related buttons. It includes options for removing bloatware, duplicate files, managing startup programs, running disk cleanup, and more. Each button corresponds to a function that will clean or optimize different areas of the system.

#### `show_update_menu()`
```python
def show_update_menu():
    clear_frame()
    buttons['update_apps_button'].pack(pady=10)
    buttons['windows_update_button'].pack(pady=10)
    buttons['driver_update_button'].pack(pady=10)
    buttons['back_button'].pack(pady=10)
```
- This function shows buttons related to updating system applications, Windows, and drivers. It helps users keep their system up to date with the latest software versions.

#### `show_repair_menu()`
```python
def show_repair_menu():
    clear_frame()
    buttons['health_scan_button'].pack(pady=10)
    buttons['storage_diagonistics_button'].pack(pady=10)
    buttons['repair_file_system_button'].pack(pady=10)
    buttons['repair_connection_button'].pack(pady=10)
    buttons['back_button'].pack(pady=10)
```
- This function presents options for repairing system health, running storage diagnostics, fixing the file system, and repairing network connections. These options help the user troubleshoot and maintain the PC.

#### `show_main_menu()`
```python
def show_main_menu():
    clear_frame()
    buttons['info_button'].pack(pady=10)
    buttons['clean_button'].pack(pady=10)
    buttons['update_button'].pack(pady=10)
    buttons['repair_button'].pack(pady=10)
    buttons['help_button'].pack(pady=10)
```
- This is the main menu of the application. It provides buttons to navigate to other categories: System Info, Clean, Update, Repair, and Help.

#### `clear_frame()`
```python
def clear_frame():
    for widget in root.winfo_children():
        widget.pack_forget()
```
- This function clears the current GUI window by "forgetting" (removing) all widgets. It is used to reset the window content when transitioning between different menus.

### GUI Setup and Main Event Loop

```python
root = tk.Tk()
root.title("PC Optimus")
root.geometry("400x600")
root.configure(bg="#2E2E2E")
```
- Initializes the main Tkinter window (`root`), sets its title, dimensions, and background color.

```python
create_shortcut()
```
- Calls the `create_shortcut()` function to ensure that any necessary shortcuts are created for the application.

```python
buttons = create_buttons(
    root, show_main_menu, show_info_menu, show_clean_menu, show_update_menu, show_repair_menu
)
```
- The `create_buttons()` function is called to generate buttons for each menu. The buttons are linked to the functions defined earlier, which determine the behavior of the app when clicked.

```python
show_main_menu()
```
- Displays the main menu when the application starts.

```python
root.mainloop()
```
- Starts the Tkinter event loop, which waits for user interactions and keeps the window open.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## UI/Buttons.py

This file defines the creation and configuration of various buttons for the PC Optimus application's graphical user interface (GUI) using Tkinter. Each button is linked to a specific action or function.

### Imports
```python
from tkinter import messagebox, ttk, scrolledtext, Listbox, Toplevel
import psutil
import tkinter as tk
import tkinter.messagebox as messagebox
import threading
import subprocess
import os
from Features.clean.tiny_clean_features import clean_recycle_bin, clean_vs, defragment
from Features.command_handling import run_command, run_admin_command, run_window_admin_command
from Features.logging_func import log_command, log_error
from Features.info.connection import show_connection_info
from Features.help import show_help
from Features.clean.rm_bloat import rm_Bloatware
from Features.clean.rm_dupe import rm_dupe
from Features.clean.clean_startup import clean_startup
from Features.info.internet_speedtest import open_speedtest_window
from Features.info.pc_info import show_pc_info
```

- **Tkinter Modules**: Used to create and manage GUI components like buttons, message boxes, and text fields.
- **psutil**: A library for interacting with system and process information, although not directly used in this snippet.
- **Features Modules**: Various features related to cleaning, optimizing, and gathering system information (such as removing bloatware, cleaning the recycle bin, and showing PC info).
- **subprocess, threading, os**: Libraries used for running system commands and executing background tasks.

### `create_buttons` Function

This function defines the appearance and functionality of each button in the app. It sets a consistent button style and links each button to its corresponding command or action. Here's a breakdown of how the function works:

```python
def create_buttons(root, show_main_menu, show_info_menu, show_clean_menu, show_update_menu, show_repair_menu):
    button_style = {
        "bg": "#444",
        "fg": "white",
        "activebackground": "#555",
        "activeforeground": "white",
        "borderwidth": 1,
        "relief": "raised"
    }
```
- **Button Style**: A dictionary defining the visual appearance of the buttons (background color, text color, active states, and border).

#### Button Definitions

Each button is created using `tk.Button`, where the root window (`root`) is the parent container, the text is the label on the button, and the command specifies the function to be executed when the button is clicked. Here's an example of how the buttons are created and linked to their actions:

```python
buttons = {
    "repair_file_system_button": tk.Button(root, text="Repair Filesystem", command=lambda: run_admin_command("echo J | chkdsk /f", "Successfully initiated chkdsk, your File System will be checked on the next startup.", root), **button_style),
    "clean_vs_button": tk.Button(root, text="Clean Virtual Storage", command=clean_vs, **button_style),
    "rm_dupe_button": tk.Button(root, text="Remove File Duplicates", command=lambda: rm_dupe(root), **button_style),
    "info_button": tk.Button(root, text="Info", command=show_info_menu, **button_style),
    "repair_button": tk.Button(root, text="Repair", command=show_repair_menu, **button_style),
    "systeminfo_button": tk.Button(root, text="Systeminfo", command=show_pc_info, **button_style),
    "advanced_systeminfo_button": tk.Button(root, text="Advanced Systeminfo", command=lambda: run_command("msinfo32.exe", "Successfully Retrieved Advanced Systeminfo."), **button_style),
    "resource_monitoring_button": tk.Button(root, text="Resource Monitoring", command=lambda: run_command("perfmon.exe /res", "Successfully ran Windows Resource Monitoring."), **button_style),
    "speedtest_button": tk.Button(root, text="Internet Speed", command=lambda: open_speedtest_window(root), **button_style),
    "connection_button": tk.Button(root, text="Connection", command=lambda: show_connection_info(root), **button_style),
    "health_scan_button": tk.Button(root, text="Repair System Files", command=lambda: run_window_admin_command("title Health Scan && cls && sfc /scannow && DISM /Online /Cleanup-Image /RestoreHealth && pause", "Successfully started Scanning for Errors.", root), **button_style),
    "clean_button": tk.Button(root, text="Clean", command=show_clean_menu, **button_style),
    "clean_mngr_button": tk.Button(root, text="Clean Manager", command=lambda: run_command("cleanmgr", "Disk cleanup completed successfully."), **button_style),
    "wsreset_button": tk.Button(root, text="WSReset", command=lambda: run_command("wsreset.exe", "Microsoft Store reset completed successfully."), **button_style),
    "disk_cleanup_button": tk.Button(root, text="Disk Cleanup", command=lambda: run_command("cleanmgr /sagerun:1", "Advanced Disk Cleanup completed successfully."), **button_style),
    "temp_cleanup_button": tk.Button(root, text="Temp Cleanup", command=lambda: run_command(r"del /q/f/s %TEMP%\*", "Successfully deleted Temporary Files."), **button_style),
    "prefetch_clean_button": tk.Button(root, text="Prefetch Cleanup", command=lambda: run_command(r"del /q/s C:\Windows\prefetch\*", "Successfully cleaned up Prefetch Files."), **button_style),
    "clean_invis_button": tk.Button(root, text="Clean Invis", command=lambda: run_window_admin_command(r"cipher /w:c && msg * Successfully Cleaned invisible Space Consuming Files && exit", "Successfully ran Windows Cipher.", root), **button_style),
    "Empty_RecycleBin_button": tk.Button(root, text="Empty Recycle Bin", command=clean_recycle_bin, **button_style),
    "defragment_button": tk.Button(root, text="Defragment", command=defragment, **button_style),
    "storage_diagonistics_button": tk.Button(root, text="Storage Diagnostics", command=lambda: run_command("MdSched.exe", "Successfully ran Windows Storage Diagnostics."), **button_style),
    "update_button": tk.Button(root, text="Update", command=show_update_menu, **button_style),
    "update_apps_button": tk.Button(root, text="Update Apps", command=lambda: run_window_admin_command("title Updater && cls && winget upgrade --all", "Winget initiated successfully.", root), **button_style),
    "windows_update_button": tk.Button(root, text="Windows Update", command=lambda: run_command("wuauclt /detectnow /updatenow", "Windows update initiated successfully."), **button_style),
    "repair_connection_button": tk.Button(root, text="Repair Connection", command=lambda: run_admin_command("ipconfig /flushdns && netsh winsock reset && ipconfig /release && ipconfig /renew", "Successfully reset Network and tried to fix Connection Problems.", root), **button_style),
    "driver_update_button": tk.Button(root, text="Driver Update", command=lambda: run_command("wuauclt /detectnow /updatenow", "Drivers updated successfully."), **button_style),
    "back_button": tk.Button(root, text="Back", command=show_main_menu, **button_style),
    "help_button": tk.Button(root, text="Help", command=lambda: print("Show Help (Placeholder)"), **button_style),
    "rm_bloatware_button": tk.Button(root, text="Remove Bloatware", command=lambda: rm_Bloatware(root), **button_style),
    "clean_startup_button": tk.Button(root, text="Clean Startup", command=lambda: clean_startup(root), **button_style)
}
```

Each button in the dictionary is configured with:
- **Text**: The label that appears on the button.
- **Command**: A function that is executed when the button is clicked.
- **Button Style**: The visual appearance set earlier using the `button_style` dictionary.

### Summary

The `create_buttons` function is central to creating the interactive elements of the PC Optimus application. It defines and returns a dictionary of buttons, each linked to a specific system maintenance task like cleaning temporary files, updating apps, running disk cleanup, and much more. By organizing buttons in a dictionary, the application easily manages the UI components.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Features/admin_elevate.py

This file contains functions that handle administrative privileges for running the PC Optimus application on Windows. It checks if the current user has administrator rights and provides a way to elevate the current process to administrator privileges if necessary.

### Imports
```python
import ctypes
import os
import sys
```
- **ctypes**: A foreign function library that allows calling functions in DLLs or shared libraries. It's used here to interact with Windows APIs to check and request administrative privileges.
- **os**: Provides a way to interact with the operating system, in this case, to determine the absolute path of the current script.
- **sys**: Provides access to some variables used or maintained by the Python interpreter, specifically `sys.argv[0]` for getting the script path.

### `is_admin` Function

```python
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
```

- **Purpose**: This function checks whether the current user has administrator rights.
- **Implementation**:
  - The function calls the `IsUserAnAdmin()` method from the `shell32` library using `ctypes.windll`.
  - If this method returns `True`, the user is an administrator, and the function returns `True`.
  - If an exception is raised (e.g., the method is not available), the function returns `False`, indicating the user does not have administrator rights.

### `elevate` Function

```python
def elevate(root):
    # Get the absolute path to the current Python executable
    script = os.path.abspath(sys.argv[0])
    root.destroy()
    # Restart the script with administrator privileges
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, f'"{script}"', None, 1)
```

- **Purpose**: This function restarts the current script with administrator privileges.
- **Implementation**:
  - The function first retrieves the absolute path of the current Python script using `os.path.abspath(sys.argv[0])`.
  - Then, it destroys the current Tkinter root window (`root.destroy()`) to close the application, as it will restart with elevated privileges.
  - Finally, the script is relaunched using the `ShellExecuteW` method from `ctypes.windll.shell32`. The `runas` command is used to request administrator rights, and the script is passed as an argument to be re-executed with those privileges.

### Summary

The `admin_elevate.py` file provides two essential functions for managing administrative privileges on Windows:
1. `is_admin()` checks whether the current user has administrator rights.
2. `elevate()` restarts the script with elevated (administrator) privileges if required.

These functions are crucial for operations that require administrative rights, such as making system-wide changes or running commands that modify system files or configurations.



## Features/command_handling.py

This file contains functions that handle the execution of system commands, particularly focusing on running them with administrative privileges. It also includes error handling and logging for successful or failed command executions.

### Imports
```python
import subprocess
import platform
from Features.logging_func import log_command, log_error
import chardet
import tkinter as tk
from tkinter import messagebox
from Features.admin_elevate import is_admin, elevate
import os
```
- **subprocess**: Allows spawning new processes, connecting to their input/output/error pipes, and obtaining their return codes. It is used for executing system commands.
- **platform**: Provides access to the underlying platform (e.g., Windows, Linux), which is used here to check the operating system.
- **logging_func**: Custom logging functions `log_command` and `log_error` are imported for logging command execution results and errors.
- **chardet**: A library to detect the encoding of byte data, ensuring correct decoding of the output from subprocesses.
- **tkinter**: The standard Python interface to the Tk GUI toolkit, used here for showing message boxes.
- **messagebox**: Provides pop-up dialog boxes for displaying information or errors to the user.
- **admin_elevate**: Functions `is_admin` and `elevate` are used to check and request administrator privileges when necessary.
- **os**: Used for interacting with the operating system, including quitting the program and terminating processes.

### `run_command` Function
```python
def run_command(command, success_message):
    try:
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        stdout, stderr = process.communicate()
        
        # Detect encoding of the output
        result_encoding = chardet.detect(stdout)['encoding']
        if result_encoding is None:
            result_encoding = 'utf-8'  # Fallback to UTF-8 if no encoding detected
        
        if process.returncode == 0:
            log_command(command, stdout.decode(result_encoding, errors='ignore'))
            messagebox.showinfo("Success", success_message)
        else:
            log_command(command, stderr.decode(result_encoding, errors='ignore'))
            raise subprocess.CalledProcessError(process.returncode, command, output=stderr)
    except Exception as e:
        log_error(f"Error running command: {command}", e)
        messagebox.showerror("Error", "An error occurred. Please check the log file for details.")
```
- **Purpose**: This function runs a system command, logs the result, and shows a message box indicating success or failure.
- **Implementation**:
  - It uses `subprocess.Popen` to run the command, capturing both the standard output (`stdout`) and error output (`stderr`).
  - The `chardet` library detects the encoding of the command output to ensure correct decoding.
  - If the command executes successfully (`returncode == 0`), the output is logged, and a success message is shown.
  - If the command fails, the error output is logged, and an exception is raised.
  - In case of any exception, an error message is shown to the user, and the error is logged.

### `run_admin_command` Function
```python
def run_admin_command(command, success_message, root):
    try:
        if platform.system() == "Windows":
            if is_admin():
                # Execute command directly as admin
                creationflags = subprocess.CREATE_NO_WINDOW
                result = subprocess.run(command, shell=True, creationflags=creationflags)
                if result.returncode == 0 or result.returncode == 3:  # Ignore exit code 3
                    messagebox.showinfo("Success", success_message)
                else:
                    messagebox.showerror("Error", f"Command failed with return code {result.returncode}")
            else:
                # Restart the script with elevated privileges
                messagebox.showinfo("Info", "This action requires administrator privileges. The program will restart with elevated rights.")
                elevate(root)
                root.quit()  # Close the old window
                os._exit(0)  # Immediately terminate the old process
        else:
            # For other platforms, run the command normally
            result = subprocess.run(command, shell=True)
            if result.returncode == 0 or result.returncode == 3:  # Ignore exit code 3
                messagebox.showinfo("Success", success_message)
            else:
                messagebox.showerror("Error", f"Command failed with return code {result.returncode}")
    except Exception as e:
        log_error(f"Error running admin command: {command}", e)
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
```
- **Purpose**: This function runs a system command with administrator privileges if required.
- **Implementation**:
  - First, it checks if the operating system is Windows using `platform.system()`.
  - If the user already has admin privileges (`is_admin()`), the command is executed using `subprocess.run()`, and no window is shown (`CREATE_NO_WINDOW` flag).
  - If the user doesn't have admin rights, the program restarts with elevated privileges using the `elevate()` function, and the old window is closed immediately.
  - If the command is executed successfully, a success message is displayed; otherwise, an error message is shown.
  - On non-Windows platforms, the command is run without elevation, and any failures are reported.

### `run_window_admin_command` Function
```python
def run_window_admin_command(command, success_message, root):
    try:
        if platform.system() == "Windows":
            if is_admin():
                # Execute the command in a new CMD window
                full_command = f'start cmd /k "{command}"'
                result = subprocess.run(full_command, shell=True)
                if result.returncode == 0 or result.returncode == 3:  # Ignore exit code 3
                    messagebox.showinfo("Success", success_message)
                else:
                    messagebox.showerror("Error", f"Command failed with return code {result.returncode}")
            else:
                # Restart the script with elevated privileges
                messagebox.showinfo("Info", "This action requires administrator privileges. The program will restart with elevated rights.")
                elevate(root)
                if root is not None:
                    root.quit()
                os._exit(0)  # Terminates the process
        else:
            # For other platforms, run the command normally
            result = subprocess.run(command, shell=True)
            if result.returncode == 0 or result.returncode == 3:  # Ignore exit code 3
                messagebox.showinfo("Success", success_message)
            else:
                messagebox.showerror("Error", f"Command failed with return code {result.returncode}")
    except Exception as e:
        log_error(f"Error running admin command in window mode: {command}", e)
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
```
- **Purpose**: This function is similar to `run_admin_command`, but it runs the command in a new command window (`cmd`) for better visibility.
- **Implementation**:
  - The command is prefixed with `start cmd /k` to run it in a new CMD window.
  - The rest of the logic is similar to `run_admin_command`, ensuring the command is run with administrator privileges if required.

### Summary

The `command_handling.py` file provides essential functionality for running system commands, with special handling for elevated (administrator) privileges:
1. `run_command` runs a system command and handles the output, logging it and showing appropriate messages to the user.
2. `run_admin_command` ensures that commands requiring administrative privileges are run with those privileges on Windows.
3. `run_window_admin_command` runs commands requiring elevated privileges in a new command window for visibility.
4. The file also handles errors gracefully, logging them and showing the user relevant messages about success or failure.



### Features/help.py

The `help.py` file provides a function to display a help message that outlines the available features and their descriptions. This is typically shown to the user when they need information on how to use the program's various tools and options.

### Code Breakdown

```python
import tkinter.messagebox as messagebox
```
- **tkinter.messagebox**: The `messagebox` module from `tkinter` is used to display pop-up windows to show messages to the user. In this case, it is used to display a help message with a list of available features.

### `show_help` Function

```python
def show_help():
    help_text = (
        "Info:\n"
        "Info: Shows information about the PC.\n"
        "Systeminfo: Displays basic system information.\n"
        "Advanced Systeminfo: Retrieves advanced system information.\n"
        "Resource Monitoring: Opens the Windows Resource Monitor.\n"
        "Speedtest: Runs a speed test.\n"
        "Connection: Shows network connection information.\n\n"

        "Clean:\n"
        "Clean: Starts the Windows Disk Cleanup.\n"
        "WSReset: Resets the Microsoft Store and clears its cache.\n"
        "Disk Cleanup: Performs an advanced disk cleanup.\n"
        "Temp Cleanup: Deletes temporary files.\n"
        "Clean Invis: Deletes invisible space-consuming files.\n"
        "Clean Manager: Launches the Disk Cleanup Manager.\n"
        "Empty Recycle Bin: Empties the Recycle Bin.\n"
        "Defragment: Performs a disk defragmentation.\n"
        "Clean Virtual Storage: Cleans virtual storage.\n\n"

        "Update:\n"
        "Update All: Updates all installed applications.\n"
        "Windows Update: Checks for new Windows updates.\n"
        "Driver Update: Updates all drivers.\n"
        "Update Apps: Updates all installed apps using Winget.\n\n"

        "Repair:\n"
        "Repair Filesystem: Initiates a check disk operation to repair filesystem errors.\n"
        "Repair System Files: Scans and repairs system files using SFC and DISM.\n"
        "Repair Connection: Repairs network connection issues.\n\n"

        "Help: Shows this help message."
    )
    messagebox.showinfo("Help", help_text)
```

- **Purpose**: This function displays a help message in a pop-up window that explains the various features available in the program.
  
- **Functionality**:
  - The `help_text` variable contains a formatted string that lists all the major sections of the program, such as:
    - **Info**: Provides system information tools like basic and advanced system info, resource monitoring, speed tests, and connection information.
    - **Clean**: Describes tools for disk cleanup, such as cleaning temporary files, defragmenting the disk, and emptying the recycle bin.
    - **Update**: Lists the tools for updating apps, Windows, and drivers.
    - **Repair**: Details commands for repairing the file system, system files, and network connection.
    - **Help**: Provides access to this help message itself.
  
  - After defining the help text, `messagebox.showinfo` is called to display it in a pop-up window with the title "Help."

### Purpose and Usage

This file allows users to easily access a comprehensive help guide detailing all of the program's functionality. When the user calls the `show_help()` function, they will be presented with a readable list of available features. The user can then follow the description to understand what each option does and how to use them.

The help message is structured and categorized for clarity, helping users navigate through different sections of system information, cleanup, updates, repairs, and more.

### Example Output (in messagebox):
```
Help

Info:
Info: Shows information about the PC.
Systeminfo: Displays basic system information.
Advanced Systeminfo: Retrieves advanced system information.
Resource Monitoring: Opens the Windows Resource Monitor.
Speedtest: Runs a speed test.
Connection: Shows network connection information.

Clean:
Clean: Starts the Windows Disk Cleanup.
WSReset: Resets the Microsoft Store and clears its cache.
Disk Cleanup: Performs an advanced disk cleanup.
Temp Cleanup: Deletes temporary files.
Clean Invis: Deletes invisible space-consuming files.
Clean Manager: Launches the Disk Cleanup Manager.
Empty Recycle Bin: Empties the Recycle Bin.
Defragment: Performs a disk defragmentation.
Clean Virtual Storage: Cleans virtual storage.

Update:
Update All: Updates all installed applications.
Windows Update: Checks for new Windows updates.
Driver Update: Updates all drivers.
Update Apps: Updates all installed apps using Winget.

Repair:
Repair Filesystem: Initiates a check disk operation to repair filesystem errors.
Repair System Files: Scans and repairs system files using SFC and DISM.
Repair Connection: Repairs network connection issues.

Help: Shows this help message.
```

### Conclusion

The `show_help` function provides users with an overview of all the tools and options in the program, helping them understand the purpose of each feature and how to use it. This is a vital utility for improving user experience by making the program more accessible.



### Features/logging_func.py

The `logging_func.py` file contains functions that help log various types of information, such as commands executed and errors encountered, to a log file. This is important for debugging and tracking the program's actions over time. The log entries are timestamped, which provides insight into when specific actions occurred.

### Code Breakdown

```python
import os
import time
```
- **`os` module**: This module is used to interact with the operating system, particularly for file handling, such as getting the directory path where the script is located.
- **`time` module**: This module is used to work with time-related tasks, such as generating timestamps for the log entries.

```python
script_dir = os.path.dirname(os.path.abspath(__file__))
```
- This line gets the absolute path of the directory where the script is located. This will be used as the base directory for the log file (`log.txt`).

### `log_command` Function

```python
def log_command(command, output):
    with open(os.path.join(script_dir, "log.txt"), "a") as f:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[COMMAND] [{timestamp}] {command}\n")
        f.write(f"[OUTPUT] {output}\n")
```
- **Purpose**: This function logs the details of a command that has been executed and its output.
- **Parameters**:
  - `command`: The command string that was executed.
  - `output`: The output or result of the command execution (either success or failure messages).
  
- **Process**:
  1. The function opens the `log.txt` file in append mode (`"a"`), ensuring that new log entries are added to the end of the file.
  2. It then records the current timestamp using `time.strftime("%Y-%m-%d %H:%M:%S")`, which formats the current time in a readable way (e.g., `2024-12-30 14:25:38`).
  3. The command and its output are written into the log file, prefixed with the `[COMMAND]` and `[OUTPUT]` labels, respectively.

### `log_error` Function

```python
def log_error(message, error):
    with open(os.path.join(script_dir, "log.txt"), "a") as f:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[ERROR] [{timestamp}] {message}\n")
        f.write(f"[DETAILS] {str(error)}\n")
```
- **Purpose**: This function logs error messages along with additional error details, such as the exception information.
- **Parameters**:
  - `message`: A brief description of the error.
  - `error`: The actual error object (usually an exception) that provides more details about what went wrong.

- **Process**:
  1. Similar to `log_command`, the function opens the `log.txt` file in append mode.
  2. It adds a timestamp to indicate when the error occurred.
  3. It then writes the error message (describing the nature of the error) and the error details (the full error message, typically generated by an exception).

### Example Log Entries

#### Command Log Example:

```
[COMMAND] [2024-12-30 14:25:38] chkdsk /f
[OUTPUT] Successfully initiated chkdsk, your File System will be checked on the next startup.
```

#### Error Log Example:

```
[ERROR] [2024-12-30 14:30:45] Error running command: chkdsk /f
[DETAILS] Command 'chkdsk /f' returned non-zero exit status 1.
```

### Purpose and Usage

- **Logging Commands**: By logging the commands executed and their outputs, the program can keep track of the actions taken by the user or the system. This is useful for debugging and monitoring.
  
- **Logging Errors**: The `log_error` function ensures that when an error occurs, the error message and the exception details are saved in the log file. This helps in identifying and resolving issues during the program's execution.
  
- The logs will be stored in a file named `log.txt` in the same directory as the script, and each log entry will be timestamped for clarity.

### Conclusion

The `logging_func.py` file ensures that all important actions (commands and errors) are recorded in a log file, providing an audit trail for both successful operations and failures. This is valuable for debugging, troubleshooting, and understanding the program's behavior over time.



### Features/shortcut.py

The `shortcut.py` file contains functionality for creating shortcuts to a script in both the Windows Start Menu and the Desktop. This feature allows users to easily access the program through shortcuts, improving usability.

### Code Breakdown

#### Imports

```python
import os
import sys
import win32com.client
import tkinter.messagebox as messagebox
import tkinter as tk
```
- **`os`**: Used for interacting with the operating system, particularly for handling paths and file operations.
- **`sys`**: Provides access to system-specific parameters and functions. Here, it's used to get the Python executable path.
- **`win32com.client`**: A Python module for COM (Component Object Model) automation, which allows interacting with Windows applications like the desktop shell to create shortcuts.
- **`tkinter`**: Provides the GUI components for the application, including message boxes to interact with the user.

#### `create_shortcut` Function

The `create_shortcut` function is the core of this file, responsible for creating a shortcut to the current Python script both in the Start Menu and optionally on the Desktop.

##### Step-by-Step Explanation:

1. **Determine Paths**:
   ```python
   script_path = os.path.abspath(__file__)
   python_exe = sys.executable
   command = f'"{python_exe}" "{script_path}"'
   ```
   - **`script_path`**: Gets the absolute path of the current Python script.
   - **`python_exe`**: Gets the path of the Python executable, which is used to run the script.
   - **`command`**: This is the command string that will be used as the target of the shortcut. It ensures the script is executed by Python.

2. **Define Shortcut Name and Path**:
   ```python
   shortcut_name = 'PCOptimus'
   start_menu_path = os.path.join(os.environ['APPDATA'], 'Microsoft', 'Windows', 'Start Menu', 'Programs')
   shortcut_path = os.path.join(start_menu_path, f"{shortcut_name}.lnk")
   ```
   - **`shortcut_name`**: The name given to the shortcut (`PCOptimus`).
   - **`start_menu_path`**: The location where shortcuts are placed in the Start Menu.
   - **`shortcut_path`**: The full path of the shortcut file to be created in the Start Menu.

3. **Check if Shortcut Exists**:
   ```python
   if os.path.exists(shortcut_path):
       print(f"The shortcut '{shortcut_name}' already exists at: {shortcut_path}")
   ```
   - Before creating the shortcut, the script checks if a shortcut already exists at the specified location.

4. **Create the Shortcut**:
   ```python
   shell = win32com.client.Dispatch('WScript.Shell')
   shortcut = shell.CreateShortcut(shortcut_path)
   shortcut.TargetPath = python_exe
   shortcut.Arguments = f'"{script_path}"'
   shortcut.WorkingDirectory = os.path.dirname(script_path)
   shortcut.IconLocation = python_exe
   shortcut.save()
   ```
   - The script uses `win32com.client.Dispatch` to access Windows' `WScript.Shell`, which allows it to create and manage shortcuts.
   - **`TargetPath`** is set to the Python executable (`python_exe`), which will run the script.
   - **`Arguments`** is set to the script's path to be passed to the Python executable.
   - **`WorkingDirectory`** is set to the directory of the script to ensure it runs in the correct context.
   - **`IconLocation`**: Uses the Python executable's icon for the shortcut.
   - The shortcut is then saved with the `.lnk` extension.

5. **Notify User About Start Menu Shortcut**:
   ```python
   messagebox.showinfo("PCOptimus Shortcut Created", "PCOptimus is now available in the Start Menu.\n")
   ```
   - A message box informs the user that the shortcut has been created in the Start Menu.

6. **Option to Create Desktop Shortcut**:
   ```python
   if messagebox.askyesno("Create Desktop Shortcut?", "Do you want to create a Desktop shortcut for PCOptimus?"):
       desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
       desktop_shortcut_path = os.path.join(desktop_path, f"{shortcut_name}.lnk")
   ```
   - After confirming the creation of the Start Menu shortcut, the user is asked if they want to create a desktop shortcut as well.
   - **`desktop_path`**: The path to the user's Desktop folder is calculated.

7. **Create Desktop Shortcut**:
   ```python
   if not os.path.exists(desktop_shortcut_path):
       desktop_shortcut = shell.CreateShortcut(desktop_shortcut_path)
       desktop_shortcut.TargetPath = python_exe
       desktop_shortcut.Arguments = f'"{script_path}"'
       desktop_shortcut.WorkingDirectory = os.path.dirname(script_path)
       desktop_shortcut.IconLocation = python_exe
       desktop_shortcut.save()
       messagebox.showinfo("Desktop Shortcut Created", f"Desktop shortcut '{shortcut_name}' successfully created.")
   ```
   - Similar to the Start Menu shortcut, the script creates a shortcut on the Desktop if one does not already exist.

8. **Handle Exceptions**:
   ```python
   except Exception as e:
       messagebox.showerror("Error Creating Shortcut", f"Error creating the shortcut: {e}")
   ```
   - If an error occurs during the process of creating the shortcut, an error message is displayed to the user.

### User Interaction

- **Start Menu Shortcut**: When the function is run, it will automatically create a shortcut for the script in the Start Menu.
- **Desktop Shortcut**: After the Start Menu shortcut is created, the user is prompted to optionally create a shortcut on the Desktop.

### Conclusion

The `create_shortcut` function provides a convenient way for users to quickly access the PCOptimus script via a shortcut. It creates a Start Menu shortcut by default and offers an optional Desktop shortcut. If any issues occur during the shortcut creation, the function catches the exception and informs the user with a helpful error message.




------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

***I hope this helped you to understand my Code :)***

