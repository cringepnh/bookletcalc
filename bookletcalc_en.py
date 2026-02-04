"""
BookletCalc - Page Calculator for Booklet Printing
Duplex booklet printing on A4 (2 pages per sheet)

This program calculates the page order for manual
duplex printing on a printer.
"""

import tkinter as tk
from tkinter import ttk, messagebox
import math
import os
import sys


def calculate_pages(total_pages: int) -> tuple[str, str]:
    """
    Calculate page order for booklet printing.
    
    In booklet format, each sheet contains 4 page positions:
    - Front side: 2 pages
    - Back side: 2 pages
    
    Args:
        total_pages: Number of pages in the document
        
    Returns:
        tuple: (first_pass, second_pass) - comma-separated page numbers
    """
    # Number of sheets - divide by 4, round up
    num_sheets = math.ceil(total_pages / 4)
    
    # Total positions (including blank pages)
    total_positions = num_sheets * 4
    
    # First pass (front side of sheets)
    first_pass = []
    
    # Second pass (back side of sheets)
    second_pass = []
    
    for sheet in range(num_sheets):
        # Calculate page numbers for each sheet
        
        # Front side: [last - 2*sheet, 1 + 2*sheet]
        # Example, 8 pages: sheet 0 -> [8, 1], sheet 1 -> [6, 3]
        front_left = total_positions - (2 * sheet)
        front_right = 1 + (2 * sheet)
        
        first_pass.append(front_left)
        first_pass.append(front_right)
        
        # Back side: [2 + 2*sheet, last - 1 - 2*sheet]
        # Example, 8 pages: sheet 0 -> [2, 7], sheet 1 -> [4, 5]
        back_left = 2 + (2 * sheet)
        back_right = total_positions - 1 - (2 * sheet)
        
        second_pass.append(back_left)
        second_pass.append(back_right)
    
    # Format (only existing pages)
    def format_pages(pages: list[int]) -> str:
        """Format page numbers as comma-separated string"""
        existing = [p for p in pages if p <= total_pages]
        return ",".join(str(p) for p in existing)
    
    return format_pages(first_pass), format_pages(second_pass)


def on_calculate_click():
    """Handler for Calculate button click"""
    entered = input_field.get().strip()
    
    # Validation: empty or invalid value
    if not entered:
        messagebox.showerror("Error", "Please enter the number of pages!")
        return
    
    try:
        total = int(entered)
    except ValueError:
        messagebox.showerror("Error", "Please enter a whole number!")
        return
    
    if total < 1:
        messagebox.showerror("Error", "Number of pages must be at least 1!")
        return
    
    if total > 10000:
        messagebox.showerror("Error", "Too many pages (maximum 10000)!")
        return
    
    # Calculate
    first, second = calculate_pages(total)
    
    # Display results
    first_pass_text.config(state="normal")
    first_pass_text.delete("1.0", tk.END)
    first_pass_text.insert("1.0", first)
    
    second_pass_text.config(state="normal")
    second_pass_text.delete("1.0", tk.END)
    second_pass_text.insert("1.0", second)
    
    # Info
    sheets = math.ceil(total / 4)
    total_positions = sheets * 4
    blank_pages = total_positions - total
    
    if blank_pages > 0:
        info_label.config(text=f"Total: {total} pages, {sheets} sheets. ({blank_pages} blank pages)")
    else:
        info_label.config(text=f"Total: {total} pages, {sheets} sheets needed")


def copy_first():
    """Copy first pass to clipboard"""
    text = first_pass_text.get("1.0", tk.END).strip()
    if text:
        window.clipboard_clear()
        window.clipboard_append(text)
        messagebox.showinfo("Done", "First pass copied!")


def copy_second():
    """Copy second pass to clipboard"""
    text = second_pass_text.get("1.0", tk.END).strip()
    if text:
        window.clipboard_clear()
        window.clipboard_append(text)
        messagebox.showinfo("Done", "Second pass copied!")


# === MAIN WINDOW ===
window = tk.Tk()
window.title("BookletCalc - Booklet Page Calculator")
window.geometry("500x400")
window.resizable(True, True)

# Minimum size
window.minsize(400, 350)

# Set icon
def resource_path(relative_path):
    """Get path for PyInstaller bundled resources"""
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), relative_path)

try:
    window.iconbitmap(resource_path('icon.ico'))
except:
    pass  # If icon not found, use default

# === INPUT SECTION ===
input_frame = ttk.Frame(window, padding="10")
input_frame.pack(fill="x")

ttk.Label(input_frame, text="Number of pages:", font=("Arial", 11)).pack(side="left")

input_field = ttk.Entry(input_frame, width=15, font=("Arial", 11))
input_field.pack(side="left", padx=10)

# Enter key binding
input_field.bind("<Return>", lambda e: on_calculate_click())

calculate_button = ttk.Button(input_frame, text="Calculate", command=on_calculate_click)
calculate_button.pack(side="left")

# === INFO LABEL ===
info_label = ttk.Label(window, text="", font=("Arial", 10), foreground="gray")
info_label.pack(pady=5)

# === RESULTS SECTION ===

# First pass
first_frame = ttk.LabelFrame(window, text="1st Pass (front side)", padding="10")
first_frame.pack(fill="both", expand=True, padx=10, pady=5)

first_pass_text = tk.Text(first_frame, height=3, font=("Consolas", 10), wrap="word")
first_pass_text.pack(fill="both", expand=True, side="left")

first_scroll = ttk.Scrollbar(first_frame, orient="vertical", command=first_pass_text.yview)
first_scroll.pack(side="right", fill="y")
first_pass_text.config(yscrollcommand=first_scroll.set)

copy_first_button = ttk.Button(window, text="Copy 1st Pass", command=copy_first)
copy_first_button.pack(pady=2)

# Second pass
second_frame = ttk.LabelFrame(window, text="2nd Pass (back side)", padding="10")
second_frame.pack(fill="both", expand=True, padx=10, pady=5)

second_pass_text = tk.Text(second_frame, height=3, font=("Consolas", 10), wrap="word")
second_pass_text.pack(fill="both", expand=True, side="left")

second_scroll = ttk.Scrollbar(second_frame, orient="vertical", command=second_pass_text.yview)
second_scroll.pack(side="right", fill="y")
second_pass_text.config(yscrollcommand=second_scroll.set)

copy_second_button = ttk.Button(window, text="Copy 2nd Pass", command=copy_second)
copy_second_button.pack(pady=2)

# === INSTRUCTIONS ===
instructions = ttk.Label(window, text="1. Enter the number of pages\n2. Click 'Calculate'\n3. Copy the result to your print dialog", 
                         font=("Arial", 9), foreground="gray", justify="center")
instructions.pack(pady=10)

# === RUN APPLICATION ===
if __name__ == "__main__":
    window.mainloop()
