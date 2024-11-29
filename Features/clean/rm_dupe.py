import os
import hashlib
import tkinter as tk
import tkinter.messagebox as messagebox
from tkinter import messagebox, ttk, scrolledtext, Listbox, MULTIPLE, Toplevel

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
def rm_dupe(root):
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