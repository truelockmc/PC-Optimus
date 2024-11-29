from speedtest import Speedtest, ConfigRetrievalError
import tkinter as tk
import tkinter.messagebox as messagebox
from tkinter import Toplevel
from Features.logging_func import log_error

# Function to check internet speed
def get_internet_speed(root):
    try:
        st = Speedtest()
        st.get_best_server()
        download_speed = st.download() / 1_000_000  # Mbps
        upload_speed = st.upload() / 1_000_000      # Mbps
        ping = st.results.ping
        return download_speed, upload_speed, ping
    except ConfigRetrievalError as e:
        log_error("Failed to retrieve speedtest configuration", e)
        messagebox.showerror("Speedtest Error", "Failed to retrieve speedtest configuration. Please check the log file for details.")
        return 0, 0, 0

# Function to show speedtest result
def open_speedtest_window(root):
    download_speed, upload_speed, ping = get_internet_speed(root)
    result = f"Download Speed: {download_speed:.2f} Mbps\nUpload Speed: {upload_speed:.2f} Mbps\nPing: {ping} ms"
    
    # Create new window for result
    info_window = Toplevel(root)
    info_window.title("Speedtest Result")
    info_window.geometry("400x200")
    info_window.configure(bg="black")  # Dark mode background for result window
    
    # Create Text widget to show results
    text = tk.Text(info_window, bg="black", fg="white", font=("Helvetica", 12))
    text.insert(tk.END, result)
    text.config(state=tk.DISABLED)
    text.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)