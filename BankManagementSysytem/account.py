from db import conn, cursor

def create_account():
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    phone = input("Enter Phone Number: ")
    address = input("Enter Address: ")
    pin = input("Create 4-digit PIN: ")
    balance = float(input("Enter Initial Balance: "))

    sql = """INSERT INTO customers
             (name, age, phone, address, pin, balance)
             VALUES (%s, %s, %s, %s, %s, %s)"""

    values = (name, age, phone, address, pin, balance)

    cursor.execute(sql, values)
    conn.commit()

    print("Account Created Successfully!")
    print("Your Account Number:", cursor.lastrowid)
