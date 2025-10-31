import tkinter as tk
import mysql.connector
from tkinter import messagebox, Label, Entry, Button
from tkinter import PhotoImage

mydb=mysql.connector.connect(host="localhost",username="root",password="",database="clg")
mycursor=mydb.cursor()

root = tk.Tk()
root.title("Admin")
root.geometry("500x350")

image_path=PhotoImage(file=r"D:\python\mainprj\codes\admindetail fig.png")
bg_image=tk.Label(root,image=image_path)
bg_image.place(x=1,y=1)

global t2
global t7

def refresh():
    t2.delete(0,"end")
    t3.delete(0,"end")
    t4.delete(0,"end")
    t5.delete(0,"end")
    t6.delete(0,"end")
    t7.delete(0,"end")
    
def save():
        d2=t2.get()
        d3=t3.get()
        d4=t4.get()
        d5=t5.get()
        d6=t6.get()
        d7=t7.get()
        val=(d2,d3,d4,d5,d6,d7)
        sql="insert into admin values(%s,%s,%s,%s,%s,%s)" 
        mycursor.execute(sql,val)
        mydb.commit()

def login():
    User_Name=t2.get()
    Password=t7.get()
    if (User_Name=='' and Password==''):
        messagebox.showinfo('','Fill Up The Blanks')
    elif (User_Name=='dorisha' and Password=='29'):
        root.destroy()
        import facultydetail
    else:
         messagebox.showinfo('','Invalid Details')

def back():
    root.destroy()
    import enter

l1=tk.Label(text="WELCOME YOU ADMIN",foreground="red",font="elephant 15 bold")
l1.place(x=100,y=30)

l2=tk.Label(text="User_Name :",font="times 10",foreground="blue")
l2.place(x=140,y=90)
t2=tk.Entry()
t2.place(x=220,y=90)

l3=tk.Label(text="DOB :",font="times 10",foreground="blue")
l3.place(x=20,y=140)
t3=tk.Entry()
t3.place(x=90,y=140)

l4=tk.Label(text="Email :",font="times 10",foreground="blue")
l4.place(x=270,y=140)
t4=tk.Entry()
t4.place(x=340,y=140)

l5=tk.Label(text="Address :",font="times 10",foreground="blue")
l5.place(x=20,y=190)
t5=tk.Entry()
t5.place(x=90,y=190,width=375)

l6=tk.Label(text="Role :",font="times 10",foreground="blue")
l6.place(x=20,y=240)
t6=tk.Entry()
t6.place(x=90,y=240)

l7=tk.Label(text="Password :",font="times 10",foreground="blue")
l7.place(x=270,y=240)
t7=tk.Entry()
t7.place(x=340,y=240)

b1=tk.Button(text="CLEAR",command=refresh,foreground="red",background="light yellow")
b1.place(x=30,y=300,width=80)

b2=tk.Button(text="SUBMIT",command=save,foreground="red",background="light yellow")
b2.place(x=150,y=300,width=80)

b3=tk.Button(text="CANCEL",command=exit,foreground="red",background="light yellow")
b3.place(x=260,y=300,width=80)

b4=tk.Button(text="LOGIN",command=login,foreground="red",background="light yellow")
b4.place(x=380,y=300,width=80)

b5=tk.Button(text="X",command=back,foreground="white",background="red")
b5.place(x=480,y=0,width=20)

root.mainloop()