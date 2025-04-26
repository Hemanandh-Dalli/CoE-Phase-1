import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="5y7Km@?3uG",
    database="Ace",
    auth_plugin='mysql_native_password'  # Add this line
)
c=conn.cursor()

sid=input("Enter your id to delete record from DB")

c.execute("delete from student_table where sid=%s",(sid,))
conn.commit()
c.close()
conn.close()