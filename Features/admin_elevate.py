import ctypes
import os
import sys

# Funktion, um zu überprüfen, ob Adminrechte vorhanden sind
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False	

# Funktion, um den aktuellen Prozess als Administrator neu zu starten
def elevate(root):
    # Hole den Pfad zur aktuellen Python-Executable
    script = os.path.abspath(sys.argv[0])
    root.destroy()
    # Starte das Skript als Administrator neu
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, f'"{script}"', None, 1)