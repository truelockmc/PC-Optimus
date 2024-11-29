from tkinter import messagebox, ttk, scrolledtext, Listbox, Toplevel
import psutil
import tkinter as tk
import tkinter.messagebox as messagebox
import threading
import subprocess
import os
from Features.shortcut import create_shortcut
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

def show_info_menu():
    clear_frame()
    systeminfo_button.pack(pady=10)
    advanced_systeminfo_button.pack(pady=10)
    resource_monitoring_button.pack(pady=10)
    speedtest_button.pack(pady=10)
    connection_button.pack(pady=10)
    back_button.pack(pady=10)

def show_clean_menu():
    clear_frame()
    rm_bloatware_button.pack(pady=10)
    rm_dupe_button.pack(pady=10)
    clean_mngr_button.pack(pady=10)
    clean_startup_button.pack(pady=10)
    wsreset_button.pack(pady=10)
    disk_cleanup_button.pack(pady=10)
    temp_cleanup_button.pack(pady=10)
    prefetch_clean_button.pack(pady=10)
    clean_invis_button.pack(pady=10)
    defragment_button.pack(pady=10)
    clean_vs_button.pack(pady=10)
    Empty_RecycleBin_button.pack(pady=10)
    back_button.pack(pady=10)

def show_update_menu():
    clear_frame()
    update_apps_button.pack(pady=10)
    windows_update_button.pack(pady=10)
    driver_update_button.pack(pady=10)
    back_button.pack(pady=10)

def show_repair_menu():
    clear_frame()
    health_scan_button.pack(pady=10)
    storage_diagonistics_button.pack(pady=10)
    repair_file_system_button.pack(pady=10)
    repair_connection_button.pack(pady=10)
    back_button.pack(pady=10)


def show_main_menu():
    clear_frame()
    info_button.pack(pady=10)
    clean_button.pack(pady=10)
    update_button.pack(pady=10)
    repair_button.pack(pady=10)
    help_button.pack(pady=10)

def clear_frame():
    for widget in root.winfo_children():
        widget.pack_forget()

# Creating the GUI
root = tk.Tk()
root.title("PC Optimus")
root.geometry("400x600")
root.configure(bg="#2E2E2E")

repair_file_system_button = tk.Button(root, text="Repair Filesystem", command=lambda: run_admin_command("echo J | chkdsk /f", "Successfully initiated chkdsk, your File System will be checked on the next startup."), bg="#444", fg="white", activebackground="#555", activeforeground="white", borderwidth=1, relief="raised")

clean_vs_button = tk.Button(root, text="Clean Virtual Storage", command=clean_vs, bg="#444", fg="white", activebackground="#555", activeforeground="white", borderwidth=1, relief="raised")

rm_dupe_button = tk.Button(root, text="Remove File Duplicates", command=lambda: rm_dupe(root), bg="#444", fg="white", activebackground="#555", activeforeground="white", borderwidth=1, relief="raised")

info_button = tk.Button(root, text="Info", command=show_info_menu, bg="#444", fg="white", activebackground="#555", activeforeground="white", borderwidth=1, relief="raised")

repair_button = tk.Button(root, text="Repair", command=show_repair_menu, bg="#444", fg="white", activebackground="#555", activeforeground="white", borderwidth=1, relief="raised")

systeminfo_button = tk.Button(root, text="Systeminfo", command=show_pc_info, bg="#444", fg="white", activebackground="#555", activeforeground="white", borderwidth=1, relief="raised")

advanced_systeminfo_button = tk.Button(root, text="Advanced Systeminfo", command=lambda: run_command("msinfo32.exe", "Successfully Retrieved Advanced Systeminfo."), bg="#444", fg="white", activebackground="#555", activeforeground="white", borderwidth=1, relief="raised")

resource_monitoring_button = tk.Button(root, text="Resource Monitoring", command=lambda: run_command("perfmon.exe /res", "Successfully ran Windows Resource Monitoring."), bg="#444", fg="white", activebackground="#555", activeforeground="white", borderwidth=1, relief="raised")

speedtest_button = tk.Button(root, text="Internet Speed", command=lambda: open_speedtest_window(root), bg="#444", fg="white", activebackground="#555", activeforeground="white", borderwidth=1, relief="raised")

connection_button = tk.Button(root, text="Connection", command=lambda: show_connection_info(root), bg="#444", fg="white", activebackground="#555", activeforeground="white", borderwidth=1, relief="raised")

health_scan_button = tk.Button(root, text="Repair System Files", command=lambda: run_window_admin_command("title Health Scan && cls && sfc /scannow && DISM /Online /Cleanup-Image /RestoreHealth && pause ", "Successfully startet Scanning for Erros in System and Image Files, please keep the New Terminal Window open to let the Process complete."), bg="#444", fg="white", activebackground="#555", activeforeground="white", borderwidth=1, relief="raised")

clean_button = tk.Button(root, text="Clean", command=show_clean_menu, bg="#444", fg="white", activebackground="#555", activeforeground="white", borderwidth=1, relief="raised")

clean_mngr_button = tk.Button(root, text="Clean Manager", command=lambda: run_command("cleanmgr", "Disk cleanup completed successfully."), bg="#444", fg="white", activebackground="#555", activeforeground="white", borderwidth=1, relief="raised")

wsreset_button = tk.Button(root, text="WSReset", command=lambda: run_command("wsreset.exe", "Microsoft Store reset completed successfully."), bg="#444", fg="white", activebackground="#555", activeforeground="white", borderwidth=1, relief="raised")

disk_cleanup_button = tk.Button(root, text="Disk Cleanup", command=lambda: run_command("cleanmgr /sagerun:1", "Advanced Disk Cleanup completed successfully."), bg="#444", fg="white", activebackground="#555", activeforeground="white", borderwidth=1, relief="raised")

temp_cleanup_button = tk.Button(root, text="Temp Cleanup", command=lambda: run_command(r"del /q/f/s %TEMP%\*", "Successfully deleted Temporary Files."), bg="#444", fg="white", activebackground="#555", activeforeground="white", borderwidth=1, relief="raised")

prefetch_clean_button = tk.Button(root, text="Prefetch Cleanup", command=lambda: run_command(r"del /q/s C:\Windows\prefetch\*", "Successfully cleaned up Prefetch Files."), bg="#444", fg="white", activebackground="#555", activeforeground="white", borderwidth=1, relief="raised")

clean_invis_button = tk.Button(root, text="Clean Invis", command=lambda: run_window_admin_command(r"cipher /w:c && msg * Successfully Cleaned invisible Space Consuming Files && exit", "Successfully ran Windows Cipher, please be patient, the process will take a while."), bg="#444", fg="white", activebackground="#555", activeforeground="white", borderwidth=1, relief="raised")

Empty_RecycleBin_button = tk.Button(root, text="Empty Recycle Bin", command=clean_recycle_bin, bg="#444", fg="white", activebackground="#555", activeforeground="white", borderwidth=1, relief="raised")

defragment_button = tk.Button(root, text="Defragment", command=defragment, bg="#444", fg="white", activebackground="#555", activeforeground="white", borderwidth=1, relief="raised")

storage_diagonistics_button = tk.Button(root, text="Storage Diagnostics", command=lambda: run_command("MdSched.exe", "Successfully ran Windows Storage Diagnostics."), bg="#444", fg="white", activebackground="#555", activeforeground="white", borderwidth=1, relief="raised")

update_button = tk.Button(root, text="Update", command=show_update_menu, bg="#444", fg="white", activebackground="#555", activeforeground="white", borderwidth=1, relief="raised")
update_button.pack(pady=10)

update_apps_button = tk.Button(root, text="Update Apps", command=lambda: run_window_admin_command("title Updater && color a && cls && winget source reset --force && winget source update && winget upgrade --all --include-unknown --accept-package-agreements --accept-source-agreements --force --uninstall-previous --disable-interactivity --wait ", "Winget initiated successfully."), bg="#444", fg="white", activebackground="#555", activeforeground="white", borderwidth=1, relief="raised")

windows_update_button = tk.Button(root, text="Windows Update", command=lambda: run_command("wuauclt /detectnow /updatenow", "Windows update initiated successfully."), bg="#444", fg="white", activebackground="#555", activeforeground="white", borderwidth=1, relief="raised")

repair_connection_button = tk.Button(root, text="Repair Connection", command=lambda: run_admin_command("ipconfig /flushdns && netsh winsock reset && ipconfig /release && ipconfig /renew && netsh interface ip reset && netsh interface ipv4 reset && netsh interface ipv6 reset && route reset && netsh winsock reset catalog ", "Successfully ressettet Network and tried to fixx Connection Problems, restart your PC to complete the Process"), bg="#444", fg="white", activebackground="#555", activeforeground="white", borderwidth=1, relief="raised")

driver_update_button = tk.Button(root, text="Driver Update", command=lambda: run_command("wuauclt /detectnow /updatenow", "Drivers updated successfully."), bg="#444", fg="white", activebackground="#555", activeforeground="white", borderwidth=1, relief="raised")

back_button = tk.Button(root, text="Back", command=show_main_menu, bg="#444", fg="white", activebackground="#555", activeforeground="white", borderwidth=1, relief="raised")

help_button = tk.Button(root, text="Help", command=show_help, bg="#444", fg="white", activebackground="#555", activeforeground="white", borderwidth=1, relief="raised")

rm_bloatware_button = tk.Button(root, text="Remove Bloatware", command=lambda: rm_Bloatware(root), bg="#444", fg="white", activebackground="#555", activeforeground="white", borderwidth=1, relief="raised")

clean_startup_button = tk.Button(root, text="Clean Startup", command=lambda: clean_startup(root), bg="#444", fg="white", activebackground="#555", activeforeground="white", borderwidth=1, relief="raised")

create_shortcut()

show_main_menu()

root.mainloop()