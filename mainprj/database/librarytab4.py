import mysql.connector
mydb=mysql.connector.connect(host="localhost",username="root",password="",database="clg")
mycursor=mydb.cursor()
sql="create table library(std_id int(20),std_name varchar(20),book_title varchar(20),total_copies int(20),copies_left int(20),final_copies int(20),activation_date varchar(20),update_date varchar(20),deactivate_date varchar(20))"
mycursor.execute(sql)
print("table created")