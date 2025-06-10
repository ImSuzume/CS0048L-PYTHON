'''
Create a simple calculator that allows users to perform basic arithmetic operations:
addition, subtraction, multiplication, and division. The program should display a menu
with options for each operation and allow the user to choose an operation and input the
numbers. The program should continue to run until the user chooses to exit.
'''

def add(num1, num2):
    result = num1 + num2
    print (f"The sum of {num1} and {num2} is {result}")
    
def subtract(num1, num2):
    result = num1 - num2
    print (f"The difference of {num1} and {num2} is {result}")
    
def multiply(num1, num2):
    result = num1 * num2
    print (f"The product of {num1} and {num2} is {result}")
    
def divide(num1, num2):
    result = num1 / num2
    print (f"The quotient of {num1} and {num2} is {result}")
    
num1 = 0
num2 = 0

def userInput():
    global num1, num2
    num1 = eval(input("Input first number: "))
    num2 = eval(input("Input second number: "))
    return num1, num2


def menu ():
    print("==============================")
    print ("a. Add")
    print ("b. Subtract")
    print ("c. Multiply")
    print ("d. Divide")
    print ("e. Exit")
    print("==============================")

def main():
    global num1, num2
    ch = ""
    while (ch!="e"):
        menu()
        ch = input("Select an option: ").lower()
        if ch == "a":
            userInput()
            add(num1, num2)
        elif ch == "b":
            userInput()
            subtract(num1, num2)
        elif ch == "c":
            userInput()
            multiply(num1, num2)
        elif ch == "d":
            userInput()
            divide(num1, num2)
        elif ch == "e":
            print("See you soon...")
        else:
            print("Invalid input. Try again.")
            
main()