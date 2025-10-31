import mysql.connector
mydb=mysql.connector.connect(host="localhost",username="root",password="")
mycursor=mydb.cursor()
sql="create database clg"
mycursor.execute(sql)
print("db created")
