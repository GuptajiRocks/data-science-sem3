import google.generativeai as genai
from tkinter import ttk
from tkinter import *

genai.configure(api_key="AIzaSyDMhYAHLqk1AjmMUQ0Eby5ycLlNDM92x10")
model = genai.GenerativeModel("gemini-1.5-flash")

root = Tk()

entry1 = Entry(root, width=20)
entry1.pack()

def jesus():
    x = str(entry1.get())
    response = model.generate_content(x)
    label.configure(text=response.text)

btn1 = Button(root, text="Click", command=jesus)
btn1.pack()

btn2 = Button(root, text="Close", command=root.destroy)
btn2.pack()

label = Label(root)
label.pack()

label2 = Label(root)
label.pack()


root.mainloop()




