from tkinter import *
from tkinter import messagebox

def login():
    username=entry1.get()
    password=entry2.get()
    if (username=='' and password==''):
        messagebox.showinfo('','Fill Up The Blanks')
    elif (username=='dorisha' and password=='123'):
        messagebox.showinfo('','Login Successfully Commpleted')
    else:
         messagebox.showinfo('','Invalid Usernae and Password')

root=Tk()
root.title("Admin")
root.geometry("500x400")

global entry1
global entry2

Label(root,text="Username").place(x=20,y=20)
Label(root,text="Password").place(x=20,y=70)

entry1=Entry(root,bd=5)
entry1.place(x=140,y=20)

entry2=Entry(root,bd=5)
entry2.place(x=140,y=70)

button=Button(root,text="login")
button.place(x=300,y=200)

root.mainloop()