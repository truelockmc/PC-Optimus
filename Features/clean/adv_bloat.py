import requests
import zipfile
import tkinter.messagebox as messagebox
from Features.logging_func import log_error, log_command
import os
import subprocess

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
		