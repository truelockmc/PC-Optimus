import logging
from tkinter import messagebox, ttk, scrolledtext, Listbox, MULTIPLE, Toplevel
import tkinter as tk
import tkinter.messagebox as messagebox
import winreg
from Features.admin_elevate import elevate, is_admin
from Features.logging_func import log_error
import os

# Logging-Konfiguration
logging.basicConfig(filename="log.txt", level=logging.INFO, 
                    format="%(asctime)s - %(levelname)s - %(message)s")

# Liste der kritischen Dateien/Ordner, die nicht deaktiviert werden sollen
critical_files = ["desktop.ini", "ntuser.dat", "pagefile.sys", "swapfile.sys"]
critical_dirs = ["system32", "SysWOW64"]

# Funktion, um Autostart-Programme aus Registry und Autostart-Ordner abzurufen
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

# Globale Definition von reg_paths
reg_paths = {
    "HKCU_Run": (winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run"),
    "HKCU_RunOnce": (winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\RunOnce"),
    "HKLM_Run": (winreg.HKEY_LOCAL_MACHINE, r"Software\Microsoft\Windows\CurrentVersion\Run"),
    "HKLM_RunOnce": (winreg.HKEY_LOCAL_MACHINE, r"Software\Microsoft\Windows\CurrentVersion\RunOnce")
}

# Funktion zum Deaktivieren ausgewählter Autostart-Programme
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


# Funktion, die beim Drücken des "Clean Startup"-Buttons ausgeführt wird
def clean_startup(root):
    if not is_admin():
        logging.info("Asking for right elevation.")
        elevate(root)
    else:
        logging.info("Admin already achieved")
        show_autostart_gui(root)

# GUI-Funktion zur Auswahl der Autostart-Programme
def show_autostart_gui(root):
    programs = get_autostart_programs()
    if not programs:
        messagebox.showinfo("No Startup Apps", "No startup apps found")
        logging.info("No startup apps found")
        return
    
    # Neues Fenster für die Auswahl der Autostart-Programme
    window = tk.Toplevel(root)
    window.title("Startup App Manager")
    window.configure(bg="#2e2e2e")
    
    # Liste der Checkboxen für jedes Autostart-Programm
    checkboxes = []
    for program in programs:
        var = tk.BooleanVar()
        cb = tk.Checkbutton(window, text=f"{program['name']} ({program['source']}) - {program['path']}", variable=var,
                            bg="#2e2e2e", fg="white", selectcolor="#444", activebackground="#555", activeforeground="white")
        cb.pack(anchor="w", padx=10, pady=2)
        checkboxes.append((var, program))

    # Button zum Deaktivieren der ausgewählten Programme
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