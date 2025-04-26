import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="5y7Km@?3uG",
    database="Ace",
    auth_plugin='mysql_native_password'  # Add this line
)
c=conn.cursor()
sid=input("Enter the std ID :")
sname=input("Enter the std name :")
city=input("Enter the std city :")
marks=int(input("Enter the std marks :"))
c.execute("insert into student_table  values (%s,%s,%s,%s)",(sid,sname,city,marks))
conn.commit()
c.close()

conn.close()