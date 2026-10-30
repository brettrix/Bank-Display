
import random

class BankAccount:
    def __init__(self, name): #Constructor
        self.name = name
        self.balance = 0.0
        self.number = random.randint(1000000, 9999999)

    def deposit(self):
        print("How much would you like to DEPOSIT?")
        print('(Pressed the wrong button? Type "menu".)')
        got_deposit_amount = False
        back_menu = False
        while got_deposit_amount == False and back_menu == False:
            try: #Need to make sure we receive a float or integer.
                typed_input = input().upper()
                if typed_input == "MENU": #This 'if' is for when you type 'menu'. Exits the deposit screen and goes back to menu.
                    back_menu = True
                    break
                amount_parts = str(float(typed_input)).split(".")
                #The line above makes sure you have a float instead of an integer (so you have a decimal for sure) and then preps it for truncation by turning it into string.
                decimal_part = amount_parts[1] #Lines 23-25 cut off any decimals past two places (i.e. 9.997 becomes 9.99)
                decimal_part = decimal_part[0:2]
                deposit_amount = float(f"{amount_parts[0]}.{decimal_part}")
                if deposit_amount > 0:
                    got_deposit_amount = True
                else:
                    forced_error = float("error") 
                    #lol this one is just my inexperience. AI says use 'raise ValueError', 
                    #but I think this is funny. Does the same thing, though, so the except
                    #will handle the print text and reset and I don't have to type it again.
            except (ValueError, IndexError): #index error covers for scientific notation and nan/inf
                print()
                print("Please enter a valid amount.")
                print()
                print("How much would you like to DEPOSIT?")
                print('(Pressed the wrong button? Type "menu".)')
        
        if got_deposit_amount == True: #this is here in case they type 'menu' and skip the deposit loop
            print()
            print(f"Successfully deposited ${deposit_amount:,.2f} into your account.")
            self.balance += deposit_amount
            print("Press enter to return to menu.")
            input() #I like this here to let them see it as long as they want

    def withdrawal(self):
        print("How much would you like to WITHDRAW?")
        print('(Pressed the wrong button? Type "menu".)')
        got_withdraw_amount = False
        back_menu = False
        while got_withdraw_amount == False and back_menu == False:
            try: #Need to make sure we receive a float or integer.
                typed_input = input().upper()
                if typed_input == "MENU": #This 'if' is for when you type 'menu'. Exits the withdrawal screen and goes back to menu.
                    back_menu = True
                    break
                amount_parts = str(float(typed_input)).split(".")
                #The line above makes sure you have a float instead of an integer (so you have a decimal for sure) and then preps it for truncation by turning it into string.
                decimal_part = amount_parts[1] #Lines 60-62 cut off any decimals past two places (i.e. 9.997 becomes 9.99)
                decimal_part = decimal_part[0:2]
                withdrawal_amount = float(f"{amount_parts[0]}.{decimal_part}")
                if withdrawal_amount <= self.balance and withdrawal_amount > 0:
                    got_withdraw_amount = True
                elif withdrawal_amount > self.balance: #insufficient funds vs invalid entry (negative numbers)
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
            except (ValueError, IndexError): #index error covers for scientific notation and nan/inf
                print()
                print("Please enter a valid amount.")
                print()
                print("How much would you like to WITHDRAW?")
                print('(Pressed the wrong button? Type "menu".)')
        
        if got_withdraw_amount == True: #this is here in case they type 'menu' and skip the withdrawal loop
            print()
            print(f"Successfully withdrew ${withdrawal_amount:,.2f} from your account.")
            self.balance -= withdrawal_amount
            print("Press enter to return to menu.")
            input()#I like this here to let them see it as long as they want
    
    def information(self):
        print(f"Name:       {self.name}")
        print(f"Account #:  {self.number}")
        print(f"Balance:    ${self.balance:,.2f}")
        print()
        print("Press enter to return to menu.")
        input()#I like this here to let them see it as long as they want

def display_menu(): #menu is shown repeatedly, so function used here
    print("Please choose an option:")
    print()
    print("1. Make a deposit")
    print("2. Make a withdrawal")
    print("3. View account information")
    print("4. Quit")
    print()
    menu_choice = input()

    return menu_choice
