# PCOptimus Documentation

Here you will find an Explaination to every Part of the Code that is Python.

# Tree:

[PCOptimus.py](https://github.com/truelockmc/PC-Optimus/blob/main/Documentation/Python%20Code%20Doc.md#pcoptimuspy---main-file)  
├── UI
│   ├── [Buttons.py](https://github.com/truelockmc/PC-Optimus/blob/main/Documentation/Python%20Code%20Doc.md#uibuttonspy)  
│   └── [__init__.py](https://github.com/truelockmc/PC-Optimus/blob/main/Documentation/Python%20Code%20Doc.md#__init__py-files)  
├── Features  
│   ├── [command_handling.py](https://github.com/truelockmc/PC-Optimus/blob/main/Documentation/Python%20Code%20Doc.md#featurescommand_handlingpy)  
│   ├── [help.py](https://github.com/truelockmc/PC-Optimus/blob/main/Documentation/Python%20Code%20Doc.md#featureshelppy)  
│   ├── [logging_func.py](https://github.com/truelockmc/PC-Optimus/blob/main/Documentation/Python%20Code%20Doc.md#featureslogging_funcpy)  
│   ├── [shortcut.py](https://github.com/truelockmc/PC-Optimus/blob/main/Documentation/Python%20Code%20Doc.md#featuresshortcutpy)  
│   ├── [__init__.py](https://github.com/truelockmc/PC-Optimus/blob/main/Documentation/Python%20Code%20Doc.md#__init__py-files)  
│   ├── [admin_elevate.py](https://github.com/truelockmc/PC-Optimus/blob/main/Documentation/Python%20Code%20Doc.md#featuresadmin_elevatepy)  
│   ├── clean  
│   │   ├── [__init__.py](https://github.com/truelockmc/PC-Optimus/blob/main/Documentation/Python%20Code%20Doc.md#__init__py-files)  
│   │   ├── [adv_bloat.py](https://github.com/truelockmc/PC-Optimus/blob/main/Documentation/Python%20Code%20Doc.md#featurescleanadv_bloatpy)  
│   │   ├── [clean_startup.py](https://github.com/truelockmc/PC-Optimus/blob/main/Documentation/Python%20Code%20Doc.md#featurescleanclean_startuppy)  
│   │   ├── [rm_bloat.py](https://github.com/truelockmc/PC-Optimus/blob/main/Documentation/Python%20Code%20Doc.md#featurescleanrm_bloatpy)  
│   │   ├── [rm_dupe.py](https://github.com/truelockmc/PC-Optimus/blob/main/Documentation/Python%20Code%20Doc.md#featurescleanrm_dupepy)  
│   │   └── [tiny_clean_features.py](https://github.com/truelockmc/PC-Optimus/blob/main/Documentation/Python%20Code%20Doc.md#featurescleantiny_clean_featurespy)  
│   ├── info  
│   │   ├── [__init__.py](https://github.com/truelockmc/PC-Optimus/blob/main/Documentation/Python%20Code%20Doc.md#__init__py-files)  
│   │   ├── [connection.py](https://github.com/truelockmc/PC-Optimus/blob/main/Documentation/Python%20Code%20Doc.md#featuresinfoconnectionpy)  
│   │   ├── [internet_speedtest.py](https://github.com/truelockmc/PC-Optimus/blob/main/Documentation/Python%20Code%20Doc.md#featuresinfointernet_speedtestpy)  
│   │   └── [pc_info.py](https://github.com/truelockmc/PC-Optimus/blob/main/Documentation/Python%20Code%20Doc.md#featuresinfopc_infopy)  


----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# ``` __init__.py ``` Files

Thise Files dont contain any Code, but the Program needs them to run, because of the following Points:

- **Package Initialization**: The `__init__.py` file is executed when a package or module is imported. It can contain package-level variables, functions, or initialization code.
  
- **Marking a Directory as a Package**: The presence of `__init__.py` turns a directory into a Python package. Without it, Python treats the directory as a regular folder, not a package.

- **Optional in Modern Python**: In Python 3.3 and above, `__init__.py` is not strictly required, but it is still commonly used for backward compatibility and for structuring packages.


----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# PCOptimus.py - Main File

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

# UI/Buttons.py

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

# Features/admin_elevate.py

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



# Features/command_handling.py

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



# Features/help.py

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



# Features/logging_func.py

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



# Features/shortcut.py

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



# Features/clean/clean_startup.py

The `clean_startup.py` file is a utility that allows users to manage which applications are set to launch automatically when their Windows system starts. It includes functionalities to retrieve autostart programs, display them in a user interface, and allow the user to disable specific autostart applications. This file works by interacting with the Windows registry and startup folder.

### Code Breakdown

#### Imports

```python
import logging
from tkinter import messagebox, ttk, scrolledtext, Listbox, MULTIPLE, Toplevel
import tkinter as tk
import tkinter.messagebox as messagebox
import winreg
from Features.admin_elevate import elevate, is_admin
from Features.logging_func import log_error
import os
```
- **`logging`**: Used for logging messages, errors, and operations performed by the script.
- **`tkinter`**: The standard GUI library used to create graphical interfaces, including the display of programs and buttons for interaction.
- **`winreg`**: Provides functions to interact with the Windows registry. This is used to read and modify the registry entries related to autostart programs.
- **`os`**: Used for interacting with the operating system, especially for file system operations (e.g., accessing the Startup folder).

#### Logging Configuration

```python
logging.basicConfig(filename="log.txt", level=logging.INFO, 
                    format="%(asctime)s - %(levelname)s - %(message)s")
```
This sets up logging to write messages to `log.txt`. The log level is set to `INFO`, meaning messages of this level or higher (e.g., `ERROR`) will be logged. The log message format includes a timestamp, log level, and message content.

#### Critical Files and Directories

```python
critical_files = ["desktop.ini", "ntuser.dat", "pagefile.sys", "swapfile.sys"]
critical_dirs = ["system32", "SysWOW64"]
```
This defines a list of critical files and directories that should not be disabled. These files and directories are excluded from the autostart process to avoid removing essential system files.

#### `get_autostart_programs` Function

```python
def get_autostart_programs():
    autostart_programs = []
    # Registry-Einträge hinzufügen
    for key, (hive, path) in reg_paths.items():
        try:
            reg_key = winreg.OpenKey(hive, path)
            i = 0
            while True:
                try:
                    name, value, _ = winreg.EnumValue(reg_key, i)
                    if not any(cf.lower() in value.lower() for cf in critical_files + critical_dirs):
                        autostart_programs.append({"name": name, "path": value, "source": key})
                    i += 1
                except OSError:
                    break
            winreg.CloseKey(reg_key)
            logging.info(f"Startup Apps loaded from {path}")
        except Exception as e:
            logging.error(f"Error while trying to access {path}: {e}")
    
    # Autostart-Ordner
    startup_folder = os.path.expanduser("~\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup")
    if os.path.exists(startup_folder):
        for item in os.listdir(startup_folder):
            item_path = os.path.join(startup_folder, item)
            if os.path.isfile(item_path) and not any(cf.lower() in item.lower() for cf in critical_files):
                autostart_programs.append({"name": item, "path": item_path, "source": "Startup Folder"})
        logging.info("Gathered Startup Folder Apps")

    return autostart_programs
```

- **Registry Paths**: This function retrieves autostart programs from the Windows registry and the Startup folder.
- It uses **`winreg`** to open registry keys and enumerate values under specific registry paths (`HKCU_Run`, `HKLM_Run`, etc.).
- It also checks the **Startup folder** for executable files that are set to launch at startup.
- **Critical files and directories** are excluded from the results to avoid affecting essential system components.
- The results are returned as a list of dictionaries containing the program name, path, and source (registry or startup folder).

#### Registry Paths Definition

```python
reg_paths = {
    "HKCU_Run": (winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run"),
    "HKCU_RunOnce": (winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\RunOnce"),
    "HKLM_Run": (winreg.HKEY_LOCAL_MACHINE, r"Software\Microsoft\Windows\CurrentVersion\Run"),
    "HKLM_RunOnce": (winreg.HKEY_LOCAL_MACHINE, r"Software\Microsoft\Windows\CurrentVersion\RunOnce")
}
```
- **`reg_paths`** is a dictionary mapping the name of the registry key to the actual registry path where autostart programs are stored. The keys represent either current user (`HKCU`) or local machine (`HKLM`) registry hives.

#### `disable_selected_autostart` Function

```python
def disable_selected_autostart(selected_programs):
    for program in selected_programs:
        try:
            if program["source"] == "Startup Folder":
                os.remove(program["path"])
            else:
                hive, path = reg_paths[program["source"]]
                reg_key = winreg.OpenKey(hive, path, 0, winreg.KEY_SET_VALUE)
                winreg.DeleteValue(reg_key, program["name"])
                winreg.CloseKey(reg_key)
            logging.info(f"Deactivated: {program['name']} - {program['path']}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while deactivating startup for {program['name']}: {e}")
            logging.error(f"Error while deactivating {program['name']}: {e}")
```
This function is used to deactivate selected autostart programs:
- If the program is in the **Startup Folder**, it deletes the corresponding file.
- If the program is in the **registry**, it removes the registry entry.
- It logs each action and handles any errors by displaying a message box and logging the error.

#### `clean_startup` Function

```python
def clean_startup(root):
    if not is_admin():
        logging.info("Asking for right elevation.")
        elevate(root)
    else:
        logging.info("Admin already achieved")
        show_autostart_gui(root)
```
This function is executed when the user clicks the **"Clean Startup"** button. If the script is not run as an administrator, it requests elevation (admin privileges). If it already has admin privileges, it shows the autostart management GUI.

#### `show_autostart_gui` Function

```python
def show_autostart_gui(root):
    programs = get_autostart_programs()
    if not programs:
        messagebox.showinfo("No Startup Apps", "No startup apps found")
        logging.info("No startup apps found")
        return
    
    window = tk.Toplevel(root)
    window.title("Startup App Manager")
    window.configure(bg="#2e2e2e")
    
    checkboxes = []
    for program in programs:
        var = tk.BooleanVar()
        cb = tk.Checkbutton(window, text=f"{program['name']} ({program['source']}) - {program['path']}", variable=var,
                            bg="#2e2e2e", fg="white", selectcolor="#444", activebackground="#555", activeforeground="white")
        cb.pack(anchor="w", padx=10, pady=2)
        checkboxes.append((var, program))

    def disable_selected():
        selected_programs = [program for var, program in checkboxes if var.get()]
        if selected_programs:
            disable_selected_autostart(selected_programs)
            messagebox.showinfo("Startup App Deactivation", "Selected apps won't run on startup anymore.")
            logging.info("Selected apps successfully deactivated")
            window.destroy()
        else:
            messagebox.showwarning("Nothing selected", "Please select any app or close this window")
            logging.warning("Nothing selected")

    disable_button = tk.Button(window, text="Disable", command=disable_selected, bg="#444", fg="white",
                               activebackground="#555", activeforeground="white", borderwidth=1, relief="raised")
    disable_button.pack(pady=10)
```
- This function creates a GUI that allows the user to manage autostart programs.
- It uses **checkboxes** to let the user select which programs to disable.
- A **"Disable"** button deactivates the selected programs.
- If no programs are selected, a warning is shown.

### Conclusion

The `clean_startup.py` file provides a feature-rich tool for managing autostart programs on a Windows system. It allows users to:
- View and manage programs that launch automatically on system startup.
- Deactivate unnecessary or unwanted programs through a GUI interface.
- Ensure that critical system files and directories are not altered or removed.
- It handles administrative privileges, logging, and error reporting to ensure a smooth user experience.

This feature is useful for optimizing startup times by removing unnecessary programs from the autostart list.



# Features/clean/rm_bloat.py 

This Python file contains the function for removing bloatware from the system, including checking for installed apps, uninstalling selected apps, and handling user interactions with Tkinter.

### **Imports**
```python
import subprocess
import tkinter as tk
import tkinter.messagebox as messagebox
import os
from Features.logging_func import log_error, log_command
from Features.admin_elevate import is_admin, elevate
from Features.clean.adv_bloat import advanced_debloat
import logging
```

- **subprocess**: Used for running PowerShell commands to check and uninstall apps.
- **tkinter**: The main module for creating the graphical user interface (GUI) for the bloatware uninstaller.
- **log_error, log_command**: Imported for logging errors and commands executed during the uninstallation process.
- **is_admin, elevate**: Used to check for administrative privileges and elevate privileges if necessary.
- **advanced_debloat**: A function from `Features.clean.adv_bloat` that offers additional bloatware removal and tracking stopping functionalities.
- **logging**: Python's logging module to track the flow of operations and errors.

### **Bloatware List**

```python
bloatware_list = [
    ("Microsoft.BingNews", 80), ("Microsoft.Getstarted", 40), ("Microsoft.Messaging", 60),
    ("Microsoft.Microsoft3DViewer", 100), ("Microsoft.MicrosoftOfficeHub", 100), ("Microsoft.MicrosoftSolitaireCollection", 60),
    # More apps listed with their estimated size
]
```
- This list contains the bloatware apps to be detected and removed, paired with their estimated disk size in MB.

### **Helper Functions**

#### `run_powershell_command(command)`
```python
def run_powershell_command(command):
    try:
        result = subprocess.run(["powershell", "-Command", command], capture_output=True, text=True)
        result.check_returncode()
        logging.info(f"Command executed successfully: {command}")
        return result.stdout
    except subprocess.CalledProcessError as e:
        logging.error(f"Error executing command: {command} | Error: {e}")
        return ""
```
- **Purpose**: Executes a PowerShell command and returns the output. Logs any errors encountered.
- **Used For**: Running PowerShell commands to check installed apps and uninstall them.

#### `check_installed_apps(progress_label, root)`
```python
def check_installed_apps(progress_label, root):
    installed_apps = []
    progress_label.config(text="Checking for installed Bloatware...")
    root.update()

    for app, size in bloatware_list:
        if app in run_powershell_command(f"Get-AppxPackage -Name {app}"):
            installed_apps.append((app, size))

    progress_label.config(text="")
    return installed_apps
```
- **Purpose**: Scans the system for the bloatware apps listed and returns a list of installed apps with their size.
- **Used For**: Identifying which bloatware apps are installed on the system.

#### `uninstall_selected_apps(selected_apps)`
```python
def uninstall_selected_apps(selected_apps):
    for app, _ in selected_apps:
        command = f"Get-AppxPackage -Name {app} | Remove-AppxPackage"
        run_powershell_command(command)
        
        # Check if the app is still installed
        remaining = run_powershell_command(f"Get-AppxPackage -Name {app}")
        if app not in remaining:
            logging.info(f"Uninstalled: {app}")
        else:
            logging.error(f"Failed to uninstall: {app}")
```
- **Purpose**: Uninstalls the selected apps by running the `Remove-AppxPackage` command via PowerShell.
- **Used For**: Actually removing the bloatware apps from the system.

#### `confirm_uninstall(root)`
```python
def confirm_uninstall(root):
    dialog = tk.Toplevel(root)
    dialog.configure(bg="#333")
    dialog.title("Confirmation")
    tk.Label(dialog, text="Type 'Uninstall pls' to confirm", fg="white", bg="#333").pack(pady=10)
    entry = tk.Entry(dialog)
    entry.pack(pady=10)
    result = []

    def on_confirm():
        result.append(entry.get())
        dialog.destroy()

    tk.Button(dialog, text="Confirm", command=on_confirm, bg="#444", fg="white").pack(pady=10)
    dialog.transient(root)
    dialog.grab_set()
    root.wait_window(dialog)
    
    return result[0] if result else ""
```
- **Purpose**: Prompts the user to confirm the uninstallation of selected apps by typing a specific confirmation text.
- **Used For**: Preventing accidental uninstallation by requiring the user to type a confirmation phrase.

### **Main Bloatware Removal Function**

#### `rm_Bloatware(root)`
```python
def rm_Bloatware(root):
    if not is_admin():
        messagebox.showwarning("Admin Rights Required", "This action requires admin rights. The program will restart with elevated privileges.")
        elevate(root)
        root.quit()
        os._exit(0)
        return

    bloatware_window = tk.Toplevel(root)
    bloatware_window.title("Bloatware Uninstaller")
    bloatware_window.geometry("500x500")
    bloatware_window.configure(bg="#333")

    progress_label = tk.Label(bloatware_window, text="", fg="white", bg="#333")
    progress_label.pack(pady=10)

    installed_apps = check_installed_apps(progress_label, root)

    if not installed_apps:
        tk.Label(bloatware_window, text="Congrats, you're Bloatware free :)", fg="white", bg="#333").pack(pady=20)
        tk.Button(bloatware_window, text="Close", command=bloatware_window.destroy, bg="#444", fg="white").pack(pady=20)
        return

    vars_ = [tk.IntVar() for _ in installed_apps]
    
    tk.Label(bloatware_window, text="These Apps are potential unwanted Bloatware.", fg="white", bg="#333").pack(pady=10)
    
    # Add a frame with a canvas and scrollbar for scrollable checkboxes
    frame_container = tk.Frame(bloatware_window, bg="#333")
    frame_container.pack(fill="both", expand=True)

    canvas = tk.Canvas(frame_container, bg="#333")
    scrollbar = tk.Scrollbar(frame_container, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="#333")

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Populate the scrollable frame with checkboxes
    for i, (app, size) in enumerate(installed_apps):
        chk = tk.Checkbutton(scrollable_frame, text=f"{app} ({size} MB)", variable=vars_[i], 
                             fg="white", bg="#333", selectcolor="#444", activebackground="#555")
        chk.grid(row=i, column=0, sticky='w', padx=20, pady=2)

    label_info = tk.Label(bloatware_window, text="", fg="white", bg="#333")
    label_info.pack(pady=10)

    def on_check():
        selected = [(app, size) for i, (app, size) in enumerate(installed_apps) if vars_[i].get() == 1]
        total_size = sum(size for _, size in selected)
        label_info.config(text=f"You will have more than {total_size} MB more free Storage, and your PC will be faster.")
    
    def on_uninstall():
        checked_apps = [(app, size) for i, (app, size) in enumerate(installed_apps) if vars_[i].get() == 1]
        if not checked_apps:
            messagebox.showwarning("No Selection", "No apps selected for uninstallation.")
            return

        on_check()  # Update the info label before confirmation
        confirmation = confirm_uninstall(root)
        if confirmation == "Uninstall pls":
            uninstall_selected_apps(checked_apps)
            remaining_apps = check_installed_apps(progress_label, root)
            if not any(app in [a[0] for a in remaining_apps] for app, _ in checked_apps):
                messagebox.showinfo("Uninstallation Complete", "Selected apps have been uninstalled.")
            else:
                messagebox.showerror("Uninstallation Failed", "Some apps could not be uninstalled.")
            bloatware_window.destroy()
        else:
            messagebox.showinfo("Uninstallation Cancelled", "No apps were uninstalled.")

    tk.Button(bloatware_window, text="Uninstall selected", command=on_uninstall, bg="#444", fg="white").pack(pady=20)
    tk.Button(bloatware_window, text="Advanced Debloat+Stop Tracking", command=advanced_debloat, bg="#444", fg="white").pack(pady=20)
```

- **Purpose**: This is the main function for managing the bloatware uninstallation process. It first checks for administrative privileges, then displays a GUI window showing a list of installed bloatware apps with checkboxes. The user can select apps to uninstall and confirm the action. The function also integrates advanced debloating options.
- **Used For**: Providing a user-friendly interface to select and remove bloatware applications from the system.



# Features/clean/adv_bloat.py

This Python file provides the functionality to download and run an advanced script for debloating the system, specifically tailored for Windows 11. The script helps in removing unnecessary apps and disabling Microsoft tracking functionalities.

### **Imports**
```python
import requests
import zipfile
import tkinter.messagebox as messagebox
from Features.logging_func import log_error, log_command
import os
import subprocess
```

- **requests**: Used for downloading files from the internet.
- **zipfile**: Used for extracting the downloaded ZIP archive containing the debloat script.
- **tkinter.messagebox**: Provides functionality to show message boxes for success or error notifications.
- **log_error, log_command**: Imported for logging any errors or commands executed during the download and execution process (though not actively used in this file).
- **os**: Used for interacting with the file system, such as creating directories and checking for file existence.
- **subprocess**: Used to run the downloaded `.bat` script in the shell.

### **Helper Functions**

#### `download_and_extract_zip(url, extract_to='.')`
```python
def download_and_extract_zip(url, extract_to='.'):
    # Create the target path for the 'debloat' folder
    debloat_folder = os.path.join(extract_to, 'debloat')
    
    # Check if the 'debloat' folder exists, if not, create it
    if not os.path.exists(debloat_folder):
        os.makedirs(debloat_folder)

    # The name of the file being downloaded
    local_filename = os.path.join(debloat_folder, 'debloat.zip')
    
    try:
        # Download the file
        with requests.get(url, stream=True) as r:
            r.raise_for_status()  # Raise error if the download fails
            with open(local_filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
        
        # Unzip the file into the 'debloat' folder
        with zipfile.ZipFile(local_filename, 'r') as zip_ref:
            zip_ref.extractall(debloat_folder)
        
        # Remove the .zip archive after extraction
        os.remove(local_filename)
        
        # Path to the 'Start.bat' file in the 'Win11Debloat-master' subfolder
        run_bat_path = os.path.join(debloat_folder, 'Win11Debloat-master', 'Run.bat')
        
        # Check if the .bat file exists
        if not os.path.exists(run_bat_path):
            raise FileNotFoundError(f"{run_bat_path} was not found.")

        # Run the Start.bat file
        result = subprocess.run(f'"{run_bat_path}"', shell=True, capture_output=True, text=True)

        # Check if the script ran successfully
        if result.returncode != 0:
            raise RuntimeError(f"The script did not run successfully. Error: {result.stderr}")

        # Show success message
        messagebox.showinfo("Success", "The script was successfully downloaded and executed!")
    
    except Exception as e:
        # Show error message
        messagebox.showerror("Error", f"An error occurred: {e}")
```
- **Purpose**: This function downloads a ZIP file from the provided URL, extracts it into a folder named `debloat`, and then runs the `Run.bat` script contained in the extracted folder.
- **Used For**: Facilitating the downloading and extraction of the advanced debloating script, followed by its execution.

#### `advanced_debloat()`
```python
def advanced_debloat():
    response = messagebox.askyesno(
        "Advanced Debloat",
        ("This will download a script by Raphire that provides advanced debloating functions for your PC, "
         "including the ability to disable Microsoft tracking. "
         "You can run the script later by going to the debloat folder and executing the Run.bat file, "
         "which also allows you to undo any changes. Please be careful and do not modify the code if you "
         "are not familiar with it, as this could render the system unusable. I assume no liability. "
         "Do you want to download and run the script?")
    )
    
    if response:
        # If the user clicks Yes
        download_link = "https://codeload.github.com/Raphire/Win11Debloat/zip/refs/heads/master"  # Download link
        download_and_extract_zip(download_link, os.getcwd())
    else:
        # If the user clicks No, simply close the popup
        pass
```
- **Purpose**: This function presents a dialog box asking the user if they want to download and run the advanced debloating script. If the user accepts, the script is downloaded, extracted, and executed.
- **Used For**: Providing a user-friendly interface for initiating the advanced debloating process.

### **Main Execution Flow**
- When the **Advanced Debloat** button is clicked in the GUI, the `advanced_debloat()` function is triggered.
- The function first shows a confirmation message to ensure the user is aware of the potential consequences of running the script.
- If the user agrees, the `download_and_extract_zip()` function is called to download and execute the script.
- If there are any errors during the download, extraction, or script execution, error messages are displayed via a Tkinter message box.

### **Key Notes**
- **Security Warning**: The script being downloaded has powerful system modifications (including the ability to disable Microsoft tracking), so the user is warned to be cautious. It is also mentioned that the script can undo changes.
- **File System Interaction**: The script downloads and extracts files to the current working directory (`os.getcwd()`), which could be modified to another location if required.



# Features/clean/rm_dupe.py

This Python file provides the functionality to search for duplicate files in the user’s directories and allows the user to delete selected duplicates. It uses hashing to identify duplicates and provides a graphical user interface (GUI) to display and manage them.

### **Imports**
```python
import os
import hashlib
import tkinter as tk
import tkinter.messagebox as messagebox
from tkinter import messagebox, ttk, scrolledtext, Listbox, MULTIPLE, Toplevel
```

- **os**: Used for file system operations, such as reading directories and deleting files.
- **hashlib**: Provides functions to compute hashes of files (MD5 is used to identify duplicates).
- **tkinter**: The main module used to create the graphical user interface (GUI) for the application.
- **tkinter.messagebox**: Used for displaying message boxes (error, warning, success, etc.) to the user.
- **Listbox, MULTIPLE, Toplevel**: Used to create and manage listboxes with multiple selections and the sub-window for displaying duplicates.

### **Helper Functions**

#### `hash_file(file_path)`
```python
def hash_file(file_path):
    hasher = hashlib.md5()
    try:
        with open(file_path, 'rb') as f:
            buf = f.read()
            hasher.update(buf)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to read {file_path}: {str(e)}")
        return None
    return hasher.hexdigest()
```
- **Purpose**: Computes the MD5 hash of a file to uniquely identify it. This hash is used to check for duplicate files.
- **Error Handling**: If reading the file fails (e.g., due to permissions or corrupted files), an error message is displayed to the user.

#### `find_duplicates(directories)`
```python
def find_duplicates(directories):
    file_hashes = {}
    duplicates = []

    for directory in directories:
        if not os.path.exists(directory):  # Check if directory exists
            continue
        for foldername, _, filenames in os.walk(directory):
            for filename in filenames:
                file_path = os.path.join(foldername, filename)
                file_hash = hash_file(file_path)
                if file_hash is None:  # Skip if hashing failed
                    continue

                if file_hash in file_hashes:
                    duplicates.append((file_path, file_hashes[file_hash]))
                else:
                    file_hashes[file_hash] = file_path

    return duplicates
```
- **Purpose**: This function scans the provided directories and checks for duplicate files by comparing their MD5 hashes.
- **Logic**: It walks through each directory, hashes each file, and compares the hash with previously encountered hashes. If a duplicate hash is found, both file paths are recorded as duplicates.

#### `search_duplicates(duplicate_window, result_listbox, delete_btn)`
```python
def search_duplicates(duplicate_window, result_listbox, delete_btn):
    directories = [
        os.path.join(os.environ['USERPROFILE'], 'Desktop'),
        os.path.join(os.environ['USERPROFILE'], 'Documents'),
        os.path.join(os.environ['USERPROFILE'], 'Pictures'),
        os.path.join(os.environ['USERPROFILE'], 'Downloads') 
    ]
    
    duplicates = find_duplicates(directories)
    
    result_listbox.delete(0, tk.END)  # Clear previous results
    if duplicates:
        for pair in duplicates:
            result_listbox.insert(tk.END, f"{pair[0]} (Duplicate of {pair[1]})")
        delete_btn['state'] = 'normal'
    else:
        messagebox.showinfo("No Duplicates Found", "No duplicate files found.")
        delete_btn['state'] = 'disabled'
```
- **Purpose**: Searches for duplicates and displays the results in a listbox within the sub-window.
- **Details**: The function calls `find_duplicates` to get a list of duplicate files and their paths. It then updates the `result_listbox` to show these duplicates, enabling the delete button if duplicates are found. If no duplicates are found, a message box informs the user.

#### `delete_selected_files(duplicate_window, result_listbox)`
```python
def delete_selected_files(duplicate_window, result_listbox):
    selected_files = result_listbox.curselection()
    if not selected_files:
        messagebox.showwarning("No Selection", "Please select files to delete.")
        return

    confirmation = messagebox.askyesno("Delete Files", "Are you sure you want to delete the selected files?")
    if confirmation:
        success = True
        for index in selected_files[::-1]:  # Reverse the list to avoid index issues when deleting
            file_entry = result_listbox.get(index)
            file_path = file_entry.split(' (')[0]  # File path until first parenthesis
            try:
                os.remove(file_path)
                result_listbox.delete(index)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to delete {file_path}: {str(e)}")
                success = False
        
        if success:
            messagebox.showinfo("Success", "Selected files deleted successfully.")
        duplicate_window.destroy()  # Close the sub-window
```
- **Purpose**: Deletes the selected duplicate files.
- **Details**: First, it checks if any files are selected. If no files are selected, it warns the user. It then asks for confirmation before proceeding. Upon confirmation, it deletes the selected files and removes them from the list. If deletion fails, it shows an error message for each failed file. Once done, the sub-window is closed.

#### `rm_dupe(root)`
```python
def rm_dupe(root):
    duplicate_window = Toplevel(root)
    duplicate_window.title("Duplicate Finder")
    duplicate_window.configure(bg='#2c2f33')
    
    label = tk.Label(duplicate_window, text="Found duplicates. Select the files you want to delete:", 
                     bg='#2c2f33', fg='#ffffff')
    label.pack(pady=10)

    result_listbox = Listbox(duplicate_window, height=15, width=100, selectmode=MULTIPLE, bg='#23272a', fg='#ffffff')
    result_listbox.pack(pady=10)

    delete_btn = tk.Button(duplicate_window, text="Delete Selected Files", 
                           command=lambda: delete_selected_files(duplicate_window, result_listbox), 
                           bg='#ff5555', fg='#ffffff', state='disabled')
    delete_btn.pack(pady=10)

    search_duplicates(duplicate_window, result_listbox, delete_btn)
```
- **Purpose**: This function opens the sub-window for the duplicate file search and management interface.
- **Details**: It creates a new `Toplevel` window for displaying duplicates, including a label, listbox, and delete button. The listbox allows the user to select multiple duplicates for deletion. The delete button is initially disabled and only enabled when duplicates are found. It then calls `search_duplicates` to populate the listbox.

### **Main Execution Flow**
- When the **"Remove Duplicates"** button is clicked in the GUI, the `rm_dupe(root)` function is triggered.
- This opens a new sub-window where the user can see a list of duplicate files, select files to delete, and perform the deletion after confirmation.
- The program uses MD5 hashes to identify duplicate files, making the process efficient and reliable.

### **Key Features**
- **Directory Scanning**: The application scans several common user directories such as Desktop, Documents, Pictures, and Downloads for duplicates.
- **User Confirmation**: Before deleting any files, the user is prompted to confirm their action to avoid accidental deletions.
- **Error Handling**: The application displays appropriate messages if errors occur during file reading, hashing, or deletion.



# Features/clean/tiny_clean_features.py

This Python file provides a set of small disk cleanup tools that include cleaning the recycle bin, clearing virtual memory, and defragmenting the disk. These operations are accessible through a simple graphical user interface (GUI) that provides feedback to the user.

### **Imports**
```python
import platform
import ctypes
import tkinter as tk
from tkinter import messagebox  
from Features.command_handling import run_command, run_admin_command, run_window_admin_command
from Features.logging_func import log_command, log_error
```

- **platform**: This module is used to check the operating system type. The functions in this script are designed to work on Windows only.
- **ctypes**: Provides access to C-style function calls and allows calling Windows API functions to perform system operations like cleaning the recycle bin and managing virtual memory.
- **tkinter**: The GUI module used to create pop-up message boxes for user feedback.
- **run_command, run_admin_command, run_window_admin_command**: These functions from the `command_handling` module are likely used to execute system commands.
- **log_command, log_error**: These functions from the `logging_func` module handle logging of events and errors.

### **Functions**

#### `clean_recycle_bin()`
```python
def clean_recycle_bin():
    try:
        if platform.system() == "Windows":
            # Alternativer Ansatz zur Verwendung von ctypes
            ctypes.windll.shell32.SHEmptyRecycleBinW(None, None, 0x0007)
            messagebox.showinfo("Success", "Recycle Bin cleaned successfully.")
        else:
            messagebox.showwarning("Warning", "This operation is only supported on Windows.")
    except Exception as e:
        log_error("Failed to clean recycle bin", e)
        messagebox.showerror("Error", "An error occurred while cleaning the recycle bin.")
```
- **Purpose**: Cleans the Recycle Bin using the Windows API function `SHEmptyRecycleBinW`.
- **Windows Only**: The function first checks if the operating system is Windows using `platform.system()`. If it is, the function calls the Windows API using `ctypes.windll.shell32`.
- **Error Handling**: In case of an error (e.g., permission issues), the function logs the error and shows an error message to the user.

#### `clean_vs()`
```python
def clean_vs():
    try:
        if platform.system() == "Windows":
            # Setzt die Working Set-Größe des Prozesses, um den virtuellen Speicher zu bereinigen
            ctypes.windll.kernel32.SetProcessWorkingSetSize(-1, -1, -1)
            messagebox.showinfo("Success", "Virtual Storage cleaned successfully.")
        else:
            messagebox.showwarning("Warning", "This operation is only supported on Windows.")
    except Exception as e:
        log_error("Failed to clean virtual Storage", e)
        messagebox.showerror("Error", f"An error occurred while cleaning the virtual Storage: {str(e)}")
```
- **Purpose**: Clears the virtual storage (working set) for the process by calling `SetProcessWorkingSetSize` with `-1` values for minimum, current, and maximum working set sizes.
- **Windows Only**: This function is specific to Windows and requires a Windows system check.
- **Error Handling**: If an error occurs during the operation, it logs the error and informs the user through a message box.

#### `defragment()`
```python
def defragment():
    try:
        if platform.system() == "Windows":
            run_command("dfrgui.exe", "Defragmentation completed successfully.")
        else:
            messagebox.showwarning("Warning", "This operation is only supported on Windows.")
    except Exception as e:
        log_error("Failed to defragment", e)
        messagebox.showerror("Error", "An error occurred while defragmenting the disk.")
```
- **Purpose**: Starts the built-in Windows disk defragmentation tool `dfrgui.exe`.
- **Windows Only**: The function checks if the system is running Windows, and if true, it runs the defragmentation tool.
- **Error Handling**: Any issues during the operation, such as missing executables or permission errors, are logged, and the user is notified.

### **Overview of Features**
1. **Clean Recycle Bin**: Cleans the system's recycle bin by calling the appropriate Windows API function.
2. **Clear Virtual Storage**: Clears the virtual memory cache (working set) for the current process to free up memory.
3. **Defragment Disk**: Launches the disk defragmentation tool on Windows.

### **User Feedback**
- **Success**: After successful completion of each operation (Recycle Bin cleanup, virtual storage cleanup, and defragmentation), the user receives a success message via a `messagebox.showinfo` pop-up.
- **Warnings**: If the user is on a non-Windows system, the tool shows a warning message explaining that the operation is only supported on Windows.
- **Errors**: If any operation encounters an error (e.g., permission issues or missing files), an error message is shown to the user, and the error is logged.

### **Logging**
- Errors are logged using the `log_error` function, which helps in diagnosing issues during the cleanup process.

### **Key Features**
- **Windows-Specific Operations**: All three features (recycle bin cleanup, virtual storage cleanup, and defragmentation) are specific to Windows, making the script limited to this OS.
- **GUI Feedback**: The use of `tkinter.messagebox` ensures that users receive instant feedback about the success, failure, or warnings related to the operations.
- **Error Handling**: Every function includes error handling to manage potential failures gracefully, ensuring that the user is informed of any problems.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Features/info/pc_info.py

### **Imports**
```python
import psutil
import os
import platform
import socket
import time
import tkinter as tk
from tkinter import messagebox
import tkinter.messagebox as messagebox
```
- **psutil**: A library for retrieving information on system utilization (CPU, memory, disk, network, etc.).
- **os**: Provides a way to interact with the operating system, though it's not used directly in this script.
- **platform**: Provides system-specific parameters such as the OS name and version.
- **socket**: Used to fetch network-related information such as the hostname and IP address.
- **time**: Used for calculating system uptime based on boot time.
- **tkinter**: A GUI toolkit for Python, used here to display information in a message box.

### **Functions**

#### 1. **`get_pc_info()`**
```python
def get_pc_info():
    cpu_info = f"CPU: {psutil.cpu_count(logical=False)} cores ({psutil.cpu_count()} logical processors)\n"
    memory_info = f"Memory: {psutil.virtual_memory().total / (1024 ** 3):.2f} GB\n"
    available_memory_info = f"Available Memory: {psutil.virtual_memory().available / (1024 ** 3):.2f} GB\n"
    disk_info = f"Disk Usage: {psutil.disk_usage('/').total / (1024 ** 3):.2f} GB total\n"
    os_info = f"OS: {platform.system()} {platform.release()}\n"
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    network_info = f"Hostname: {hostname}\nIP Address: {ip_address}\n"
    boot_time = psutil.boot_time()
    uptime = time.time() - boot_time
    uptime_info = f"Uptime: {int(uptime // 3600)} hours, {int((uptime % 3600) // 60)} minutes\n"
    
    info = cpu_info + memory_info + available_memory_info + disk_info + os_info + network_info + uptime_info
    return info
```
- **CPU Information**: 
    - `psutil.cpu_count(logical=False)` returns the number of physical cores.
    - `psutil.cpu_count()` gives the number of logical processors (including hyper-threading).
- **Memory Information**:
    - `psutil.virtual_memory().total` gives the total installed RAM, converted to GB.
    - `psutil.virtual_memory().available` returns the available RAM, also converted to GB.
- **Disk Usage**: 
    - `psutil.disk_usage('/')` provides the total disk space on the root directory (`/`), converted to GB.
- **OS Information**:
    - `platform.system()` returns the OS name (e.g., "Windows", "Linux").
    - `platform.release()` gives the OS release version (e.g., "10" for Windows 10).
- **Network Information**:
    - `socket.gethostname()` retrieves the local machine's hostname.
    - `socket.gethostbyname(hostname)` returns the machine's IP address.
- **Uptime**:
    - `psutil.boot_time()` retrieves the system's boot time in seconds since the epoch.
    - The uptime is calculated as the difference between the current time and the boot time, then converted to hours and minutes.

The function then returns a formatted string containing all this information.

#### 2. **`show_pc_info()`**
```python
def show_pc_info():
    info = get_pc_info()
    messagebox.showinfo("PC Information", info)
```
- **Purpose**: This function retrieves the system information by calling `get_pc_info()` and then displays it using `messagebox.showinfo()`, which shows a pop-up with the information.
- **Usage**: When the user invokes `show_pc_info()`, a message box will pop up containing the PC details, allowing them to quickly view important system metrics.

---

### **Functionality Overview**

- **System Information**: The script collects the following information about the system:
  - CPU: Number of physical cores and logical processors.
  - Memory: Total and available system memory (RAM).
  - Disk Usage: Total disk space available on the root directory.
  - Operating System: The OS name and release version.
  - Network: Hostname and IP address of the machine.
  - Uptime: Time since the system was last booted.
  
- **GUI**: The system information is presented to the user in a pop-up message box via `tkinter`.

### **Error Handling**:
- The script does not include explicit error handling in the functions. However, since it uses `psutil` and `socket`, which are reliable libraries, it is assumed that the functions will work correctly if the system is running as expected. If needed, error handling could be added to manage cases like network failures or missing modules.

### **Use Case**:
This script is helpful for users who want to quickly gather key information about their computer system, such as:
- **System diagnostics**: Checking memory, CPU, disk, and network details.
- **Uptime**: Determining how long the system has been running without rebooting.
  
This could be integrated into a larger system maintenance or monitoring tool, or simply used as a standalone utility.

### **How It Works**:
- Once the `show_pc_info()` function is called, it triggers the retrieval of system information by the `get_pc_info()` function and presents that information to the user in a message box.

--- 

### **Example Output in Message Box**
If you were to run the script, the user would see a message box with information similar to this:

```
PC Information
-------------------------------
CPU: 4 cores (8 logical processors)
Memory: 16.00 GB
Available Memory: 8.50 GB
Disk Usage: 500.00 GB total
OS: Windows 10
Hostname: DESKTOP-1234
IP Address: 192.168.1.5
Uptime: 12 hours, 34 minutes
```



# Features/info/connection.py

### **Imports**
```python
from Features.logging_func import log_command, log_error
import socket
import tkinter as tk
import requests
import subprocess
import chardet  # Ensure you import chardet
```
- **log_command, log_error**: Functions to log command execution and errors, respectively (from `logging_func.py`).
- **socket**: Used to get the local machine's IP address and network hostname.
- **requests**: A library for making HTTP requests, here used to fetch ISP details from an online API (`ipinfo.io`).
- **subprocess**: Used to run shell commands, specifically for gathering network information (e.g., signal strength).
- **chardet**: A character encoding detector that ensures the correct encoding is applied when handling subprocess output.

### **Functions**

#### 1. **`run_command_nomsg(command)`**
```python
def run_command_nomsg(command):
    try:
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        stdout, stderr = process.communicate()

        # Erkennen der Kodierung
        result_encoding = chardet.detect(stdout)['encoding']
        if result_encoding is None:
            result_encoding = 'utf-8'  # Fallback auf eine Standardkodierung

        # Log the output (whether it's success or error)
        if process.returncode == 0:
            decoded_output = stdout.decode(result_encoding, errors='ignore')
            log_command(command, decoded_output)
            return decoded_output  # Return the output so it can be processed by the caller
        else:
            decoded_error = stderr.decode(result_encoding, errors='ignore')
            log_command(command, decoded_error)
            raise subprocess.CalledProcessError(process.returncode, command, output=stderr)

    except Exception as e:
        log_error(f"Error running command: {command}", e)
        raise  # Re-raise the exception to be handled by the caller
```
- **Purpose**: This function runs a shell command and captures its output and errors.
- **Details**:
  - Runs the command via `subprocess.Popen()`.
  - Detects the encoding of the output using `chardet`.
  - Logs both standard output and error messages.
  - Returns the decoded standard output if successful, or raises an error with the decoded error message if the command fails.

#### 2. **`get_network_name()`**
```python
def get_network_name():
    try:
        result = subprocess.run(['powershell', '-Command', 'Get-NetConnectionProfile | Select-Object -ExpandProperty Name'], capture_output=True, text=True)
        network_name = result.stdout.strip()
        return network_name if network_name else "Not connected"
    except Exception as e:
        log_error("Failed to retrieve network name", e)
        return "Not connected"
```
- **Purpose**: This function retrieves the name of the current network connection using a PowerShell command (`Get-NetConnectionProfile`).
- **Details**:
  - Runs the PowerShell command to get the network profile's name.
  - If successful, returns the network name; if not, returns `"Not connected"`.

#### 3. **`get_provider_info()`**
```python
def get_provider_info():
    try:
        response = requests.get('https://ipinfo.io')
        data = response.json()
        return data.get('org', 'Unknown')  # ISP (Internet Service Provider) from the data
    except:
        return "Unknown"
```
- **Purpose**: This function fetches ISP information using the `ipinfo.io` API, which provides details about the IP address, including the organization (ISP).
- **Details**:
  - Makes a GET request to `ipinfo.io` to fetch the data.
  - If the request is successful, it returns the ISP name; if not, it returns `"Unknown"`.

#### 4. **`get_signal_strength()`**
```python
def get_signal_strength():
    try:
        result = run_command_nomsg(["netsh", "wlan", "show", "interfaces"])
        # Split the result into lines and search for the "Signal" line
        for line in result.splitlines():
            if "Signal" in line:
                # Extract and return the signal strength value, assuming it's in percentage
                signal_strength = line.split(":")[1].strip()
                return f"Signal Strength: {signal_strength}"
        return "Signal Strength: Unknown"
    except Exception as e:
        return f"Failed to retrieve signal strength: {e}"
```
- **Purpose**: This function retrieves the Wi-Fi signal strength using the `netsh` command (Windows only).
- **Details**:
  - Runs the `netsh wlan show interfaces` command to gather information about the Wi-Fi connection.
  - Searches for the "Signal" line in the command output and extracts the signal strength (assumed to be in percentage).
  - If the signal strength cannot be determined, it returns `"Signal Strength: Unknown"`.

#### 5. **`get_connection_info()`**
```python
def get_connection_info():
    try:
        ip_address = socket.gethostbyname(socket.gethostname())
        network_name = get_network_name()
        signal_strength = get_signal_strength()
        provider = get_provider_info()  # Get provider info from API
        return f"IP Address: {ip_address}\nNetwork Name: {network_name}\nSignal Strength: {signal_strength}\nProvider: {provider}"
    except Exception as e:
        return f"Failed to retrieve connection info: {e}"
```
- **Purpose**: This function gathers comprehensive connection information, including IP address, network name, signal strength, and ISP details.
- **Details**:
  - Retrieves the IP address using `socket.gethostbyname()`.
  - Calls the previously defined functions to gather the network name, signal strength, and ISP.
  - Returns a formatted string with all the gathered information.

#### 6. **`show_connection_info(root)`**
```python
def show_connection_info(root):
    info = get_connection_info()

    # Create a new window for connection information
    info_window = tk.Toplevel(root)
    info_window.title("Connection Information")
    info_window.geometry("400x300")
    info_window.configure(bg="black")  # Set the background color to black for dark mode
    
    # Create a Text widget to display the connection info
    text = tk.Text(info_window, bg="black", fg="white", font=("Helvetica", 12))
    text.insert(tk.END, info)
    text.config(state=tk.DISABLED)
    text.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)
```
- **Purpose**: This function opens a new window displaying the connection information.
- **Details**:
  - Retrieves connection info using `get_connection_info()`.
  - Creates a new `Toplevel` window with dark mode styling (black background and white text).
  - Displays the connection information in a `Text` widget, making the window visually appealing and easy to read.
  - The `Text` widget is set to `DISABLED` to make it read-only.

---

### **Functionality Overview**

- **Network Information**: The script retrieves a variety of network-related information, such as:
  - **IP Address**: The local IP address of the machine.
  - **Network Name**: The name of the network the machine is connected to.
  - **Signal Strength**: The signal strength of the Wi-Fi connection.
  - **ISP Information**: The ISP (Internet Service Provider) based on the external IP address.

- **Error Handling**: Each function includes error handling with logging. If any operation fails (e.g., command execution, network request), an error message is returned or logged.

- **GUI**: The network information is displayed in a new window using `tkinter`, making the script suitable for interactive use.

### **Example Output**
The user would see a window with information like:

```
IP Address: 192.168.1.5
Network Name: HomeNetwork
Signal Strength: 80%
Provider: Comcast
```

This part of the Code is useful for users who want to quickly check their network connection details, including troubleshooting network-related issues.



# Features/info/internet_speedtest.py

### **Imports**
```python
from speedtest import Speedtest, ConfigRetrievalError
import tkinter as tk
import tkinter.messagebox as messagebox
from tkinter import Toplevel
from Features.logging_func import log_error
```
- **`Speedtest`**: This is the main class from the `speedtest-cli` package, which is used to conduct the internet speed test.
- **`ConfigRetrievalError`**: This exception is raised if there is an issue retrieving the server configuration for the speed test.
- **`tkinter`**: The standard Python library for creating graphical user interfaces (GUIs).
- **`log_error`**: A custom logging function from the `logging_func.py` file to log errors when something goes wrong during the speed test.

### **Functions**

#### 1. **`get_internet_speed(root)`**
```python
def get_internet_speed(root):
    try:
        st = Speedtest()
        st.get_best_server()
        download_speed = st.download() / 1_000_000  # Mbps
        upload_speed = st.upload() / 1_000_000      # Mbps
        ping = st.results.ping
        return download_speed, upload_speed, ping
    except ConfigRetrievalError as e:
        log_error("Failed to retrieve speedtest configuration", e)
        messagebox.showerror("Speedtest Error", "Failed to retrieve speedtest configuration. Please check the log file for details.")
        return 0, 0, 0
```
- **Purpose**: This function performs the internet speed test.
- **Steps**:
  - A `Speedtest` object is created to interact with the speedtest server.
  - The best server for the speed test is selected using `get_best_server()`.
  - The **download speed** is retrieved in bits per second and then converted to megabits per second (Mbps).
  - The **upload speed** is retrieved in a similar manner.
  - The **ping** is retrieved from the `results` object, which gives the round-trip time to the server in milliseconds (ms).
- **Error Handling**:
  - If there's an issue retrieving the server configuration (e.g., network problems), a `ConfigRetrievalError` exception is caught.
  - The error is logged using the `log_error()` function, and an error message is displayed in a `messagebox`.

- **Returns**: The function returns the download speed, upload speed, and ping values (in Mbps and ms). If an error occurs, it returns `(0, 0, 0)`.

#### 2. **`open_speedtest_window(root)`**
```python
def open_speedtest_window(root):
    download_speed, upload_speed, ping = get_internet_speed(root)
    result = f"Download Speed: {download_speed:.2f} Mbps\nUpload Speed: {upload_speed:.2f} Mbps\nPing: {ping} ms"
    
    # Create new window for result
    info_window = Toplevel(root)
    info_window.title("Speedtest Result")
    info_window.geometry("400x200")
    info_window.configure(bg="black")  # Dark mode background for result window
    
    # Create Text widget to show results
    text = tk.Text(info_window, bg="black", fg="white", font=("Helvetica", 12))
    text.insert(tk.END, result)
    text.config(state=tk.DISABLED)
    text.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)
```
- **Purpose**: This function creates a new window that displays the results of the internet speed test.
- **Steps**:
  - Calls `get_internet_speed()` to fetch the internet speed test results (download speed, upload speed, and ping).
  - Formats the results into a string to be displayed in the new window.
  - A new `Toplevel` window is created for displaying the results.
  - The window is styled with a black background (`bg="black"`) for dark mode.
  - A `Text` widget is used to display the results in the new window. The text is set to white to contrast with the black background, and the text widget is configured to be read-only (`state=tk.DISABLED`).
  - The results are inserted into the `Text` widget and displayed in the window.

### **Example Output**
After running the speed test, the user will see a window like this:
```
Download Speed: 45.62 Mbps
Upload Speed: 5.14 Mbps
Ping: 32 ms
```

This window displays the results of the speed test in a user-friendly format, with the speeds in Mbps and the ping in ms.

### **Error Handling**
- If there's an issue during the speed test (such as a network error or configuration retrieval issue), the error is logged and a `messagebox` is shown to the user with an appropriate error message.
  

### **How it Works**
1. When the user triggers the speed test (presumably through a button or menu option in the GUI), the `open_speedtest_window(root)` function is called.
2. The speed test is conducted via the `Speedtest` class, which measures download speed, upload speed, and ping.
3. The results are formatted and displayed in a new window with a dark theme.
4. If an error occurs (e.g., if the configuration cannot be retrieved), an error message is shown.

### **Use Case**
This script can be part of a system utility tool where users want to quickly check their internet connection's speed. It could be useful for troubleshooting network issues, testing the performance of different network providers, or simply checking the speed of the current internet connection. The results are presented in an easy-to-understand format within a GUI, making it user-friendly.

### **GUI Design Considerations**
- The dark mode styling (black background and white text) is likely intended for users who prefer a darker UI theme, which is commonly seen in many modern applications.
- The use of a `Text` widget makes the results easily readable and scalable for future updates (e.g., if additional information needs to be displayed).
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

***I hope this helped you to understand my Code :)***

