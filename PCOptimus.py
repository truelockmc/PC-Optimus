from tkinter import messagebox, ttk, scrolledtext, Listbox, MULTIPLE, Toplevel
from speedtest import Speedtest, ConfigRetrievalError
import psutil
import hashlib
import tkinter as tk
import tkinter.messagebox as messagebox
import threading
import platform
import socket
import time
import subprocess
import os
import re
import chardet
import ctypes
import sys
import traceback
import logging
import zipfile
import requests
import win32com.client

# Logging-Konfiguration
logging.basicConfig(filename="log.txt", level=logging.INFO, 
                    format="%(asctime)s - %(levelname)s - %(message)s")

# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Funktion, um zu überprüfen, ob Adminrechte vorhanden sind
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False	

def create_shortcut():
    # Automatische Bestimmung des aktuellen Skript-Pfads
    script_path = os.path.abspath(__file__)

    # Python-Interpreter-Pfad
    python_exe = sys.executable

    # Befehl zum Ausführen des Skripts mit dem Python-Interpreter
    command = f'"{python_exe}" "{script_path}"'

    # Name der Verknüpfung
    shortcut_name = 'PCOptimus'

    # Speicherort der Verknüpfung im Startmenü
    start_menu_path = os.path.join(os.environ['APPDATA'], 'Microsoft', 'Windows', 'Start Menu', 'Programs')
    shortcut_path = os.path.join(start_menu_path, f"{shortcut_name}.lnk")

    # Überprüfen, ob die Verknüpfung bereits existiert
    if os.path.exists(shortcut_path):
        print(f"The shortcut '{shortcut_name}' already exists at: {shortcut_path}")
    else:
        try:
            # Erstellen der Verknüpfung mit win32com.client
            shell = win32com.client.Dispatch('WScript.Shell')
            shortcut = shell.CreateShortcut(shortcut_path)
            shortcut.TargetPath = python_exe
            shortcut.Arguments = f'"{script_path}"'
            shortcut.WorkingDirectory = os.path.dirname(script_path)
            shortcut.IconLocation = python_exe
            shortcut.save()

            print(f"Shortcut '{shortcut_name}' successfully created at: {shortcut_path}")

            # Benachrichtigung und Abfrage, ob eine Desktop-Verknüpfung erstellt werden soll
            root = tk.Tk()
            root.withdraw()  # Verstecke das Hauptfenster

            # Zeige eine Nachricht an den Benutzer
            messagebox.showinfo("PCOptimus Shortcut Created",
                                "PCOptimus is now available in the Start Menu.\n")

            # Benutzerabfrage für die Desktop-Verknüpfung
            if messagebox.askyesno("Create Desktop Shortcut?",
                                   "Do you want to create a Desktop shortcut for PCOptimus?"):
                desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
                desktop_shortcut_path = os.path.join(desktop_path, f"{shortcut_name}.lnk")

                # Überprüfen, ob die Desktop-Verknüpfung bereits existiert
                if not os.path.exists(desktop_shortcut_path):
                    # Erstellen der Desktop-Verknüpfung
                    desktop_shortcut = shell.CreateShortcut(desktop_shortcut_path)
                    desktop_shortcut.TargetPath = python_exe
                    desktop_shortcut.Arguments = f'"{script_path}"'
                    desktop_shortcut.WorkingDirectory = os.path.dirname(script_path)
                    desktop_shortcut.IconLocation = python_exe
                    desktop_shortcut.save()
                    
                    messagebox.showinfo("Desktop Shortcut Created",
                                        f"Desktop shortcut '{shortcut_name}' successfully created.")
                else:
                    messagebox.showinfo("Desktop Shortcut Exists",
                                        f"The desktop shortcut '{shortcut_name}' already exists.")
        except Exception as e:
            messagebox.showerror("Error Creating Shortcut", f"Error creating the shortcut: {e}")

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

# Funktion, um den aktuellen Prozess als Administrator neu zu starten
def elevate():
    # Hole den Pfad zur aktuellen Python-Executable
    script = os.path.abspath(sys.argv[0])
    root.destroy()
    # Starte das Skript als Administrator neu
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, f'"{script}"', None, 1)

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
                elevate()
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

# Funktion, um einen Befehl als Administrator mit sichtbarem CMD-Fenster auszuführen
def run_window_admin_command(command, success_message):
    try:
        if platform.system() == "Windows":
            if is_admin():
                # Befehl in einem neuen CMD-Fenster ausführen
                # Der Befehl 'start' wird verwendet, um ein neues CMD-Fenster zu öffnen
                full_command = f'start cmd /k "{command}"'
                result = subprocess.run(full_command, shell=True)
                if result.returncode == 0 or result.returncode == 3:  # Ignoriere exit code 3
                    messagebox.showinfo("Success", success_message)
                else:
                    messagebox.showerror("Error", f"Command failed with return code {result.returncode}")
            else:
                # Skript als Administrator neu starten
                messagebox.showinfo("Info", "This action requires administrator privileges. The program will restart with elevated rights.")
                elevate()
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

# Funktion zum Abrufen der ISP-Informationen (Internetanbieter)
def get_provider_info():
    try:
        response = requests.get('https://ipinfo.io')
        data = response.json()
        return data.get('org', 'Unknown')  # ISP (Internetanbieter) aus den Daten extrahieren
    except:
        return "Unknown"

# Funktion zum Abrufen der Verbindungsinformationen
def get_connection_info():
    try:
        ip_address = socket.gethostbyname(socket.gethostname())
        network_name = get_network_name()
        signal_strength = "Unknown"  # Signalstärke ist in Windows nicht einfach abrufbar
        provider = get_provider_info()  # Anbieter durch API-Aufruf ermitteln
        return f"IP Address: {ip_address}\nNetwork Name: {network_name}\nSignal Strength: {signal_strength}\nProvider: {provider}"
    except Exception as e:
        return f"Failed to retrieve connection info: {e}"

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
		
# Funktion zum Anzeigen der Hilfenachricht
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

# Function to download and extract the .zip archive
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

# Function that is triggered when the "Advanced Debloat" button is clicked
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
		
# Liste der Bloatware mit den entsprechenden Paketnamen und geschätztem Speicherplatzbedarf in MB

bloatware_list = [
    ("Microsoft.BingNews", 80), ("Microsoft.GetHelp", 50), ("Microsoft.Getstarted", 40), ("Microsoft.Messaging", 60),
    ("Microsoft.Microsoft3DViewer", 100), ("Microsoft.MicrosoftOfficeHub", 100), ("Microsoft.MicrosoftSolitaireCollection", 60),
    ("Microsoft.NetworkSpeedTest", 70), ("Microsoft.News", 80), ("Microsoft.Office.Lens", 100), ("Microsoft.Office.OneNote", 150),
    ("Microsoft.Office.Sway", 60), ("Microsoft.OneConnect", 70), ("Microsoft.People", 50), ("Microsoft.Print3D", 95),
    ("Microsoft.SkypeApp", 120), ("Microsoft.Office.Todo.List", 60), ("microsoft.windowscommunicationsapps", 100),
    ("Microsoft.WindowsFeedbackHub", 80), ("Microsoft.ZuneMusic", 150), ("Microsoft.ZuneVideo", 200), ("EclipseManager", 80),
    ("ActiproSoftwareLLC", 90), ("Adobe.CCExpress", 200), ("AdobeSystemsIncorporated.AdobePhotoshopExpress", 150),
    ("Clipchamp.Clipchamp", 10000), ("Facebook.Facebook", 50), ("Instagram.Instagram", 75), ("Netflix.Netflix", 120),
    ("AmazonVideo.PrimeVideo", 130), ("Microsoft.HiddenCity", 300), ("Microsoft.MixedReality.Portal", 200),
    ("ROBLOXCORPORATION.ROBLOX", 250), ("TikTok.TikTok", 90), ("Microsoft.AgeOfEmpiresCastleSiege", 180),
    ("GAMELOFTSA.Asphalt8Airborne", 400), ("king.com.BubbleWitch3Saga", 110), ("king.com.CandyCrushFriends", 140),
    ("king.com.CandyCrushSaga", 160), ("Zynga.FarmVille2CountryEscape", 150), ("Fitbit.FitbitCoach", 90),
    ("Playrix.Gardenscapes", 100), ("PhototasticCollage", 50), ("PicsArt-Photostudio", 85), ("SpotifyAB.SpotifyMusic", 110),
    ("Twitter.Twitter", 70), ("Microsoft.549981C3F5F10", 150), ("Microsoft.3DBuilder", 120), ("Microsoft.BingFinance", 60),
    ("Microsoft.BingFoodAndDrink", 40), ("Microsoft.BingHealthAndFitness", 70), ("Microsoft.BingSports", 50),
    ("Microsoft.BingTranslator", 55), ("Microsoft.BingTravel", 50), ("Microsoft.BingWeather", 45), ("Microsoft.MicrosoftJournal", 85),
    ("Microsoft.MicrosoftPowerBIForWindows", 150), ("Microsoft.Todos", 70), ("Microsoft.WindowsMaps", 100), ("Microsoft.WindowsSoundRecorder", 15), ("MSTeams", 200),
    ("ACGMediaPlayer", 80), ("AutodeskSketchBook", 150), ("CaesarsSlotsFreeCasino", 85), ("COOKINGFEVER", 100),
    ("CyberLinkMediaSuiteEssentials", 200), ("DisneyMagicKingdoms", 90), ("DrawboardPDF", 100), ("Duolingo-LearnLanguagesforFree", 70),
    ("FarmVille2CountryEscape", 150), ("Fitbit", 90), ("Flipboard", 70), ("HULULLC.HULUPLUS", 150),
    ("iHeartRadio", 80), ("LinkedInforWindows", 40), ("MarchofEmpires", 110), ("PandoraMediaInc", 60),
    ("Plex", 120), ("PolarrPhotoEditorAcademicEdition", 90), ("Royal Revolt", 100), ("Shazam", 50),
    ("Sidia.LiveWallpaper", 60), ("SlingTV", 120), ("TuneInRadio", 70), ("Viber", 75), ("WinZipUniversal", 80),
    ("Wunderlist", 50), ("XING", 60)
]

def run_powershell_command(command):
    try:
        result = subprocess.run(["powershell", "-Command", command], capture_output=True, text=True)
        result.check_returncode()
        logging.info(f"Command executed successfully: {command}")
        return result.stdout
    except subprocess.CalledProcessError as e:
        logging.error(f"Error executing command: {command} | Error: {e}")
        return ""

def check_installed_apps(progress_label):
    installed_apps = []
    progress_label.config(text="Checking for installed Bloatware...")
    root.update()  # Aktualisiert das Fenster, um die Nachricht anzuzeigen

    for app, size in bloatware_list:
        if app in run_powershell_command(f"Get-AppxPackage -Name {app}"):
            installed_apps.append((app, size))

    progress_label.config(text="")
    return installed_apps

def uninstall_selected_apps(selected_apps):
    for app, _ in selected_apps:
        command = f"Get-AppxPackage -Name {app} | Remove-AppxPackage"
        run_powershell_command(command)
        
        # Überprüfen, ob die App noch installiert ist
        remaining = run_powershell_command(f"Get-AppxPackage -Name {app}")
        if app not in remaining:
            logging.info(f"Uninstalled: {app}")
        else:
            logging.error(f"Failed to uninstall: {app}")

def confirm_uninstall():
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

def rm_Bloatware():
    if not is_admin():
        messagebox.showwarning("Admin Rights Required", "This action requires admin rights. The program will restart with elevated privileges.")
        elevate()
        root.quit()  # Altes Fenster schließen
        os._exit(0)  # Sofort das alte Fenster beenden
        return

    bloatware_window = tk.Toplevel(root)
    bloatware_window.title("Bloatware Uninstaller")
    bloatware_window.geometry("500x500")  # Increases the window size
    bloatware_window.configure(bg="#333")

    progress_label = tk.Label(bloatware_window, text="", fg="white", bg="#333")
    progress_label.pack(pady=10)

    installed_apps = check_installed_apps(progress_label)

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
        confirmation = confirm_uninstall()
        if confirmation == "Uninstall pls":
            uninstall_selected_apps(checked_apps)
            remaining_apps = check_installed_apps(progress_label)
            if not any(app in [a[0] for a in remaining_apps] for app, _ in checked_apps):
                messagebox.showinfo("Uninstallation Complete", "Selected apps have been uninstalled.")
            else:
                messagebox.showerror("Uninstallation Failed", "Some apps could not be uninstalled.")
            bloatware_window.destroy()
        else:
            messagebox.showinfo("Uninstallation Cancelled", "No apps were uninstalled.")

    tk.Button(bloatware_window, text="Uninstall selected", command=on_uninstall, bg="#444", fg="white").pack(pady=20)
    tk.Button(bloatware_window, text="Advanced Debloat+Stop Tracking", command=advanced_debloat, bg="#444", fg="white").pack(pady=20)
    
# Function to compute the hash of a file
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

# Function to find duplicates in specified directories
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

# Function to search for duplicates and display them in the sub-window
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

# Function to delete selected files
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

# Function to open the sub-window for finding duplicates
def rm_dupe():
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

create_shortcut()

# Creating the GUI
root = tk.Tk()
root.title("PC Optimus")
root.geometry("400x600")
root.configure(bg="#2E2E2E")

repair_file_system_button = tk.Button(root, text="Repair Filesystem", command=lambda: run_admin_command("echo J | chkdsk /f", "Successfully initiated chkdsk, your File System will be checked on the next startup."), bg="#444", fg="white", activebackground="#555", activeforeground="white", borderwidth=1, relief="raised")

clean_vs_button = tk.Button(root, text="Clean Virtual Storage", command=clean_vs, bg="#444", fg="white", activebackground="#555", activeforeground="white", borderwidth=1, relief="raised")

rm_dupe_button = tk.Button(root, text="Remove File Duplicates", command=rm_dupe, bg="#444", fg="white", activebackground="#555", activeforeground="white", borderwidth=1, relief="raised")

info_button = tk.Button(root, text="Info", command=show_info_menu, bg="#444", fg="white", activebackground="#555", activeforeground="white", borderwidth=1, relief="raised")

repair_button = tk.Button(root, text="Repair", command=show_repair_menu, bg="#444", fg="white", activebackground="#555", activeforeground="white", borderwidth=1, relief="raised")

systeminfo_button = tk.Button(root, text="Systeminfo", command=show_pc_info, bg="#444", fg="white", activebackground="#555", activeforeground="white", borderwidth=1, relief="raised")

advanced_systeminfo_button = tk.Button(root, text="Advanced Systeminfo", command=lambda: run_command("msinfo32.exe", "Successfully Retrieved Advanced Systeminfo."), bg="#444", fg="white", activebackground="#555", activeforeground="white", borderwidth=1, relief="raised")

resource_monitoring_button = tk.Button(root, text="Resource Monitoring", command=lambda: run_command("perfmon.exe /res", "Successfully ran Windows Resource Monitoring."), bg="#444", fg="white", activebackground="#555", activeforeground="white", borderwidth=1, relief="raised")

speedtest_button = tk.Button(root, text="Speedtest", command=show_speedtest_result, bg="#444", fg="white", activebackground="#555", activeforeground="white", borderwidth=1, relief="raised")

connection_button = tk.Button(root, text="Connection", command=show_connection_info, bg="#444", fg="white", activebackground="#555", activeforeground="white", borderwidth=1, relief="raised")

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

rm_bloatware_button = tk.Button(root, text="Remove Bloatware", command=rm_Bloatware, bg="#444", fg="white", activebackground="#555", activeforeground="white", borderwidth=1, relief="raised")

show_main_menu()

root.mainloop()