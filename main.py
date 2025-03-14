import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to generate Pie Chart
def generate_pie_chart(data):
    try:
        data = list(map(float, data))  # Convert input to float
        if any(x < 0 for x in data):
            messagebox.showerror("Error", "Negative values are not allowed!")
            return
        if sum(data) == 0:
            messagebox.showerror("Error", "All values cannot be zero!")
            return
        
        plt.figure(figsize=(6, 6))
        plt.pie(data, labels=[f"Slice {i+1}" for i in range(len(data))], autopct='%1.1f%%', startangle=90)
        plt.title("Pie Chart Representation")
        plt.show()
    except ValueError:
        messagebox.showerror("Error", "Invalid input! Enter numeric values only.")

# Function to generate Histogram
def generate_histogram(data):
    try:
        data = list(map(float, data))  # Convert input to float
        if any(x < 0 for x in data):
            messagebox.showerror("Error", "Negative values are not allowed!")
            return
        
        plt.figure(figsize=(7, 5))
        sns.histplot(data, bins=10, kde=True, color='blue')
        plt.xlabel("Value Range")
        plt.ylabel("Frequency")
        plt.title("Histogram Representation")
        plt.show()
    except ValueError:
        messagebox.showerror("Error", "Invalid input! Enter numeric values only.")

# Function to handle dataset from CSV
def load_csv():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if not file_path:
        return
    
    try:
        df = pd.read_csv(file_path)
        column_selected = column_var.get()
        if column_selected not in df.columns:
            messagebox.showerror("Error", "Selected column not found in CSV!")
            return
        
        data = df[column_selected].dropna().tolist()
        update_input_field(data)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load CSV: {str(e)}")

# Function to update input field with CSV data
def update_input_field(data):
    input_var.set(', '.join(map(str, data)))

# Function to generate chart based on selection
def generate_chart():
    chart_type = chart_var.get()
    data = input_var.get().split(',')
    
    if not data or data == [""]:
        messagebox.showerror("Error", "Please enter data or load from CSV.")
        return

    if chart_type == "Pie Chart":
        generate_pie_chart(data)
    elif chart_type == "Histogram":
        generate_histogram(data)
    else:
        messagebox.showerror("Error", "Please select a chart type.")

# GUI Setup
root = tk.Tk()
root.title("Pie Chart & Histogram Generator")
root.geometry("700x500")

# Load background image
bg_image = Image.open("background.jpg")  # Change this to your background image path
bg_image = bg_image.resize((1600, 800), Image.Resampling.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

# Background Label
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)

# Create a transparent frame in the center
frame = tk.Frame(root, bg="#ffffff", bd=2, relief="ridge")
frame.place(relx=0.5, rely=0.5, anchor="center", width=500, height=350)

# Use an RGBA color (Light Gray with Transparency Effect)
frame.configure(bg="#ffffff", highlightbackground="gray", highlightthickness=1)


# Title
title_label = tk.Label(frame, text="Pie Chart & Histogram Generator", font=("Arial", 14, "bold"), bg="#ffffff", fg="#333333")
title_label.pack(pady=10)

# Chart selection dropdown
chart_var = tk.StringVar()
ttk.Label(frame, text="Select Chart Type:", background="#ffffff").pack(pady=5)
chart_menu = ttk.Combobox(frame, textvariable=chart_var, values=["Pie Chart", "Histogram"], state="readonly")
chart_menu.pack(pady=5)

# Column selection for CSV
column_var = tk.StringVar()
ttk.Label(frame, text="Enter Column Name from CSV:", background="#ffffff").pack(pady=5)
column_entry = ttk.Entry(frame, textvariable=column_var, width=50)
column_entry.pack(pady=5)

# Input field for user data
input_var = tk.StringVar()
ttk.Label(frame, text="Enter Values (comma-separated):", background="#ffffff").pack(pady=5)
input_entry = ttk.Entry(frame, textvariable=input_var, width=50)
input_entry.pack(pady=5)

# Load CSV Button
ttk.Button(frame, text="Load from CSV", command=load_csv).pack(pady=5)

# Generate Button
ttk.Button(frame, text="Generate Chart", command=generate_chart).pack(pady=10)

# Run the GUI
root.mainloop()
