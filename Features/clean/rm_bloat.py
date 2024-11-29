from Features.clean.adv_bloat import advanced_debloat
import subprocess
from Features.logging_func import log_error, log_command
import tkinter as tk
import tkinter.messagebox as messagebox
from tkinter import messagebox, ttk, scrolledtext, Listbox, MULTIPLE, Toplevel
import sys
import os
from Features.admin_elevate import is_admin, elevate
import logging

# Liste der Bloatware mit den entsprechenden Paketnamen und geschätztem Speicherplatzbedarf in MB
bloatware_list = [
    ("Microsoft.BingNews", 80), ("Microsoft.Getstarted", 40), ("Microsoft.Messaging", 60),
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

def check_installed_apps(progress_label, root):
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

def confirm_uninstall(root):
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

def rm_Bloatware(root):
    if not is_admin():
        messagebox.showwarning("Admin Rights Required", "This action requires admin rights. The program will restart with elevated privileges.")
        elevate(root)
        root.quit()  # Altes Fenster schließen
        os._exit(0)  # Sofort das alte Fenster beenden
        return

    bloatware_window = tk.Toplevel(root)
    bloatware_window.title("Bloatware Uninstaller")
    bloatware_window.geometry("500x500")  # Increases the window size
    bloatware_window.configure(bg="#333")

    progress_label = tk.Label(bloatware_window, text="", fg="white", bg="#333")
    progress_label.pack(pady=10)

    installed_apps = check_installed_apps(progress_label, root)

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
        confirmation = confirm_uninstall(root)
        if confirmation == "Uninstall pls":
            uninstall_selected_apps(checked_apps)
            remaining_apps = check_installed_apps(progress_label, root)
            if not any(app in [a[0] for a in remaining_apps] for app, _ in checked_apps):
                messagebox.showinfo("Uninstallation Complete", "Selected apps have been uninstalled.")
            else:
                messagebox.showerror("Uninstallation Failed", "Some apps could not be uninstalled.")
            bloatware_window.destroy()
        else:
            messagebox.showinfo("Uninstallation Cancelled", "No apps were uninstalled.")

    tk.Button(bloatware_window, text="Uninstall selected", command=on_uninstall, bg="#444", fg="white").pack(pady=20)
    tk.Button(bloatware_window, text="Advanced Debloat+Stop Tracking", command=advanced_debloat, bg="#444", fg="white").pack(pady=20)