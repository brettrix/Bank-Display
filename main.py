#Author: Brett Rix

from functions import BankAccount
from functions import display_menu

#The customer should be able to:
#1. Make a deposit
#2. Make a withdrawal
#3. View account information
#4. Quit

print("Welcome to Rix Bank.")
print()
print("Please enter your name:")

customer_name = input()
account1 = BankAccount(customer_name)

print()
menu_choice = display_menu().upper()

while menu_choice not in ["4", "4.", "QUIT", "4. QUIT"]:
    if menu_choice in ["1", "1.", "MAKE A DEPOSIT", "DEPOSIT", "1. MAKE A DEPOSIT"]:
        print()
        account1.deposit()
    elif menu_choice in ["2", "2.", "MAKE A WITHDRAWAL", "WITHDRAW", "WITHDRAWAL", "2. MAKE A WITHDRAWAL"]:
        print()
        account1.withdrawal()
    elif menu_choice in ["3", "3.", "VIEW ACCOUNT INFORMATION", "ACCOUNT INFORMATION", "INFO", "INFORMATION", "3. VIEW ACCOUNT INFORMATION"]:
        print()
        account1.information()
    else:
        print("Please enter a valid choice.")
    print()
    menu_choice = display_menu().upper()

print(f"Thank you for your business, {account1.name}!")