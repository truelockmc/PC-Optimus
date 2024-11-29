from Features.logging_func import log_command, log_error
import socket
import tkinter as tk
import requests
import subprocess
import chardet  # Ensure you import chardet

def run_command_nomsg(command):
    try:
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        stdout, stderr = process.communicate()

        # Erkennen der Kodierung
        result_encoding = chardet.detect(stdout)['encoding']
        if result_encoding is None:
            result_encoding = 'utf-8'  # Fallback auf eine Standardkodierung

        # Log the output (whether it's success or error)
        if process.returncode == 0:
            decoded_output = stdout.decode(result_encoding, errors='ignore')
            log_command(command, decoded_output)
            return decoded_output  # Return the output so it can be processed by the caller
        else:
            decoded_error = stderr.decode(result_encoding, errors='ignore')
            log_command(command, decoded_error)
            raise subprocess.CalledProcessError(process.returncode, command, output=stderr)

    except Exception as e:
        log_error(f"Error running command: {command}", e)
        raise  # Re-raise the exception to be handled by the caller

# Function to retrieve network name
def get_network_name():
    try:
        result = subprocess.run(['powershell', '-Command', 'Get-NetConnectionProfile | Select-Object -ExpandProperty Name'], capture_output=True, text=True)
        network_name = result.stdout.strip()
        return network_name if network_name else "Not connected"
    except Exception as e:
        log_error("Failed to retrieve network name", e)
        return "Not connected"

# Function to get ISP information
def get_provider_info():
    try:
        response = requests.get('https://ipinfo.io')
        data = response.json()
        return data.get('org', 'Unknown')  # ISP (Internet Service Provider) from the data
    except:
        return "Unknown"

def get_signal_strength():
    try:
        result = run_command_nomsg(["netsh", "wlan", "show", "interfaces"])
        # Split the result into lines and search for the "Signal" line
        for line in result.splitlines():
            if "Signal" in line:
                # Extract and return the signal strength value, assuming it's in percentage
                signal_strength = line.split(":")[1].strip()
                return f"Signal Strength: {signal_strength}"
        return "Signal Strength: Unknown"
    except Exception as e:
        return f"Failed to retrieve signal strength: {e}"

# Function to retrieve connection information
def get_connection_info():
    try:
        ip_address = socket.gethostbyname(socket.gethostname())
        network_name = get_network_name()
        signal_strength = get_signal_strength()
        provider = get_provider_info()  # Get provider info from API
        return f"IP Address: {ip_address}\nNetwork Name: {network_name}\nSignal Strength: {signal_strength}\nProvider: {provider}"
    except Exception as e:
        return f"Failed to retrieve connection info: {e}"

# Function to show connection info in a new window with dark mode
def show_connection_info(root):
    info = get_connection_info()

    # Create a new window for connection information
    info_window = tk.Toplevel(root)
    info_window.title("Connection Information")
    info_window.geometry("400x300")
    info_window.configure(bg="black")  # Set the background color to black for dark mode
    
    # Create a Text widget to display the connection info
    text = tk.Text(info_window, bg="black", fg="white", font=("Helvetica", 12))
    text.insert(tk.END, info)
    text.config(state=tk.DISABLED)
    text.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)