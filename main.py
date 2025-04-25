import os
import numpy as np
from tkinter import *
from tkinter import filedialog, messagebox
from tkinter.ttk import Progressbar  # Import Progressbar
from PIL import Image, ImageTk
import shutil

# Function to load images
def load_images(input_dir):
    images = []
    for i in range(1, 11):
        path = os.path.join(input_dir, f"image{i}.png")
        img = Image.open(path).convert("L")
        images.append(np.array(img))
    return images

# Function to compute the global average intensity
def compute_global_average(images):
    all_pixels = np.concatenate([img.flatten() for img in images])
    return np.mean(all_pixels)

# Function to normalize an image and return the scaling factor
def normalize_image(img, global_avg):
    current_avg = img.mean()
    if current_avg == 0:
        return np.zeros_like(img, dtype=np.uint8), 0
    factor = global_avg / current_avg
    normalized = np.clip(img * factor, 0, 255).astype(np.uint8)
    return normalized, factor

# Function to save normalized images
def save_images(images, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    for i, img in enumerate(images, 1):
        out_path = os.path.join(output_dir, f"normalized_image{i}.png")
        Image.fromarray(img).save(out_path)

# Function to validate the results
def validate(images, global_avg):
    validation_report = []
    for i, (img, scaling_factor) in enumerate(images, 1):
        avg = img.mean()
        status = "✅" if abs(avg - global_avg) <= 1 else "❌"
        validation_report.append(f"normalized_image{i}.png - Avg: {avg:.2f} - Scaling Factor: {scaling_factor:.4f} - {status}")
    return validation_report

# Function to browse folder for input images
def browse_input_folder():
    input_folder = filedialog.askdirectory()
    if input_folder:
        input_dir_entry.delete(0, END)
        input_dir_entry.insert(0, input_folder)

# Function to browse folder for output images
def browse_output_folder():
    output_folder = filedialog.askdirectory()
    if output_folder:
        output_dir_entry.delete(0, END)
        output_dir_entry.insert(0, output_folder)

# Function to run the normalizer and display results
def run_normalizer():
    input_dir = input_dir_entry.get()
    output_dir = output_dir_entry.get()
    
    if not input_dir or not output_dir:
        messagebox.showerror("Error", "Please select both input and output directories!")
        return
    
    try:
        # Update progress bar
        progress_bar["value"] = 20
        root.update_idletasks()
        
        # Load images
        images = load_images(input_dir)
        
        # Compute global average intensity
        global_avg = compute_global_average(images)
        global_avg_label.config(text=f"Global Average Intensity: {global_avg:.2f}")
        
        # Normalize images
        normalized_images = []
        scaling_factors = []
        for img in images:
            normalized_img, factor = normalize_image(img, global_avg)
            normalized_images.append(normalized_img)
            scaling_factors.append(factor)
            
            # Update progress bar
            progress_bar["value"] += 8
            root.update_idletasks()
        
        # Save the normalized images
        save_images(normalized_images, output_dir)
        
        # Update progress bar
        progress_bar["value"] = 90
        root.update_idletasks()
        
        # Validate results
        validation_report = validate(zip(normalized_images, scaling_factors), global_avg)
        validation_text.config(state=NORMAL)
        validation_text.delete(1.0, END)
        for line in validation_report:
            validation_text.insert(END, line + "\n")
        validation_text.config(state=DISABLED)
        
        # Complete progress
        progress_bar["value"] = 100
        root.update_idletasks()
        
        messagebox.showinfo("Success", "Normalization completed successfully!")
    
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Set up the main GUI window
root = Tk()
root.title("Satellite Image Brightness Normalizer")
root.geometry("600x600")
root.configure(bg="#f4f4f4")

# Use custom font
font = ("Helvetica", 12)

# Title label
title_label = Label(root, text="Satellite Image Brightness Normalizer", font=("Helvetica", 16, "bold"), fg="#4CAF50", bg="#f4f4f4")
title_label.pack(pady=20)

# Create a frame for the input and output directory selection
frame = Frame(root, bg="#f4f4f4")
frame.pack(pady=10)

# Input Directory
input_dir_label = Label(frame, text="Select Input Folder:", font=font, bg="#f4f4f4")
input_dir_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
input_dir_entry = Entry(frame, width=40, font=font)
input_dir_entry.grid(row=0, column=1, padx=10, pady=5)
input_dir_button = Button(frame, text="Browse", font=font, command=browse_input_folder, bg="#4CAF50", fg="white")
input_dir_button.grid(row=0, column=2, padx=10, pady=5)

# Output Directory
output_dir_label = Label(frame, text="Select Output Folder:", font=font, bg="#f4f4f4")
output_dir_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
output_dir_entry = Entry(frame, width=40, font=font)
output_dir_entry.grid(row=1, column=1, padx=10, pady=5)
output_dir_button = Button(frame, text="Browse", font=font, command=browse_output_folder, bg="#4CAF50", fg="white")
output_dir_button.grid(row=1, column=2, padx=10, pady=5)

# Global Average Label
global_avg_label = Label(root, text="Global Average Intensity: Not computed yet", font=font, bg="#f4f4f4")
global_avg_label.pack(pady=20)

# Normalize and Validate Button
normalize_button = Button(root, text="Normalize Images", font=("Helvetica", 14), command=run_normalizer, bg="#FF9800", fg="white")
normalize_button.pack(pady=20)

# Progress Bar
progress_bar = Progressbar(root, orient=HORIZONTAL, length=400, mode="determinate")
progress_bar.pack(pady=20)

# Validation Report
validation_label = Label(root, text="Validation Report:", font=font, bg="#f4f4f4")
validation_label.pack(pady=5)
validation_text = Text(root, width=60, height=10, wrap=WORD, font=font, state=DISABLED)
validation_text.pack(pady=10)

# Run the GUI
root.mainloop()
