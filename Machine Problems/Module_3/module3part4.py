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

def playGame():
    numberToGuess = random.randint(1, 100)
    guess = ""
    print("")
    print("I'm thinking of a number between 1 and 100.")
    while guess != numberToGuess:
        userInput = input("Enter your guess: ")
        if userInput.isdigit():
            guess = int(userInput)
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
            elif guess < numberToGuess:
                print("Too low. Try again.")
            elif guess > numberToGuess:
                print("Too high. Try again.")
            else:
                print("Congratulations! You guessed it.\n")
        else:
            print("Invalid input. Please enter a number.")

def main():
    choice=0
    while (choice!="2"):
        menu()
        choice = input("Select an option: ").lower()
        if choice=="1":
            playGame()
        elif choice=="2":
            print("See you soon...")
        else:
            print("")
            print("Invalid input. Try again.")
main()