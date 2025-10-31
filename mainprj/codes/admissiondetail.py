import tkinter as tk
import mysql.connector
from tkinter import PhotoImage

mydb=mysql.connector.connect(host="localhost",username="root",password="",database="clg")
mycursor=mydb.cursor()

root=tk.Tk()
root.title("admission")
root.geometry("550x550")

image_path=PhotoImage(file=r"D:\python\mainprj\codes\admissiondetail pic.png")
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
    t12.delete(0,"end")
    t13.delete(0,"end")
    t14.delete(0,"end")
    t15.delete(0,"end")
    t16.delete(0,"end")

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
        d12=t12.get()
        d13=t13.get()
        d14=t14.get()
        d15=t15.get()
        d16=t16.get()
        val=(d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16)
        sql="insert into admission values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" 
        mycursor.execute(sql,val)
        mydb.commit()

def update():
    d1=int(t1.get())
    d2=t2.get()
    d3=t3.get()
    d4=t4.get()
    d5=t5.get()
    d6=int(t6.get())
    d7=t7.get()
    d8=t8.get()
    d9=t9.get()
    d10=t10.get()
    d11=t11.get()
    d12=t12.get()
    d13=t13.get()
    d14=t14.get()
    d15=t15.get()
    d16=t16.get()
    sql="update admission set s_name=%s,branch=%s,degree=%s,gender=%s,age=%s,dob=%s,adm_date=%s,address=%s,s_mobile=%s,f_name=%s,f_ocp=%s,f_mob=%s,m_name=%s,m_ocp=%s,m_mob=%s where std_id=%s"
    val=(d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16,d1)
    mycursor.execute(sql,val)
    mydb.commit()

def delete():
    d1=int(t1.get())
    val=(d1,)
    sql="delete from admission where std_id=%s"
    mycursor.execute(sql,val)
    mydb.commit()

def view():
    d1=int(t1.get())
    val=(d1,)
    sql="select*from admission where std_id=%s"
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
        t12.insert(0,x[11])
        t13.insert(0,x[12])
        t14.insert(0,x[13])
        t15.insert(0,x[14])
        t16.insert(0,x[15])

def back():
    root.destroy()
    import enter

l0=tk.Label(text="ADMISSION",foreground="red",font="elephant 12 bold")
l0.place(x=200,y=3)

l1=tk.Label(text="Student_id:",font="times 10",foreground="blue")
l1.place(x=40,y=40)
t1=tk.Entry()
t1.place(x=120,y=40)

l2=tk.Label(text="S_Name:",font="times 10",foreground="blue")
l2.place(x=40,y=90)
t2=tk.Entry()
t2.place(x=120,y=90)

l3=tk.Label(text="Branch:",font="times 10",foreground="blue")
l3.place(x=40,y=140)
t3=tk.Entry()
t3.place(x=120,y=140)

l4=tk.Label(text="Degree:",font="times 10",foreground="blue")
l4.place(x=40,y=190)
t4=tk.Entry()
t4.place(x=120,y=190)

l5=tk.Label(text="Gender:",font="times 10",foreground="blue")
l5.place(x=40,y=240)
t5=tk.Entry()
t5.place(x=120,y=240)

l6=tk.Label(text="Age:",font="times 10",foreground="blue")
l6.place(x=40,y=290)
t6=tk.Entry()
t6.place(x=120,y=290)

l7=tk.Label(text="DOB:",font="times 10",foreground="blue")
l7.place(x=40,y=340)
t7=tk.Entry()
t7.place(x=120,y=340)

l8=tk.Label(text="Adm_Date:",font="times 10",foreground="blue")
l8.place(x=40,y=390)
t8=tk.Entry()
t8.place(x=120,y=390)

l9=tk.Label(text="Address:",font="times 10",foreground="blue")
l9.place(x=300,y=40)
t9=tk.Entry()
t9.place(x=390,y=40)

l10=tk.Label(text="S_Mobile:",font="times 10",foreground="blue")
l10.place(x=300,y=90)
t10=tk.Entry()
t10.place(x=390,y=90)

l11=tk.Label(text="Fathername:",font="times 10",foreground="blue")
l11.place(x=300,y=140)
t11=tk.Entry()
t11.place(x=390,y=140)

l12=tk.Label(text="F_Occupation:",font="times 10",foreground="blue")
l12.place(x=300,y=190)
t12=tk.Entry()
t12.place(x=390,y=190)

l13=tk.Label(text="F_Mobile:",font="times 10",foreground="blue")
l13.place(x=300,y=240)
t13=tk.Entry()
t13.place(x=390,y=240)

l14=tk.Label(text="Mothername:",font="times 10",foreground="blue")
l14.place(x=300,y=290)
t14=tk.Entry()
t14.place(x=390,y=290)

l15=tk.Label(text="M_Occupation:",font="times 10",foreground="blue")
l15.place(x=300,y=340)
t15=tk.Entry()
t15.place(x=390,y=340)

l16=tk.Label(text="M_Mobile:",font="times 10",foreground="blue")
l16.place(x=300,y=390)
t16=tk.Entry()
t16.place(x=390,y=390)

b1=tk.Button(text="CLEAR",command=refresh,foreground="red",background="light yellow")
b1.place(x=90,y=440,width=80)

b2=tk.Button(text="SAVE",command=save,foreground="red",background="light yellow")
b2.place(x=240,y=440,width=80)


b3=tk.Button(text="QUIT",command=exit,foreground="red",background="light yellow")
b3.place(x=360,y=440,width=80)

b4=tk.Button(text="UPDATE",command=update,foreground="red",background="light yellow")
b4.place(x=90,y=490,width=80)

b5=tk.Button(text="DELETE",command=delete,foreground="red",background="light yellow")
b5.place(x=240,y=490,width=80)

b6=tk.Button(text="VIEW",command=view,foreground="red",background="light yellow")
b6.place(x=360,y=490,width=80)

b7=tk.Button(text="X",command=back,foreground="white",background="red")
b7.place(x=520,y=0,width=30)

root.mainloop()