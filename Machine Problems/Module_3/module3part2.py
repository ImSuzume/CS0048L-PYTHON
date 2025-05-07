"""
Create a program that converts temperatures between Celsius and Fahrenheit.
The program should display a menu with options to convert from Celsius to
Fahrenheit or from Fahrenheit to Celsius. The program should continue to
run until the user chooses to exit.
"""
temp = 0

def userInput():
    global temp
    temp = eval(input("Input temperature: "))
    return temp

def CtoF():
    NewTemp = (temp * (9/5) + 32)
    print("")
    print (f"{temp}C is equals to {NewTemp}F.")

def FtoC():
    NewTemp = (temp - 32) * (5/9)
    print("")
    print (f"{temp}F is equals to {NewTemp}C.")

def menu ():
    print("==================================")
    print ("1. Convert Celcius to Fahrenheit")
    print ("2. Convert Fahrenheit to Celcius")
    print ("3. Exit")
    print("==================================")
    
def main():
    choice=0
    while (choice!="3"):
        menu()
        choice = input("Select an option: ").lower()
        if choice=="1":
            userInput()
            CtoF()
        elif choice=="2":
            userInput()
            FtoC()
        elif choice == "3":
            print("See you soon...")
        else:
            print("")
            print("Invalid input. Try again.")
main()