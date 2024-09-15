import tkinter as tk
from tkinter import ttk
import google.generativeai as genai

genai.configure(api_key="AIzaSyDMhYAHLqk1AjmMUQ0Eby5ycLlNDM92x10")
model = genai.GenerativeModel("gemini-1.5-flash")

def process_text():
    x = str(entry.get())
    response = model.generate_content(x)
    label.configure(text=response.text)

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
button = ttk.Button(frame, text="Process Text", command=process_text)
button.pack(pady=10)

# Create the label for displaying output
label = ttk.Label(frame, text="")
label.pack(pady=10)

root.mainloop()