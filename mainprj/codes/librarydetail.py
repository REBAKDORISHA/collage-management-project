import tkinter as tk
import mysql.connector
from tkinter import PhotoImage
import os

mydb=mysql.connector.connect(host="localhost",username="root",password="",database="clg")
mycursor=mydb.cursor()

root=tk.Tk()
root.title("library")
root.geometry("800x250")


image_path=PhotoImage(file=r"D:\python\mainprj\codes\librarydetail fig.png")
bg_image=tk.Label(root,image=image_path)
bg_image.place(x=1,y=1)

def refresh():
    t1.delete(0,"end")
    t2.delete(0,"end")
    t3.delete(0,"end")
    t4.delete(0,"end")
    t5.delete(0,"end")
    t6.delete(0,"end")
    t7.delete(0,"end")
    t8.delete(0,"end")
    t9.delete(0,"end")

def save(): 
    d1=t1.get()
    d2=t2.get()
    d3=t3.get()
    d4=t4.get()
    d5=t5.get()
    d6=t6.get()
    d7=t7.get()
    d8=t8.get()
    d9=t9.get()
    val=(d1,d2,d3,d4,d5,d6,d7,d8,d9)
    sql="insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s)" 
    mycursor.execute(sql,val)
    mydb.commit()

def update():
    d1=int(t1.get())
    d2=t2.get()
    d3=t3.get()
    d4=int(t4.get())
    d5=int(t5.get())
    d6=t6.get()
    d7=t7.get()
    d8=t8.get()
    d9=t9.get()
    sql="update library set std_name=%s,book_title=%s,total_copies=%s,copies_left=%s,final_copies=%s,activation_date=%s,update_date=%s,deactivate_date=%s where std_id=%s"
    val=(d2,d3,d4,d5,d6,d7,d8,d9,d1)
    mycursor.execute(sql,val)
    mydb.commit()

def delete():
    d1=int(t1.get())
    val=(d1,)
    sql="delete from library where std_id=%s"
    mycursor.execute(sql,val)
    mydb.commit()

def view():
    d1=int(t1.get())
    val=(d1,)
    sql="select*from library where std_id=%s"
    mycursor.execute(sql,val)
    resultset=mycursor.fetchall()
    for x in resultset:
        t2.insert(0,x[1])
        t3.insert(0,x[2])
        t4.insert(0,x[3])
        t5.insert(0,x[4])
        t6.insert(0,x[5])
        t7.insert(0,x[6])
        t8.insert(0,x[7])
        t9.insert(0,x[8])

def final_copies():
    n1=int(t4.get())
    n2=int(t5.get())
    final_copies=n1-n2
    t6.insert(0,final_copies)

    n1=int(t4.get())
    n2=int(t5.get())
    if n1>=n2:
        res="less final_copies"
    else:
        res="FINAL_COPIES"

def back():
    root.destroy()
    import enter

def connect():
    os.system("python librarygraph.py")

l0=tk.Label(text="LIBRARY",foreground="red",font="elephant 12 bold")
l0.place(x=360,y=10)

l1=tk.Label(text="Std_Id :",font="times 10",foreground="blue")
l1.place(x=10,y=60)
t1=tk.Entry()
t1.place(x=110,y=60)

l2=tk.Label(text="Std_Name :",font="times 10",foreground="blue")
l2.place(x=270,y=60)
t2=tk.Entry()
t2.place(x=360,y=60)

l3=tk.Label(text="Book_Title :",font="times 10",foreground="blue")
l3.place(x=535,y=60)
t3=tk.Entry()
t3.place(x=655,y=60)

l4=tk.Label(text="Total_Copies :",font="times 10",foreground="blue")
l4.place(x=10,y=100)
t4=tk.Entry()
t4.place(x=110,y=100)

l5=tk.Label(text="Copies_Left :",font="times 10",foreground="blue")
l5.place(x=270,y=100)
t5=tk.Entry()
t5.place(x=360,y=100)

l6=tk.Label(text="FINAL_COPIES :",font="times 10",foreground="blue")
l6.place(x=535,y=100)
t6=tk.Entry()
t6.place(x=655,y=100)

l7=tk.Label(text="Activation_Date :",font="times 10",foreground="blue")
l7.place(x=10,y=140)
t7=tk.Entry()
t7.place(x=110,y=140)

l8=tk.Label(text="Update_Date :",font="times 10",foreground="blue")
l8.place(x=270,y=140)
t8=tk.Entry()
t8.place(x=360,y=140)

l9=tk.Label(text="Deactivate_Date :",font="times 10",foreground="blue")
l9.place(x=535,y=140)
t9=tk.Entry()
t9.place(x=655,y=140)

b1=tk.Button(text="CLEAR",command=refresh,foreground="red",background="light yellow")
b1.place(x=65,y=200,width=80)

b2=tk.Button(text="SUBMIT",command=save,foreground="red",background="light yellow")
b2.place(x=165,y=200,width=80)

b3=tk.Button(text="QUIT",command=exit,foreground="red",background="light yellow")
b3.place(x=265,y=200,width=80)

b4=tk.Button(text="UPDATE",command=update,foreground="red",background="light yellow")
b4.place(x=365,y=200,width=80)

b5=tk.Button(text="DELETE",command=delete,foreground="red",background="light yellow")
b5.place(x=465,y=200,width=80)

b6=tk.Button(text="VIEW",command=view,foreground="red",background="light yellow")
b6.place(x=565,y=200,width=80)

b7=tk.Button(text="FINAL_COPIES",command=final_copies,foreground="red",background="light yellow")
b7.place(x=665,y=200,width=80)

b8=tk.Button(text="X",command=back,foreground="white",background="red")
b8.place(x=780,y=0,width=20)

b9=tk.Button(text="GRAPH",command=connect,foreground="red",background="light yellow")
b9.place(x=365,y=170,width=80)

root.mainloop()
