import tkinter as tk
from tkinter import messagebox
from db import conn, cursor


def login():
    account_no = entry_account.get()
    pin = entry_pin.get()

    if account_no == "" or pin == "":
        messagebox.showwarning("Warning", "Please enter Account Number and PIN")
        return

    cursor.execute(
        "SELECT account_no, name, age, phone, address, balance "
        "FROM customers WHERE account_no=%s AND pin=%s",
        (account_no, pin)
    )

    result = cursor.fetchone()

    if result:
        messagebox.showinfo("Login", "Login Successful!")

        details = tk.Toplevel(root)
        details.title("Account Details")
        details.geometry("400x400")

        tk.Label(
            details,
            text="ACCOUNT DETAILS",
            font=("Arial", 18, "bold")
        ).pack(pady=20)

        tk.Label(details, text="Account Number: " + str(result[0]),
                 font=("Arial", 12)).pack(pady=5)

        tk.Label(details, text="Name: " + str(result[1]),
                 font=("Arial", 12)).pack(pady=5)

        tk.Label(details, text="Age: " + str(result[2]),
                 font=("Arial", 12)).pack(pady=5)

        tk.Label(details, text="Phone: " + str(result[3]),
                 font=("Arial", 12)).pack(pady=5)

        tk.Label(details, text="City/Address: " + str(result[4]),
                 font=("Arial", 12)).pack(pady=5)

        tk.Label(details, text="Balance: ₹" + str(result[5]),
                 font=("Arial", 12, "bold")).pack(pady=10)

    else:
        messagebox.showerror(
            "Login Failed",
            "Invalid Account Number or PIN"
        )


# Main window
root = tk.Tk()
root.title("Bank Management System")
root.geometry("450x350")

tk.Label(
    root,
    text="BANK MANAGEMENT SYSTEM",
    font=("Arial", 18, "bold")
).pack(pady=30)

tk.Label(root, text="Account Number").pack()

entry_account = tk.Entry(root, width=30)
entry_account.pack(pady=5)

tk.Label(root, text="PIN").pack(pady=5)

entry_pin = tk.Entry(root, width=30, show="*")
entry_pin.pack(pady=5)

tk.Button(
    root,
    text="LOGIN",
    width=15,
    command=login
).pack(pady=25)

root.mainloop()
