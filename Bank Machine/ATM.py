import os
import time
from BankAccount import BankAccount

bank_accounts = [BankAccount("jsmith","1452",156.21), BankAccount("aobrien","9892",856.21), 
                 BankAccount("hpotter","6001",43.50), BankAccount("hgranger","6993")]

print("\nATM Interface\n")
principal_menu = list()
principal_menu.append("1. Enter your pin number")
principal_menu.append("2. Exit")

for entry in range(len(principal_menu)):
    print(principal_menu[entry])

option = int(input("\nEnter your option: "))

if option == 1:

    os.system('cls')
    print("\nATM Interface\n")
    customer_pin = input("Enter your  pin number: ")

    while True:

        flag = 0

        for bank_account in bank_accounts:

            if customer_pin == BankAccount.get_pin(bank_account):

                secondary_menu = list()
                secondary_menu.append("1. Withdraw")
                secondary_menu.append("2. Deposit")
                secondary_menu.append("3. Check Balance")
                secondary_menu.append("4. Check Overdraft Status")
                secondary_menu.append("5. Exit")

                while True:

                    os.system('cls')

                    for entry in range(len(secondary_menu)):
                        print(secondary_menu[entry])

                    option = int(input("\nPlease select your option: "))

                    if option == 1:

                        os.system('cls')
                        amount = input("Register the amount which you want to withdraw (EUR): ")
                        os.system('cls')
                        print(BankAccount.withdraw(bank_account, float(amount)))
                        print("\nYou will be redirected to the main menu automatically.")
                        time.sleep(3)

                    elif option == 2:

                        os.system('cls')
                        amount = input("Register the amount which you want to deposit (EUR): ")
                        os.system('cls')
                        print(BankAccount.deposit(bank_account, float(amount)))
                        print("\nYou will be redirected to the main menu automatically.")
                        time.sleep(3)

                    elif option == 3:
                        
                        os.system('cls')
                        balance = BankAccount.get_balance(bank_account)
                        print("Account Balance\n")
                        print("Your balance is: EUR", round(balance,2))
                        print("\nYou will be redirected to the main menu automatically.")
                        time.sleep(5)

                    elif option == 4:

                        os.system('cls')
                        overdraft_status = BankAccount.get_overdraft_status(bank_account)
                        print("Overdraft Status\n")
                        print("Your overdraft status is:", overdraft_status)
                        print("\nYou will be redirected to the main menu automatically.")
                        time.sleep(5)
                        
                    elif option == 5:
                        flag = 1
                        break
                    else:
                        os.system('cls')
                        print("Unknown option selected! You will be redirected to the main menu...\n")
                        time.sleep(3)
        
        os.system('cls')

        if flag == 1:
            print("\nATM Interface\n")
            for entry in range(len(principal_menu)):
                print(principal_menu[entry])
            option = int(input("\nEnter your option: "))
            
            if option == 1:
                os.system('cls')
                customer_pin = input("Enter your pin number: ")
            else:
                exit(True)
        else:
            print("Customer does not exist in the system.")
            customer_pin = input("\nPlease insert the correct number pin: ")

else:
    exit(True)