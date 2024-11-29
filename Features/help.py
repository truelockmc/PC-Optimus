import tkinter.messagebox as messagebox

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