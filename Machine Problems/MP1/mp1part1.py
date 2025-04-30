"""
This machine problem aims to create a simple program to manage orders at the "Python Restaurant." 
Users can select items from a menu, and the program will calculate the total cost of their order. 
If the total exceeds ₱500, a 10% discount is applied.
"""

#value
Burger = 120
Pizza = 300
Pasta = 250
Fries = 80
total = 0
choice = 0

def menu():
    print ("============================")
    print (f"1. Burger - ₱{Burger}")
    print (f"2. Pizza - ₱{Pizza}")
    print (f"3. Pasta - ₱{Pasta}")
    print (f"4. Fries - ₱{Fries}")
    print ("5. Exit")
    print ("============================")

while (choice!=5):
    menu()
    choice_input = input("Select an item: ")
    if choice_input == "":
        print("Please enter a number. Empty input is not allowed.")
        continue
    
    if choice_input.isdigit():
        choice = int(choice_input)
        if (choice == 1):
            print ("Added Burger to your order.")
            total += Burger
        elif (choice == 2):
            print ("Added Pizza to your order.")
            total += Pizza
        elif (choice == 3):
            print ("Added Pasta to your order.")
            total += Pasta
        elif (choice == 4):
            print ("Added Fries to your order.")
            total += Fries
        elif (choice == 5):
            print ("====== Order Summary =======")
            if (total > 500):
                totalfinal=total*0.9
            else:
                totalfinal=total
            print (f"Total before discount: ₱{total:.2f}")
            print (f"Final Amount to Pay: ₱{totalfinal:.2f}")
            print ("============================")
        else:
            print("Invalid input. Please enter a number between 1 and 5.")
    else:
        print("Invalid input. Please enter a number.")