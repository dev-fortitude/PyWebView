import os
import webview
import tkinter as tk
from tkinter import messagebox

dark_mode = False

def toggle_theme():
    global dark_mode
    dark_mode = not dark_mode
    update_theme()

def update_theme():
    bg_color = "#2E2E2E" if dark_mode else "#F0F0F0"
    fg_color = "white" if dark_mode else "black"
    button_bg = "#555" if dark_mode else "#DDD"
    theme_text = "Light Mode" if dark_mode else "Dark Mode"
    
    root.configure(bg=bg_color)
    label.config(bg=bg_color, fg=fg_color)
    url_entry.config(bg=button_bg, fg=fg_color, insertbackground=fg_color)
    generate_button.config(bg=button_bg, fg=fg_color)
    build_button.config(bg=button_bg, fg=fg_color)
    theme_button.config(bg=button_bg, fg=fg_color, text=theme_text)

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
root.geometry("400x250")

label = tk.Label(root, text="Enter Website URL:")
label.pack(pady=5)

url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate WebView Script", command=generate_script)
generate_button.pack(pady=5)

build_button = tk.Button(root, text="Complete Launcher", command=build_exe)
build_button.pack(pady=5)

theme_button = tk.Button(root, text="Dark Mode", command=toggle_theme)
theme_button.pack(pady=5)

update_theme()
root.mainloop()