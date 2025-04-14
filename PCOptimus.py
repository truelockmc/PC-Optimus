import tkinter as tk
from Features.shortcut import create_shortcut
from Features.clean.tiny_clean_features import clean_recycle_bin, clean_vs, defragment
from Features.command_handling import run_command, run_admin_command, run_window_admin_command
from Features.info.connection import show_connection_info
from Features.clean.rm_bloat import rm_Bloatware
from Features.clean.rm_dupe import rm_dupe
from Features.clean.clean_startup import clean_startup
from Features.info.internet_speedtest import open_speedtest_window
from Features.info.pc_info import show_pc_info
from UI.Buttons import create_buttons

# Menue Funktionen
def show_info_menu():
    clear_frame()
    buttons['systeminfo_button'].pack(pady=10)
    buttons['advanced_systeminfo_button'].pack(pady=10)
    buttons['resource_monitoring_button'].pack(pady=10)
    buttons['speedtest_button'].pack(pady=10)
    buttons['connection_button'].pack(pady=10)
    buttons['back_button'].pack(pady=10)

def show_clean_menu():
    clear_frame()
    buttons['rm_bloatware_button'].pack(pady=10)
    buttons['rm_dupe_button'].pack(pady=10)
    buttons['clean_mngr_button'].pack(pady=10)
    buttons['clean_startup_button'].pack(pady=10)
    buttons['wsreset_button'].pack(pady=10)
    buttons['disk_cleanup_button'].pack(pady=10)
    buttons['temp_cleanup_button'].pack(pady=10)
    buttons['prefetch_clean_button'].pack(pady=10)
    buttons['clean_invis_button'].pack(pady=10)
    buttons['defragment_button'].pack(pady=10)
    buttons['clean_vs_button'].pack(pady=10)
    buttons['Empty_RecycleBin_button'].pack(pady=10)
    buttons['back_button'].pack(pady=10)

def show_update_menu():
    clear_frame()
    buttons['update_apps_button'].pack(pady=10)
    buttons['windows_update_button'].pack(pady=10)
    buttons['driver_update_button'].pack(pady=10)
    buttons['back_button'].pack(pady=10)

def show_repair_menu():
    clear_frame()
    buttons['health_scan_button'].pack(pady=10)
    buttons['storage_diagonistics_button'].pack(pady=10)
    buttons['repair_file_system_button'].pack(pady=10)
    buttons['repair_connection_button'].pack(pady=10)
    buttons['check_hardware_button'].pack(pady=10)
    buttons['back_button'].pack(pady=10)

def show_main_menu():
    clear_frame()
    buttons['info_button'].pack(pady=10)
    buttons['clean_button'].pack(pady=10)
    buttons['update_button'].pack(pady=10)
    buttons['repair_button'].pack(pady=10)
    buttons['help_button'].pack(pady=10)

def clear_frame():
    for widget in root.winfo_children():
        widget.pack_forget()

# GUI starten
root = tk.Tk()
root.title("PC Optimus")
root.geometry("400x600")
root.configure(bg="#2E2E2E")

create_shortcut()

# Buttons erstellen
buttons = create_buttons(
    root, show_main_menu, show_info_menu, show_clean_menu, show_update_menu, show_repair_menu
)

show_main_menu()

root.mainloop()
