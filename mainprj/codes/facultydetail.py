import tkinter as tk
import mysql.connector
from tkinter import PhotoImage

mydb=mysql.connector.connect(host="localhost",username="root",password="",database="clg")
mycursor=mydb.cursor()

root=tk.Tk()
root.title("faculty")
root.geometry("300x700")

image_path=PhotoImage(file=r"D:\python\mainprj\codes\facultydetail fig.png")
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
    t10.delete(0,"end")
    t11.delete(0,"end")
   
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
        d10=t10.get()
        d11=t11.get()
        val=(d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11)
        sql="insert into faculty values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" 
        mycursor.execute(sql,val)
        mydb.commit()

def update():
    d1=int(t1.get())
    d2=t2.get()
    d3=t3.get()
    d4=t4.get()
    d5=t5.get()
    d6=t6.get()
    d7=t7.get()
    d8=t8.get()
    d9=t9.get()
    d10=t10.get()
    d11=t11.get()
    val=(d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d1)
    sql="update faculty set fac_name=%s,branch=%s,gender=%s,age=%s,dob=%s,join_date=%s,qualf=%s,exp=%s,address=%s,fac_mob=%s where fac_id=%s"
    mycursor.execute(sql,val)
    mydb.commit()

def delete():
    d1=int(t1.get())
    val=(d1,)
    sql="delete from faculty where fac_id=%s"
    mycursor.execute(sql,val)
    mydb.commit()

def view():
    d1=int(t1.get())
    val=(d1,)
    sql="select*from faculty where fac_id=%s"
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
        t10.insert(0,x[9])
        t11.insert(0,x[10])

def back():
    root.destroy()
    import enter
    
l0=tk.Label(text="FACULTY",foreground="red",font="elephant 12 bold")
l0.place(x=100,y=3)

l1=tk.Label(text="Faculty_Id:",font="times 10",foreground="blue")
l1.place(x=40,y=40)
t1=tk.Entry()
t1.place(x=120,y=40)

l2=tk.Label(text="Fac_Name:",font="times 10",foreground="blue")
l2.place(x=40,y=90)
t2=tk.Entry()
t2.place(x=120,y=90)

l3=tk.Label(text="Branch:",font="times 10",foreground="blue")
l3.place(x=40,y=140)
t3=tk.Entry()
t3.place(x=120,y=140)

l4=tk.Label(text="Gender:",font="times 10",foreground="blue")
l4.place(x=40,y=190)
t4=tk.Entry()
t4.place(x=120,y=190)

l5=tk.Label(text="Age:",font="times 10",foreground="blue")
l5.place(x=40,y=240)
t5=tk.Entry()
t5.place(x=120,y=240)

l6=tk.Label(text="DOB:",font="times 10",foreground="blue")
l6.place(x=40,y=290)
t6=tk.Entry()
t6.place(x=120,y=290)

l7=tk.Label(text="Join_Date:",font="times 10",foreground="blue")
l7.place(x=40,y=340)
t7=tk.Entry()
t7.place(x=120,y=340)

l8=tk.Label(text="Qualification:",font="times 10",foreground="blue")
l8.place(x=40,y=390)
t8=tk.Entry()
t8.place(x=120,y=390)

l9=tk.Label(text="Experience:",font="times 10",foreground="blue")
l9.place(x=40,y=440)
t9=tk.Entry()
t9.place(x=120,y=440)

l10=tk.Label(text="Address:",font="times 10",foreground="blue")
l10.place(x=40,y=490)
t10=tk.Entry()
t10.place(x=120,y=490)

l11=tk.Label(text="Fac_Mobile:",font="times 10",foreground="blue")
l11.place(x=40,y=540)
t11=tk.Entry()
t11.place(x=120,y=540)

b1=tk.Button(text="CLEAR",command=refresh,foreground="red",background="light yellow")
b1.place(x=30,y=590,width=80)

b2=tk.Button(text="SUBMIT",command=save,foreground="red",background="light yellow")
b2.place(x=110,y=590,width=80)

b3=tk.Button(text="QUIT",command=exit,foreground="red",background="light yellow")
b3.place(x=190,y=590,width=80)

b4=tk.Button(text="UPDATE",command=update,foreground="red",background="light yellow")
b4.place(x=30,y=640,width=80)

b5=tk.Button(text="DELETE",command=delete,foreground="red",background="light yellow")
b5.place(x=110,y=640,width=80)

b6=tk.Button(text="VIEW",command=view,foreground="red",background="light yellow")
b6.place(x=190,y=640,width=80)

b5=tk.Button(text="X",command=back,foreground="white",background="red")
b5.place(x=270,y=0,width=30)

root.mainloop()