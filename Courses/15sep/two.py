import tkinter as tk
from tkinter import ttk

def process_text(text):
    # Replace this with your actual text processing logic
    result = text.upper()
    label.config(text=result)

root = tk.Tk()
root.title("Text Processing Dialog")
root.geometry("300x200")

# Create a frame for the widgets
frame = ttk.Frame(root, padding=(10, 10))
frame.pack()

# Create the text entry field
entry = ttk.Entry(frame, width=30)
entry.pack(pady=10)

# Create the button
button = ttk.Button(frame, text="Process Text", command=lambda: process_text(entry.get()))
button.pack(pady=10)

# Create the label for displaying output
label = ttk.Label(frame, text="")
label.pack(pady=10)

root.mainloop()