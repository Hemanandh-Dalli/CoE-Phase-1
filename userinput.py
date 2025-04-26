import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="5y7Km@?3uG",
    database="Ace",
    auth_plugin='mysql_native_password'  # Add this line
)
print("Database connection established")
conn.close() 