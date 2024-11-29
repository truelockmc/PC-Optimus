import platform
import ctypes
import tkinter as tk
from tkinter import messagebox  
from Features.command_handling import run_command, run_admin_command, run_window_admin_command
from Features.logging_func import log_command, log_error


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

def defragment():
    try:
        if platform.system() == "Windows":
            run_command("dfrgui.exe", "Defragmentation completed successfully.")
        else:
            messagebox.showwarning("Warning", "This operation is only supported on Windows.")
    except Exception as e:
        log_error("Failed to defragment", e)
        messagebox.showerror("Error", "An error occurred while defragmenting the disk.")