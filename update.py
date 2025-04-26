import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="5y7Km@?3uG",
    database="Ace",
    auth_plugin='mysql_native_password'  # Add this line
)
c=conn.cursor()
sid=input("Enter your id to update marks:")
marks=input("Enter your Updated marks:")

c.execute("update student_table set marks=%s where sid=%s",(marks,sid))

conn.commit()
c.close()
conn.close()b
