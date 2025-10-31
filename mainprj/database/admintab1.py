import mysql.connector
mydb=mysql.connector.connect(host="localhost",username="root",password="",database="clg")
mycursor=mydb.cursor()
sql="create table admin(user_name varchar(20),dob varchar(20),email varchar(20),address varchar(20),roll varchar(20),Password varchar(20))"
mycursor.execute(sql)
print("table created")