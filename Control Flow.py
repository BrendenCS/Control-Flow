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



else:
    print("\nHave a wonderful day",first_name,last_name + ", please come back and visit soon ;).")