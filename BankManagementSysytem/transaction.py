from db import conn, cursor
from decimal import Decimal
def check_balance():
    account_no = int(input("Enter Account Number: "))

    cursor.execute(
        "SELECT name, balance FROM customers WHERE account_no=%s",
        (account_no,)
    )

    result = cursor.fetchone()

    if result:
        print("\n----- Account Details -----")
        print("Name:", result[0])
        print("Current Balance:", result[1])
    else:
        print("Account Not Found!")
def deposit():
    account_no = int(input("Enter Account Number: "))
    amount = Decimal(input("Enter Deposit Amount: "))

    # Check if account exists
    cursor.execute("SELECT balance FROM customers WHERE account_no = %s", (account_no,))
    result = cursor.fetchone()

    if result:
        new_balance = result[0] + amount

        # Update balance
        cursor.execute(
            "UPDATE customers SET balance = %s WHERE account_no = %s",
            (new_balance, account_no)
        )

        # Save transaction
        cursor.execute(
            "INSERT INTO transaction (account_no, transaction_type, amount) VALUES (%s, %s, %s)",
            (account_no, "Deposit", amount)
        )

        conn.commit()
        print("Amount Deposited Successfully!")
        print("Updated Balance:", new_balance)

    else:
        print("Account not found!")


def withdraw():
    account_no = int(input("Enter Account Number: "))
    amount = Decimal(input("Enter Withdraw Amount: "))

    cursor.execute(
        "SELECT balance FROM customers WHERE account_no=%s",
        (account_no,)
    )
    result = cursor.fetchone()

    if result:
        balance = result[0]

        if balance >= amount:
            new_balance = balance - amount

            cursor.execute(
                "UPDATE customers SET balance=%s WHERE account_no=%s",
                (new_balance, account_no)
            )

            cursor.execute(
                "INSERT INTO transaction(account_no, transaction_type, amount) VALUES(%s,%s,%s)",
                (account_no, "Withdraw", amount)
            )

            conn.commit()

            print("Amount Withdrawn Successfully!")
            print("Updated Balance:", new_balance)

        else:
            print("Insufficient Balance!")

    else:
        print("Account Not Found! ")

def transaction_history():
    account_no = int(input("Enter Account Number: "))

    cursor.execute(
        "SELECT transaction_type, amount FROM transaction WHERE account_no=%s",
        (account_no,)
    )

    result = cursor.fetchall()

    if result:
        print("\n----- Transaction History -----")
        for row in result:
            print("Type:", row[0], "| Amount:", row[1])
    else:
        print("No Transactions Found!")
        
def delete_account():
    account_no = int(input("Enter Account Number to Delete: "))

    cursor.execute(
        "SELECT name FROM customers WHERE account_no=%s",
        (account_no,)
    )

    result = cursor.fetchone()

    if result:
        print("Account Holder Name:", result[0])

        confirm = input("Are you sure you want to delete this account? (yes/no): ")

        if confirm.lower() == "yes":
            cursor.execute(
                "DELETE FROM transaction WHERE account_no=%s",
                (account_no,)
            )

            cursor.execute(
                "DELETE FROM customers WHERE account_no=%s",
                (account_no,)
            )

            conn.commit()
            print("Account Deleted Successfully!")

        else:
            print("Deletion Cancelled.")

    else:
        print("Account Not Found!")


def update_customer():
    account_no = int(input("Enter Account Number: "))

    cursor.execute(
        "SELECT name, phone, address FROM customers WHERE account_no=%s",
        (account_no,)
    )
    result = cursor.fetchone()

    if result:
        print("\nCurrent Details")
        print("Name    :", result[0])
        print("Phone   :", result[1])
        print("Address :", result[2])

        name = input("Enter New Name: ")
        phone = input("Enter New Phone Number: ")
        address = input("Enter New Address: ")

        cursor.execute(
            "UPDATE customers SET name=%s, phone=%s, address=%s WHERE account_no=%s",
            (name, phone, address, account_no)
        )

        conn.commit()
        print("Customer Details Updated Successfully!")

    else:
        print("Account Not Found!")

def change_pin():
    account_no = int(input("Enter Account Number: "))

    old_pin = input("Enter Old PIN: ")

    cursor.execute(
        "SELECT pin FROM customers WHERE account_no=%s",
        (account_no,)
    )

    result = cursor.fetchone()

    if result:
        if result[0] == old_pin:

            new_pin = input("Enter New 4-digit PIN: ")
            confirm_pin = input("Confirm New PIN: ")

            if new_pin == confirm_pin:

                cursor.execute(
                    "UPDATE customers SET pin=%s WHERE account_no=%s",
                    (new_pin, account_no)
                )

                conn.commit()
                print("PIN")

from decimal import Decimal

def transfer_money():
    sender = int(input("Enter Sender Account Number: "))
    receiver = int(input("Enter Receiver Account Number: "))
    amount = Decimal(input("Enter Transfer Amount: "))

    # Check sender
    cursor.execute(
        "SELECT balance FROM customers WHERE account_no=%s",
        (sender,)
    )
    sender_data = cursor.fetchone()

    # Check receiver
    cursor.execute(
        "SELECT balance FROM customers WHERE account_no=%s",
        (receiver,)
    )
    receiver_data = cursor.fetchone()

    if sender_data and receiver_data:

        sender_balance = sender_data[0]
        receiver_balance = receiver_data[0]

        if sender_balance >= amount:

            new_sender_balance = sender_balance - amount
            new_receiver_balance = receiver_balance + amount

            # Update sender balance
            cursor.execute(
                "UPDATE customers SET balance=%s WHERE account_no=%s",
                (new_sender_balance, sender)
            )

            # Update receiver balance
            cursor.execute(
                "UPDATE customers SET balance=%s WHERE account_no=%s",
                (new_receiver_balance, receiver)
            )

            # Record sender transaction
            cursor.execute(
                "INSERT INTO transaction(account_no, transaction_type, amount) VALUES(%s,%s,%s)",
                (sender, "Transfer Sent", amount)
            )

            # Record receiver transaction
            cursor.execute(
                "INSERT INTO transaction(account_no, transaction_type, amount) VALUES(%s,%s,%s)",
                (receiver, "Transfer Received", amount)
            )

            conn.commit()
            print("Money Transferred Successfully!")

        else:
            print("Insufficient Balance!")

    else:
        print("Invalid Account Number!")
def login():
    account_no = int(input("Enter Account Number: "))
    pin = input("Enter PIN: ")

    cursor.execute(
        "SELECT * FROM customers WHERE account_no=%s AND pin=%s",
        (account_no, pin)
    )

    result = cursor.fetchone()

    if result:
        print("\nLogin Successful!")
        return account_no
    else:
        print("\nInvalid Account Number or PIN!")
        return None
