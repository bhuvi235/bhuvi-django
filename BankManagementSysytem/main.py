from account import create_account
from transaction import deposit,withdraw,check_balance,transaction_history,delete_account,update_customer,change_pin,transfer_money,login
while True:
    print("\n" + "=" * 50)
    print("                         BANK MANAGEMENT SYSTEM")
    print("=" * 50)
    print(" 1. Create Account")
    print(" 2. Deposit Money")
    print(" 3. Withdraw Money")
    print(" 4. Check Balance")
    print(" 5. Transaction History")
    print(" 6. Delete Account")
    print(" 7. Update Customer")
    print(" 8. Change PIN")
    print(" 9. Transfer Money")
    print("10. login")
    print("11. Exit")
    print("=" * 50)

    choice = int(input("Enter your choice: "))
   

    if choice == 1:
        create_account()
    elif choice ==2:
        deposit()
    elif choice ==3:
        withdraw()
    elif choice ==4:
        check_balance()
    elif choice ==5:
        transaction_history()
    elif choice ==6:
        delete_account()
    elif choice ==7:
        update_customer()
    elif choice ==8:
        change_pin()
    elif choice ==9:
        transfer_money()
    elif choice==10:
        login()
    elif choice == 11:
        print("Thank you for using Bank Management System!")
        break

    else:
        print("Invalid Choice! Please try again.")
