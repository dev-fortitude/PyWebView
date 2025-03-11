import os
import sys
import webview
import tkinter as tk
from tkinter import messagebox

def create_webview_script(url):
    script_content = f"""import webview
webview.create_window('WebView App', '{url}')
webview.start()"""
    
    with open("Output.py", "w", encoding="utf-8") as file:
        file.write(script_content)

def build_exe():
    if not os.path.exists("Output.py"):
        messagebox.showerror("Error", "No script found. Enter a URL and click 'Create Script' first.")
        return
    
    os.system("pyinstaller --onefile --noconsole Output.py")
    messagebox.showinfo("Success", "Python launcher file built successfully! Check the root directory")

def generate_script():
    url = url_entry.get().strip()
    if not url:
        messagebox.showerror("Error", "Please enter a valid URL.")
        return
    
    create_webview_script(url)
    messagebox.showinfo("Success", "Script generated successfully! Now, click 'Complete Launcher'.")

root = tk.Tk()
root.title("WebView Builder")
root.geometry("400x200")

tk.Label(root, text="Enter Website URL:").pack(pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate WebView Script", command=generate_script)
generate_button.pack(pady=5)

build_button = tk.Button(root, text="Complete Launcher", command=build_exe)
build_button.pack(pady=5)

root.mainloop()