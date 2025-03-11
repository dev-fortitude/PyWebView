import os
import webview
import tkinter as tk
from tkinter import messagebox, scrolledtext
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

dark_mode = False

def toggle_theme():
    """Toggle between light and dark mode."""
    global dark_mode
    dark_mode = not dark_mode
    logging.debug(f"Theme toggled. Dark mode: {dark_mode}")
    update_theme()

def update_theme():
    """Update the UI theme based on the current mode."""
    try:
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
        log_text.config(bg=bg_color, fg=fg_color)
        
        logging.debug("Theme updated successfully.")
    except Exception as e:
        log_error(f"Error updating theme: {e}")

def create_webview_script(url):
    """Create a Python script to launch a WebView for the given URL."""
    try:
        script_content = f"""import webview
webview.create_window('WebView App', '{url}')
webview.start()"""
        
        with open("Output.py", "w", encoding="utf-8") as file:
            file.write(script_content)
        log_info("WebView script created successfully.")
    except Exception as e:
        log_error(f"Error creating WebView script: {e}")

def build_exe():
    """Build an EXE file using PyInstaller."""
    try:
        if not os.path.exists("Output.py"):
            log_warning("No script found. Cannot proceed with EXE build.")
            messagebox.showerror("Error", "No script found. Enter a URL and click 'Create Script' first.")
            return
        
        log_info("Starting EXE build...")
        os.system("pyinstaller --onefile --noconsole Output.py")
        log_info("EXE build completed successfully.")
        messagebox.showinfo("Success", "Python launcher file built successfully! Check the root directory")
    except Exception as e:
        log_error(f"Error during EXE build: {e}")
        messagebox.showerror("Error", "An error occurred while building the EXE file.")

def generate_script():
    """Generate the WebView script based on the user input."""
    try:
        url = url_entry.get().strip()
        if not url:
            log_warning("Invalid URL entered.")
            messagebox.showerror("Error", "Please enter a valid URL.")
            return
        
        log_info(f"Generating script for URL: {url}")
        create_webview_script(url)
        messagebox.showinfo("Success", "Script generated successfully! Now, click 'Complete Launcher'.")
    except Exception as e:
        log_error(f"Error generating script: {e}")

def log_info(message):
    logging.info(message)
    log_text.insert(tk.END, f"INFO: {message}\n")
    log_text.yview(tk.END)

def log_warning(message):
    logging.warning(message)
    log_text.insert(tk.END, f"WARNING: {message}\n")
    log_text.yview(tk.END)

def log_error(message):
    logging.error(message)
    log_text.insert(tk.END, f"ERROR: {message}\n")
    log_text.yview(tk.END)

root = tk.Tk()
root.title("WebView Builder")
root.geometry("400x350")

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

log_text = scrolledtext.ScrolledText(root, height=6, width=50, state=tk.NORMAL)
log_text.pack(pady=5)

update_theme()
log_info("Application started successfully.")
root.mainloop()