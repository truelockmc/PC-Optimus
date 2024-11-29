import os
import sys
import win32com.client
import tkinter.messagebox as messagebox
import tkinter as tk

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