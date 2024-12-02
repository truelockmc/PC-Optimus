import subprocess
import platform
from Features.logging_func import log_command, log_error
import chardet
import platform
import tkinter as tk
from tkinter import messagebox  
from Features.admin_elevate import is_admin, elevate

def run_command(command, success_message):
    try:
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        stdout, stderr = process.communicate()
        
        # Erkennen der Kodierung
        result_encoding = chardet.detect(stdout)['encoding']
        if result_encoding is None:
            result_encoding = 'utf-8'  # Fallback auf eine Standardkodierung
        
        if process.returncode == 0:
            log_command(command, stdout.decode(result_encoding, errors='ignore'))
            messagebox.showinfo("Success", success_message)
        else:
            log_command(command, stderr.decode(result_encoding, errors='ignore'))
            raise subprocess.CalledProcessError(process.returncode, command, output=stderr)
    except Exception as e:
        log_error(f"Error running command: {command}", e)
        messagebox.showerror("Error", "An error occurred. Please check the log file for details.")
     
# Funktion, um einen Befehl als Administrator auszuführen und das Fenster zu verbergen
def run_admin_command(command, success_message, show_window=False):
    try:
        if platform.system() == "Windows":
            if is_admin():
                # Befehl direkt ausführen, da der Benutzer Adminrechte hat
                creationflags = subprocess.CREATE_NO_WINDOW if not show_window else 0
                result = subprocess.run(command, shell=True, creationflags=creationflags)
                if result.returncode == 0 or result.returncode == 3:  # Ignoriere exit code 3
                    messagebox.showinfo("Success", success_message)
                else:
                    messagebox.showerror("Error", f"Command failed with return code {result.returncode}")
            else:
                # Skript als Administrator neu starten
                messagebox.showinfo("Info", "This action requires administrator privileges. The program will restart with elevated rights.")
                elevate(root)
                root.quit()  # Altes Fenster schließen
                os._exit(0)  # Sofort das alte Fenster beenden
        else:
            # Für andere Betriebssysteme: Befehl normal ausführen
            result = subprocess.run(command, shell=True)
            if result.returncode == 0 or result.returncode == 3:  # Ignoriere exit code 3
                messagebox.showinfo("Success", success_message)
            else:
                messagebox.showerror("Error", f"Command failed with return code {result.returncode}")
    except Exception as e:
        # Fehlerprotokollierung und Anzeige
        log_error(f"Error running admin command: {command}", e)
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def run_window_admin_command(command, success_message):
    global root  # Zugriff auf die globale Variable root
    try:
        if platform.system() == "Windows":
            if is_admin():
                # Befehl in einem neuen CMD-Fenster ausführen
                full_command = f'start cmd /k "{command}"'
                result = subprocess.run(full_command, shell=True)
                if result.returncode == 0 or result.returncode == 3:  # Ignoriere exit code 3
                    messagebox.showinfo("Success", success_message)
                else:
                    messagebox.showerror("Error", f"Command failed with return code {result.returncode}")
            else:
                # Skript als Administrator neu starten
                messagebox.showinfo("Info", "This action requires administrator privileges. The program will restart with elevated rights.")
                elevate(root)
                if root is not None:
                    root.quit()
                os._exit(0)  # Beendet den Prozess
        else:
            # Für andere Betriebssysteme: Befehl normal ausführen
            result = subprocess.run(command, shell=True)
            if result.returncode == 0 or result.returncode == 3:  # Ignoriere exit code 3
                messagebox.showinfo("Success", success_message)
            else:
                messagebox.showerror("Error", f"Command failed with return code {result.returncode}")
    except Exception as e:
        # Fehlerprotokollierung und Anzeige
        log_error(f"Error running admin command: {command}", e)
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
