import tkinter as tk
from tkinter import ttk
import google.generativeai as genai
import mysql.connector as mp

connection = mp.connect(host='localhost', database="pysqlone",user="root", password="root")
genai.configure(api_key="AIzaSyDMhYAHLqk1AjmMUQ0Eby5ycLlNDM92x10")
model = genai.GenerativeModel("gemini-1.5-flash")
cursor = connection.cursor()
cursor.execute("USE pysqlone;")


def process_text():
    x = str(entry.get())
    response = model.generate_content(x)
    otpt = str(response.text)
    label.configure(text=response.text)
    insert_query = f"INSERT INTO prompthistory VALUES(\"{x}\", \"{otpt}\");"
    cursor.execute(str(insert_query))
    connection.commit()

root = tk.Tk()
root.title("Text Processing Dialog")
root.geometry("300x200")

frame = ttk.Frame(root, padding=(10, 10))
frame.pack()

entry = ttk.Entry(frame, width=30)
entry.pack(pady=10)

button = ttk.Button(frame, text="Use Gen AI", command=process_text)
button.pack(pady=10)

cbtt = ttk.Button(frame, text="Close Window", command=root.destroy)
cbtt.pack(pady=10)

label = ttk.Label(frame, text="")
label.pack(pady=10)

root.mainloop()