import psutil
import tkinter as tk
from tkinter import messagebox
from speedtest import Speedtest, ConfigRetrievalError
from PIL import Image, ImageTk
import tkinter.messagebox as messagebox
import threading
import platform
import socket
import time
import subprocess
import webbrowser
import os
import re
import chardet
import tempfile
import ctypes

# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))

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

def defragment():
    try:
        if platform.system() == "Windows":
            run_command("dfrgui.exe", "Defragmentation completed successfully.")
        else:
            messagebox.showwarning("Warning", "This operation is only supported on Windows.")
    except Exception as e:
        log_error("Failed to defragment", e)
        messagebox.showerror("Error", "An error occurred while defragmenting the disk.")
        
def update_apps():
    # Batch-Befehle
    commands = [
        "title Updater",
        "color a",
        "winget source reset --force",  # Quellen zurücksetzen
        "winget source update",  # Quellen aktualisieren
        "winget upgrade --all --include-unknown --accept-package-agreements --accept-source-agreements --force --uninstall-previous --disable-interactivity --wait",
        "pause"
    ]
    
    # Temporäre Batch-Datei erstellen
    with tempfile.NamedTemporaryFile(delete=False, suffix=".bat", mode='w', encoding='utf-8') as batch_file:
        for command in commands:
            batch_file.write(command + "\n")
        batch_file_path = batch_file.name

    # PowerShell-Skript, um die Batch-Datei mit Adminrechten auszuführen
    powershell_script = f'''
    $batch_file = "{batch_file_path}"
    Start-Process -FilePath "cmd.exe" -ArgumentList "/c `" $batch_file `"" -Verb runAs
    '''
    
    # Temporäre PowerShell-Datei erstellen
    with tempfile.NamedTemporaryFile(delete=False, suffix=".ps1", mode='w', encoding='utf-8') as ps_file:
        ps_file.write(powershell_script)
        ps_file_path = ps_file.name

    # PowerShell-Skript ausführen
    subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", ps_file_path], check=True)

    # Temporäre Dateien löschen
    os.remove(ps_file_path)
    # Die Batch-Datei wird nicht sofort gelöscht, damit das Fenster offen bleibt
    print(f"Die Batch-Datei befindet sich unter: {batch_file_path}")

    
    # Function to check internet speed
def get_internet_speed():
    try:
        st = Speedtest()
        st.get_best_server()
        download_speed = st.download() / 1_000_000
        upload_speed = st.upload() / 1_000_000
        ping = st.results.ping
        return download_speed, upload_speed, ping
    except ConfigRetrievalError as e:
        log_error("Failed to retrieve speedtest configuration", e)
        messagebox.showerror("Speedtest Error", "Failed to retrieve speedtest configuration. Please check the log file for details.")
        return 0, 0, 0

# Function to check system status
def get_system_status():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    total_memory = memory.total / (1024 ** 3)
    available_memory = memory.available / (1024 ** 3)
    return cpu_usage, total_memory, available_memory

# Function to retrieve PC info
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

# Function to retrieve network name
def get_network_name():
    try:
        result = subprocess.run(['powershell', '-Command', 'Get-NetConnectionProfile | Select-Object -ExpandProperty Name'], capture_output=True, text=True)
        network_name = result.stdout.strip()
        return network_name if network_name else "Not connected"
    except Exception as e:
        log_error("Failed to retrieve network name", e)
        return "Not connected"

# Function to retrieve connection information
def get_connection_info():
    try:
        ip_address = socket.gethostbyname(socket.gethostname())
        network_name = get_network_name()
        signal_strength = "Unknown"  # Signal strength is not easily retrievable in Windows
        provider = "Unknown"  # Provider is not easily retrievable without third-party tools
        return f"IP Address: {ip_address}\nNetwork Name: {network_name}\nSignal Strength: {signal_strength}\nProvider: {provider}"
    except Exception as e:
        log_error("Failed to retrieve connection info", e)
        return "Failed to retrieve connection information."

# Function to show speedtest result
def show_speedtest_result():
    download_speed, upload_speed, ping = get_internet_speed()
    result = f"Download Speed: {download_speed:.2f} Mbps\nUpload Speed: {upload_speed:.2f} Mbps\nPing: {ping} ms"
    info_window = tk.Toplevel(root)
    info_window.title("Speedtest Result")
    info_window.geometry("400x200")
    text = tk.Text(info_window)
    text.insert(tk.END, result)
    text.config(state=tk.DISABLED)
    text.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

# Function to show connection info
def show_connection_info():
    info = get_connection_info()
    info_window = tk.Toplevel(root)
    info_window.title("Connection Information")
    info_window.geometry("400x300")
    text = tk.Text(info_window)
    text.insert(tk.END, info)
    text.config(state=tk.DISABLED)
    text.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

def show_pc_info():
    info = get_pc_info()
    messagebox.showinfo("PC Information", info)

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

def run_admin_command(command, success_message):
    try:
        # Check if the OS is Windows
        if platform.system() == "Windows":
            # Execute command with admin privileges
            process = subprocess.Popen(['runas', '/user:Administrator', f'{command}'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            stdout, stderr = process.communicate()
            
            # Erkennen der Kodierung
            result_encoding = chardet.detect(stdout)['encoding']
            if result_encoding is None:
                result_encoding = 'utf-8'  # Fallback auf eine Standardkodierung
            
            if process.returncode == 0:
                log_command(command, stdout.decode(result_encoding, errors='ignore'))
                messagebox.showinfo("Success", success_message)
            else:
                raise subprocess.CalledProcessError(process.returncode, command, output=stderr)
        else:
            run_command(command, success_message)
    except Exception as e:
        log_error(f"Error running admin command: {command}", e)
        messagebox.showerror("Error", "An error occurred. Please check the log file for details.")
        
def health_scan():
    # Batch-Befehle
    commands = [
        "title Health Scan",
        "msg * This Tool Scans for System Errors and fixxes them",
        "clear",
        "sfc /scannow",
        "DISM /Online /Cleanup-Image /RestoreHealth",
        "pause"
    ]
    
    # Temporäre Batch-Datei erstellen
    with tempfile.NamedTemporaryFile(delete=False, suffix=".bat", mode='w', encoding='utf-8') as batch_file:
        for command in commands:
            batch_file.write(command + "\n")
        batch_file_path = batch_file.name

    # PowerShell-Skript, um die Batch-Datei mit Adminrechten auszuführen
    powershell_script = f'''
    $batch_file = "{batch_file_path}"
    Start-Process -FilePath "cmd.exe" -ArgumentList "/c `" $batch_file `"" -Verb runAs
    '''
    
    # Temporäre PowerShell-Datei erstellen
    with tempfile.NamedTemporaryFile(delete=False, suffix=".ps1", mode='w', encoding='utf-8') as ps_file:
        ps_file.write(powershell_script)
        ps_file_path = ps_file.name

    # PowerShell-Skript ausführen
    subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", ps_file_path], check=True)

    # Temporäre Dateien löschen
    os.remove(ps_file_path)
    # Die Batch-Datei wird nicht sofort gelöscht, damit das Fenster offen bleibt
    print(f"Die Batch-Datei befindet sich unter: {batch_file_path}")


def log_command(command, output):
    with open(os.path.join(script_dir, "log.txt"), "a") as f:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[COMMAND] [{timestamp}] {command}\n")
        f.write(f"[OUTPUT] {output}\n")

def log_error(message, error):
    with open(os.path.join(script_dir, "log.txt"), "a") as f:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[ERROR] [{timestamp}] {message}\n")
        f.write(f"[DETAILS] {str(error)}\n")

def open_link(url):
    webbrowser.open_new(url)

def show_help():
    help_text = (
        "Health Scan: Scans for System Errors and fixxes them.\n"
        "PC Info: Shows detailed information about the PC.\n"
        "Clean: Starts the Windows Disk Cleanup.\n"
        "WSReset: Resets the Microsoft Store and clears its cache.\n"
        "Disk Cleanup: Performs an advanced disk cleanup.\n"
        "Temp Cleanup: Deletes temporary files.\n"
        "Update All: Updates all installed applications.\n"
        "Windows Update: Checks for new Windows updates.\n"
        "Driver Update: Updates all drivers.\n"
        "Clean Invis: Deletes invisible space-consuming files.\n"
    )
    messagebox.showinfo("Help", help_text)

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
    clean_mngr_button.pack(pady=10)
    wsreset_button.pack(pady=10)
    disk_cleanup_button.pack(pady=10)
    temp_cleanup_button.pack(pady=10)
    clean_invis_button.pack(pady=10)
    defragment_button.pack(pady=10)
    storage_diagonistics_button.pack(pady=10)
    Empty_RecycleBin_button.pack(pady=10)
    back_button.pack(pady=10)

def show_update_menu():
    clear_frame()
    update_apps_button.pack(pady=10)
    windows_update_button.pack(pady=10)
    driver_update_button.pack(pady=10)
    back_button.pack(pady=10)

def show_main_menu():
    clear_frame()
    info_button.pack(pady=10)
    clean_button.pack(pady=10)
    update_button.pack(pady=10)
    health_scan_button.pack(pady=10)
    help_button.pack(pady=10)
    logo_frame.pack(side=tk.TOP, anchor=tk.NW)

def clear_frame():
    for widget in root.winfo_children():
        widget.pack_forget()
    logo_frame.pack_forget()

def update_progress_window():
    def update_progress():
        global process
        start_time = time.time()
        while process.poll() is None:  # Solange der Prozess läuft
            elapsed_time = time.time() - start_time
            progress = min(int((elapsed_time / 60) * 100), 100)  # Simulierter Fortschritt basierend auf der Zeit
            progress_var.set(progress)
            progress_label.config(text=f"{progress}%")
            time.sleep(1)  # Wartezeit zum Aktualisieren der Fortschrittsanzeige
        
        progress_var.set(100)  # Setze den Fortschritt auf 100% am Ende
        progress_label.config(text="100%")
        progress_label.config(text="Cleaning Complete")
        progress_bar.stop()

    # Fortschrittsfenster erstellen
    progress_window = tk.Toplevel(root)
    progress_window.title("Progress")
    
    tk.Label(progress_window, text="Cleaning invisible space-consuming files. Close other apps to maximize cleanup and please be patient, this process may take a while.").pack(pady=10)
    
    global progress_var
    progress_var = tk.DoubleVar()
    progress_bar = ttk.Progressbar(progress_window, orient='horizontal', length=300, mode='determinate', variable=progress_var)
    progress_bar.pack(pady=10)

    progress_label = tk.Label(progress_window, text="0%")
    progress_label.pack(pady=10)

    # Fortschrittsanzeige im Hintergrund aktualisieren
    threading.Thread(target=update_progress, daemon=True).start()

def run_cipher_command():
    global process
    try:
        process = subprocess.Popen("cipher /w:c", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        stdout, stderr = process.communicate()
        
        if process.returncode == 0:
            messagebox.showinfo("Success", "Successfully deleted invisible space-consuming files.")
        else:
            raise subprocess.CalledProcessError(process.returncode, "cipher /w:c", output=stderr)
    except Exception as e:
        log_error("Error running cipher /w:c command", e)
        messagebox.showerror("Error", "An error occurred while cleaning invisible files. Please check the log file for details.")

def clean_invis_operation():
    info_message = "Cleaning invisible space-consuming files. Close other apps to maximize cleanup and please be patient, this process may take a while."
    messagebox.showinfo("Cleaning", info_message)

    # Fortschrittsfenster öffnen
    update_progress_window()

    # Starte die `cipher /w:c` Operation in einem neuen Thread
    threading.Thread(target=run_cipher_command, daemon=True).start()

# Creating the GUI
root = tk.Tk()
root.title("System Utility")
root.geometry("400x600")
root.configure(bg="#2E2E2E")

def load_image(file, size):
    image_path = os.path.join(script_dir, file)
    image = Image.open(image_path).resize(size, Image.LANCZOS)
    return ImageTk.PhotoImage(image)

pc_info_button = tk.Button(root, text="PC Info", command=show_pc_info, bg="#444", fg="white", activebackground="#555", activeforeground="white", borderwidth=1, relief="raised")
pc_info_button.pack(pady=10)

pc_info_button.bind("<Enter>", lambda e: pc_info_button.config(relief="sunken"))
pc_info_button.bind("<Leave>", lambda e: pc_info_button.config(relief="raised"))

info_button = tk.Button(root, text="Info", command=show_info_menu, bg="#444", fg="white", activebackground="#555", activeforeground="white", borderwidth=1, relief="raised")

systeminfo_button = tk.Button(root, text="Systeminfo", command=show_pc_info, bg="#444", fg="white", activebackground="#555", activeforeground="white", borderwidth=1, relief="raised")

advanced_systeminfo_button = tk.Button(root, text="Advanced Systeminfo", command=lambda: run_command("msinfo32.exe", "Successfully Retrieved Advanced Systeminfo."), bg="#444", fg="white", activebackground="#555", activeforeground="white", borderwidth=1, relief="raised")

resource_monitoring_button = tk.Button(root, text="Resource Monitoring", command=lambda: run_command("perfmon.exe /res", "Successfully ran Windows Resource Monitoring."), bg="#444", fg="white", activebackground="#555", activeforeground="white", borderwidth=1, relief="raised")

speedtest_button = tk.Button(root, text="Speedtest", command=show_speedtest_result, bg="#444", fg="white", activebackground="#555", activeforeground="white", borderwidth=1, relief="raised")

connection_button = tk.Button(root, text="Connection", command=show_connection_info, bg="#444", fg="white", activebackground="#555", activeforeground="white", borderwidth=1, relief="raised")

health_scan_button = tk.Button(root, text="Health Scan", command=health_scan, bg="#444", fg="white", activebackground="#555", activeforeground="white", borderwidth=1, relief="raised")

clean_button = tk.Button(root, text="Clean", command=show_clean_menu, bg="#444", fg="white", activebackground="#555", activeforeground="white", borderwidth=1, relief="raised")

clean_mngr_button = tk.Button(root, text="Clean Manager", command=lambda: run_command("cleanmgr", "Disk cleanup completed successfully."), bg="#444", fg="white", activebackground="#555", activeforeground="white", borderwidth=1, relief="raised")

wsreset_button = tk.Button(root, text="WSReset", command=lambda: run_command("wsreset.exe", "Microsoft Store reset completed successfully."), bg="#444", fg="white", activebackground="#555", activeforeground="white", borderwidth=1, relief="raised")

disk_cleanup_button = tk.Button(root, text="Disk Cleanup", command=lambda: run_command("cleanmgr /sagerun:1", "Advanced Disk Cleanup completed successfully."), bg="#444", fg="white", activebackground="#555", activeforeground="white", borderwidth=1, relief="raised")

temp_cleanup_button = tk.Button(root, text="Temp Cleanup", command=lambda: run_command("del /q/f/s %TEMP%\*", "Successfully deleted Temporary Files."), bg="#444", fg="white", activebackground="#555", activeforeground="white", borderwidth=1, relief="raised")

clean_invis_button = tk.Button(root, text="Clean Invis", command=clean_invis_operation, bg="#444", fg="white", activebackground="#555", activeforeground="white", borderwidth=1, relief="raised")

Empty_RecycleBin_button = tk.Button(root, text="Empty Recycle Bin", command=clean_recycle_bin, bg="#444", fg="white", activebackground="#555", activeforeground="white", borderwidth=1, relief="raised")

defragment_button = tk.Button(root, text="Defragment", command=defragment, bg="#444", fg="white", activebackground="#555", activeforeground="white", borderwidth=1, relief="raised")

storage_diagonistics_button = tk.Button(root, text="Storage Diagnostics", command=lambda: run_command("MdSched.exe", "Successfully ran Windows Storage Diagnostics."), bg="#444", fg="white", activebackground="#555", activeforeground="white", borderwidth=1, relief="raised")

update_button = tk.Button(root, text="Update", command=show_update_menu, bg="#444", fg="white", activebackground="#555", activeforeground="white", borderwidth=1, relief="raised")
update_button.pack(pady=10)

update_apps_button = tk.Button(root, text="Update Apps", command=update_apps, bg="#444", fg="white", activebackground="#555", activeforeground="white", borderwidth=1, relief="raised")

windows_update_button = tk.Button(root, text="Windows Update", command=lambda: run_command("wuauclt /detectnow /updatenow", "Windows update initiated successfully."), bg="#444", fg="white", activebackground="#555", activeforeground="white", borderwidth=1, relief="raised")

driver_update_button = tk.Button(root, text="Driver Update", command=lambda: run_command("wuauclt /detectnow /updatenow", "Drivers updated successfully."), bg="#444", fg="white", activebackground="#555", activeforeground="white", borderwidth=1, relief="raised")

back_button = tk.Button(root, text="Back", command=show_main_menu, bg="#444", fg="white", activebackground="#555", activeforeground="white", borderwidth=1, relief="raised")

help_button = tk.Button(root, text="Help", command=show_help, bg="#444", fg="white", activebackground="#555", activeforeground="white", borderwidth=1, relief="raised")

logo_image = load_image("logo.png", (150, 50))
logo_label = tk.Label(root, image=logo_image, bg="#2E2E2E")
logo_frame = tk.Frame(root, bg="#2E2E2E")
logo_label.pack()
logo_frame.pack(side=tk.TOP, anchor=tk.NW)

show_main_menu()

root.mainloop()