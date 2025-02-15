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

def create_buttons(root, show_main_menu, show_info_menu, show_clean_menu, show_update_menu, show_repair_menu):
    # Gemeinsamer Button-Stil
    button_style = {
        "bg": "#444",
        "fg": "white",
        "activebackground": "#555",
        "activeforeground": "white",
        "borderwidth": 1,
        "relief": "raised"
    }

    # Alle Buttons erstellen
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
        "update_apps_button": tk.Button(root, text="Update Apps", command=lambda: run_window_admin_command("title Updater && winget source update && cls && winget upgrade --all --include-unknown --accept-package-agreements --accept-source-agreements --force --disable-interactivity --wait", "Winget initiated successfully.", root), **button_style),
        "windows_update_button": tk.Button(root, text="Windows Update", command=lambda: run_command("wuauclt /detectnow /updatenow", "Windows update initiated successfully."), **button_style),
        "repair_connection_button": tk.Button(root, text="Repair Connection", command=lambda: run_admin_command("ipconfig /flushdns && netsh winsock reset && ipconfig /release && ipconfig /renew", "Successfully reset Network and tried to fix Connection Problems.", root), **button_style),
        "driver_update_button": tk.Button(root, text="Driver Update", command=lambda: run_command("wuauclt /detectnow /updatenow", "Drivers updated successfully."), **button_style),
        "back_button": tk.Button(root, text="Back", command=show_main_menu, **button_style),
        "help_button": tk.Button(root, text="Help", command=lambda: print("Show Help (Placeholder)"), **button_style),
        "rm_bloatware_button": tk.Button(root, text="Remove Bloatware", command=lambda: rm_Bloatware(root), **button_style),
        "clean_startup_button": tk.Button(root, text="Clean Startup", command=lambda: clean_startup(root), **button_style)
    }
    return buttons
