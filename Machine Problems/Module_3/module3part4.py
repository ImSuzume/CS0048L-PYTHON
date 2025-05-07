"""
Create a number guessing game where the user tries to guess a randomly
generated number within a specified range (1 to 100). The program should
provide feedback on whether the guess is too high or too low. The program
should continue to run until the user chooses to exit.
"""

import random

def menu ():
    print("==================================")
    print ("1. Enter a Number")
    print ("2. Exit")
    print("==================================")
    
def main():
    choice=0
    while (choice!="2"):
        menu()
        choice = input("Select an option: ").lower()
        if choice=="1":
            print("")
        elif choice=="2":
            print("See you soon...")
        else:
            print("")
            print("Invalid input. Try again.")
main()