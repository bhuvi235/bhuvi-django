import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="csctnr",
        database="bank"
    )

    cursor = conn.cursor()
    print("Database Connected Successfully!")

except mysql.connector.Error as err:
    print("Error:", err)
