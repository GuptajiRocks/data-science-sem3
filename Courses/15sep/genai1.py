import google.generativeai as genai
from tkinter import ttk
from tkinter import *

genai.configure(api_key="AIzaSyDMhYAHLqk1AjmMUQ0Eby5ycLlNDM92x10")
model = genai.GenerativeModel("gemini-1.5-flash")
#response = model.generate_content("Write a story about a magic backpack.")
#print(response.text)


root = Tk()

entry1 = Entry(root, width=20)
entry1.pack()

def jesus():
    x = str(entry1.get())
    response = model.generate_content(x)
    label.configure(text=response.text)

btn1 = Button(root, text="Click", command=jesus)
btn1.pack()

label = Label(root)
label.pack()


root.mainloop()




