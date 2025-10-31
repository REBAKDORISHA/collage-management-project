import mysql.connector
mydb=mysql.connector.connect(host="localhost",username="root",password="",database="clg")
mycursor=mydb.cursor()
sql="create table admission(std_id int(20),s_name varchar(20),branch varchar(20),degree varchar(20),gender varchar(20),age int(20),dob varchar(20),adm_date varchar(20),address varchar(20),s_mobile varchar(20),f_name varchar(20),f_ocp varchar(20),f_mob varchar(20),m_name varchar(20),m_ocp varchar(20),m_mob varchar(20))"
mycursor.execute(sql)
print("table created")
