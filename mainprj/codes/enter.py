import tkinter as tk
import mysql.connector
from tkinter import PhotoImage
import os

mydb=mysql.connector.connect(host="localhost",username="root",password="",database="clg")
mycursor=mydb.cursor()

root=tk.Tk()
root.title("Admin")
root.geometry("550x400")


image_path=PhotoImage(file=r"D:\python\mainprj\codes\e.png")
bg_image=tk.Label(root,image=image_path)
bg_image.place(x=1,y=1)

def next_page1():
    root.destroy()
    import admindetail

def next_page2():
    root.destroy()
    import admissiondetail

def next_page3():
    root.destroy()
    import facultydetail

def next_page4():
    root.destroy()
    import librarydetail

l1=tk.Label(text="WARM WELCOME",foreground="red",font="elephant 15 bold",background="white")
l1.place(x=180,y=30)

b1=tk.Button(text="ADMIN",command=next_page1,foreground="white",font="elephant 15 bold",background="royal blue",border=5)
b1.place(x=20,y=80)

b2=tk.Button(text="ADMISSION",command=next_page2,foreground="white",font="elephant 15 bold",background="royal blue",border=5)
b2.place(x=60,y=160)

b3=tk.Button(text="FACULTY",command=next_page3,foreground="white",font="elephant 15 bold",background="royal blue",border=5)
b3.place(x=380,y=80)

b4=tk.Button(text="LIBRARY",command=next_page4,foreground="white",font="elephant 15 bold",background="royal blue",border=5)
b4.place(x=340,y=160)

l2 = tk.Label(text="LESS THINKING\nMORE CREATING", foreground="maroon", font="elephant 15 bold", background="white")
l2.place(x=150,y=250)

root.mainloop()
