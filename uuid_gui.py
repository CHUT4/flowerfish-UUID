import tkinter as tk
import subprocess
import sys, os

def resource_path(relative_path):
    """Dapatkan path file saat running exe"""
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

def get_uuid():
    try:
        output = subprocess.check_output("wmic csproduct get uuid", shell=True)
        uuid = output.decode().split("\n")[1].strip()
        return uuid
    except Exception as e:
        return f"Error: {e}"

def show_uuid():
    uuid = get_uuid()
    result_entry.config(state="normal")
    result_entry.delete(0, tk.END)
    result_entry.insert(0, uuid)
    result_entry.config(state="readonly")

root = tk.Tk()
root.title("Serial Number Motherboard UUID Finder")

# ganti icon (Windows pakai .ico)
root.iconbitmap(resource_path("flowerfish.ico"))

root.geometry("400x200")

label = tk.Label(root, text="Klik tombol untuk mendapatkan UUID motherboard", font=("Arial", 10))
label.pack(pady=10)

button = tk.Button(root, text="Get UUID", command=show_uuid, font=("Arial", 12))
button.pack(pady=10)

result_entry = tk.Entry(root, font=("Arial", 10), fg="blue", width=40)
result_entry.pack(pady=10)

root.mainloop()
