from tkinter import *

window = Tk()
window.title("Final Exam")
window.geometry("380x200+20+10")

def Least():
    L = []
    L.append(eval(conOfent2.get()))
    L.append(eval(conOfent3.get()))
    L.append(eval(conOfent4.get()))
    conOfLeast.set(min(L))

lbl2 = Label(window, text="First number:")
lbl2.grid(row=1, column=0, sticky=W)

conOfent2 = StringVar()
ent2 = Entry(window, bd=2, textvariable=conOfent2)
ent2.grid(row=1, column=1)


lbl3 = Label(window, text="Second number:")
lbl3.grid(row=2, column=0)

conOfent3 = StringVar()
ent3 = Entry(window, bd=2, textvariable=conOfent3)
ent3.grid(row=2, column=1)


lbl4 = Label(window, text="Third number:")
lbl4.grid(row=3, column=0, sticky=W)

conOfent4 = StringVar()
ent4 = Entry(window,bd=2,textvariable=conOfent4)
ent4.grid(row=3, column=1)


btn1 = Button(window, text="Result", command=Least)
btn1.grid(row=4, column=1)

lbl5 = Label(window, text="Result :")
lbl5.grid(row=5, column=0, sticky=W)

conOfLeast = StringVar()
ent5 = Entry(window, bd=2, state="readonly", textvariable=conOfLeast)
ent5.grid(row=5, column=1)

mainloop()