
import random

class BankAccount:
    def __init__(self, name):
        self.name = name
        self.balance = 0.0
        self.number = random.randint(1000000, 9999999)

    def deposit(self):
        print("How much would you like to DEPOSIT?")
        print('(Pressed the wrong button? Type "menu".)')
        got_deposit_amount = False
        back_menu = False
        while got_deposit_amount == False and back_menu == False:
            try:
                typed_input = input().upper()
                if typed_input == "MENU":
                    back_menu = True
                    break
                amount_parts = str(float(typed_input)).split(".")
                decimal_part = amount_parts[1]
                decimal_part = decimal_part[0:2]
                deposit_amount = float(f"{amount_parts[0]}.{decimal_part}")
                if deposit_amount > 0:
                    got_deposit_amount = True
                else:
                    forced_error = float("error") 
                    #LOL this one is just my inexperience. AI says use 'raise ValueError', 
                    #but I think this is funny. Does the same thing, though, so the except
                    #will handle the text and reset and I don't have to type it again.
            except ValueError:
                print()
                print("Please enter a valid amount.")
                print("How much would you like to DEPOSIT?")
                print()
                print('(Pressed the wrong button? Type "menu".)')
        
        if got_deposit_amount == True:
            print()
            print(f"Successfully deposited ${deposit_amount:,.2f} into your account.")
            self.balance += deposit_amount
            print("Press enter to return to menu.")
            input()

    def withdrawal(self):
        print("How much would you like to WITHDRAW?")
        print('(Pressed the wrong button? Type "menu".)')
        got_withdraw_amount = False
        back_menu = False
        while got_withdraw_amount == False and back_menu == False:
            try:
                typed_input = input().upper()
                if typed_input == "MENU":
                    back_menu = True
                    break
                amount_parts = str(float(typed_input)).split(".")
                decimal_part = amount_parts[1]
                decimal_part = decimal_part[0:2]
                withdrawal_amount = float(f"{amount_parts[0]}.{decimal_part}")
                if withdrawal_amount <= self.balance and withdrawal_amount > 0:
                    got_withdraw_amount = True
                elif withdrawal_amount > self.balance:
                    print()
                    print(f"Sorry, insufficient funds. You have ${self.balance:,.2f}")
                    print()
                    print("How much would you like to WITHDRAW?")
                    print('(Pressed the wrong button? Type "menu".)')

                else:
                    forced_error = float("error") 
                    #LOL this one is just my inexperience. AI says use 'raise ValueError', 
                    #but I think this is funny. Does the same thing, though, so the except
                    #will handle the text and reset and I don't have to type it again.
            except ValueError:
                print()
                print("Please enter a valid amount.")
                print()
                print("How much would you like to WITHDRAW?")
                print('(Pressed the wrong button? Type "menu".)')
        
        if got_withdraw_amount == True:
            print()
            print(f"Successfully withdrew ${withdrawal_amount:,.2f} from your account.")
            self.balance -= withdrawal_amount
            print("Press enter to return to menu.")
            input()        
    
    def information(self):
        print(f"Name:       {self.name}")
        print(f"Account #:  {self.number}")
        print(f"Balance:    ${self.balance:,.2f}")
        print()
        print("Press enter to return to menu.")
        input()

def display_menu():
    print("Please choose an option:")
    print()
    print("1. Make a deposit")
    print("2. Make a withdrawal")
    print("3. View account information")
    print("4. Quit")
    print()
    menu_choice = input()

    return menu_choice
