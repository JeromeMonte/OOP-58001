import tkinter
from tkinter import*
from tkinter import ttk
window = Tk()

window.geometry("400x230+10+20")
window.title("Midterm in OOP")

str1 = StringVar()
str2 = StringVar()

def upd():
    str2.set(str1.get())

label = Label(window, text = "Enter your fullname : ", fg = "Red")
label.place(x=45, y=65)

txtfld1 = Entry(window, bd = 5, textvariable=str1)
txtfld1.place(x=235, y=65)

button = Button(window, text = "Click to display your fullname", fg = "red", command=lambda:upd())
button.place(x=45, y=105)

txtfld2 = Entry(window, bd = 5, textvariable=str2)
txtfld2.place(x=235, y=105)


window.mainloop()
