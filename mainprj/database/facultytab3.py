import mysql.connector
mydb=mysql.connector.connect(host="localhost",username="root",password="",database="clg")
mycursor=mydb.cursor()
sql="create table faculty(fac_id int(20),fac_name varchar(20),branch varchar(20),gender varchar(20),age int(20),dob varchar(20),join_date varchar(20),qualf varchar(20),exp varchar(20),address varchar(20),fac_mob varchar(20))"
mycursor.execute(sql)
print("table created")