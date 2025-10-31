import tkinter as tk
import mysql.connector
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib import style
import numpy as np
import os
"""from datetime import datetime"""

"""mydb=mysql.connector.connect(host="localhost",username="root",password="",database="clg")
mycursor=mydb.cursor()"""

# Set up the connection to MySQL database
def db():
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="clg")
    mycursor = mydb.cursor()
    sql = "SELECT total_copies, copies_left FROM library"
    mycursor.execute(sql)
    resultset = mycursor.fetchall()
    """mydb.close()"""
# Reverse to get chronological order
    resultset.reverse()
    return resultset

# Animation function
def animate(i):
    data=db()
    x=[row[0] for row in data]
    y=[row[1] for row in data]
    axis.clear()
    axis.plot(x,y, marker='d', linestyle='--', color='blue',markersize=3,linewidth=1)
    plt.title("BOOKS UPDATE",fontsize=14,fontstyle="normal",color="red")
    plt.xlabel("TOTAL COPIES",fontsize=12,fontstyle="oblique",color="red")
    plt.ylabel("COPIES LEFT",fontsize=12,fontstyle="oblique",color="red")
    plt.plot(x,y)

# Set up plot
fig, axis = plt.subplots()
ani = animation.FuncAnimation(fig, animate, interval=2000)  # updates every 2 seconds

def connect():
    os.system("python enter.py")

b1=tk.Button(text="X",command=connect,foreground="white",background="red")
b1.place(x=770,y=0,width=30)

plt.show()



