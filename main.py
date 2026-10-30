#Author: Brett Rix

from functions import BankAccount
from functions import display_menu

#The customer should be able to:

print("Welcome to Rix Bank.")
print()
print("Please enter your name:")

customer_name = input()
account1 = BankAccount(customer_name)

print()
#Function gets input, since the menu choice will be repeated, turned it into a function
menu_choice = display_menu().upper()

#4. Quit
while menu_choice not in ["4", "4.", "QUIT", "4. QUIT"]:
    #1. Make a deposit
    if menu_choice in ["1", "1.", "MAKE A DEPOSIT", "DEPOSIT", "1. MAKE A DEPOSIT"]:
        print()
        account1.deposit()
    #2. Make a withdrawal
    elif menu_choice in ["2", "2.", "MAKE A WITHDRAWAL", "WITHDRAW", "WITHDRAWAL", "2. MAKE A WITHDRAWAL"]:
        print()
        account1.withdrawal()
    #3. View account information
    elif menu_choice in ["3", "3.", "VIEW ACCOUNT INFORMATION", "ACCOUNT INFORMATION", "INFO", "INFORMATION", "3. VIEW ACCOUNT INFORMATION"]:
        print()
        account1.information()
    else:
        print("Please enter a valid choice.")
    print()
    #see line 16
    menu_choice = display_menu().upper()

print(f"Thank you for your business, {account1.name}!")