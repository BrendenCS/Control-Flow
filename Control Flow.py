# Programer: Brenden Krueger
# Date: 10-11-2021
# Program: ATM Bank Transaction

"""
This program simulates an ATM utilizing If, Elif, and Else statements.
Nesting If statements and refresh our Comparison & Logical Operators.
"""

print("Welcome to Cash-R-Us Bank\nLet's take a moment to set up your account.\n")

# Set up account by asking users for their fist and last names using Variable.
first_name = input("What is your first name: ")
last_name = input("What is your last name: ")

print("\nWelcome to Cash-R-Us",first_name,last_name + ", we will now set up a security PIN on your account.\n")

print("Hello World")

# Set up a PIN - Personal Identification Number
pin = input("Please choose a 4-digit Personal Identification Number: ")

print("\nThank you", first_name + ", we see that you set your PIN to",pin)

print("\nWould you like to make a transaction though our Automated Teller Machine")
ATM = input("Yes or No: ").lower()

if ATM == "yes":
    print("\n*******************************************************\n")

    # This part of the program will be asking users to complete a transaction though the ATM
    print("Please insert your ATM card\n")
    print("Welcome to Cash-R-Us ATM",first_name,last_name,"\n")
    userPIN = input("What is your four diget PIN: ")

    if pin == userPIN:
        balance = 674
        print("\nYour Balance: $" + str(balance))

        # Ask users what type of transaction they want - Withdrawal - Deposit
        typeOfTransaction = input("\nWould you like to make a Withdrawal, Deposit, or check your Balance\nW = Withdrawal or D = Deposit or B = Balance: ").lower()
        if typeOfTransaction == "w":
            withdrawalAmount = int(input("Enter amount of withdrawal: "))
            balance = balance - withdrawalAmount
            print("Your new balance is: $" + str(balance))

         elif typeOfTransaction == "d":
             depositAmount = int(input("Enter amount of your deposit: "))
             balance = balance + depositAmount
             print("Your new balance is: $" + str(balance))


    else:
        print("Sorry", first_name,last_name,"your PIN doesn't match our records")


else:
    print("\nHave a wonderful day",first_name,last_name + ", please come back and visit soon ;).")