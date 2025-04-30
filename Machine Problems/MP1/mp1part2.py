"""
The goal of this machine problem is to create a program to manage a grocery store. 
Users can view available items, add items to their cart, and calculate the total cost of 
their purchase, including VAT (12%).
"""

Rice = 50
Egg = 7
Milk = 60
Bread = 35
total = 0
rice_qty = 0
eggs_qty = 0
milk_qty = 0
bread_qty = 0

def Items():
    print("======= ITEM LIST ========")
    print(f"1. Rice - ₱{Rice}")
    print(f"2. Eggs - ₱{Egg}")
    print(f"3. Milk - ₱{Milk}")
    print(f"4. Bread - ₱{Bread}")
    print("==========================")

def AddtoCart():
    global total, rice_qty, eggs_qty, milk_qty, bread_qty
    item = input("Enter item to add (Rice, Egg, Milk, Bread): ").lower()
    
    if item == "":
        print("Empty input is not allowed. Please enter an item name.")
        return
        
    if (item == "rice"):
        price = Rice
        qty_input = input(f"Enter quantity of Rice to add: ")
        if qty_input == "":
            print("Empty input is not allowed. Please enter a quantity.")
            return
            
        if qty_input.isdigit():
            quantity = int(qty_input)
            if quantity <= 0:
                print("Please enter a positive quantity.")
                return
            rice_qty += quantity
            total += price * quantity
            print(f"Added {quantity} Rice(s) to your cart.")
        else:
            print("Invalid quantity. Please enter a number.")
            
    elif (item == "egg"):
        price = Egg
        qty_input = input(f"Enter quantity of Eggs to add: ")
        if qty_input == "":
            print("Empty input is not allowed. Please enter a quantity.")
            return
            
        if qty_input.isdigit():
            quantity = int(qty_input)
            if quantity <= 0:
                print("Please enter a positive quantity.")
                return
            eggs_qty += quantity
            total += price * quantity
            print(f"Added {quantity} Egg(s) to your cart.")
        else:
            print("Invalid quantity. Please enter a number.")
            
    elif (item == "milk"):
        price = Milk
        qty_input = input(f"Enter quantity of Milk to add: ")
        if qty_input == "":
            print("Empty input is not allowed. Please enter a quantity.")
            return
            
        if qty_input.isdigit():
            quantity = int(qty_input)
            if quantity <= 0:
                print("Please enter a positive quantity.")
                return
            milk_qty += quantity
            total += price * quantity
            print(f"Added {quantity} Milk(s) to your cart.")
        else:
            print("Invalid quantity. Please enter a number.")
            
    elif (item == "bread"):
        price = Bread
        qty_input = input(f"Enter quantity of Bread to add: ")
        if qty_input == "":
            print("Empty input is not allowed. Please enter a quantity.")
            return
            
        if qty_input.isdigit():
            quantity = int(qty_input)
            if quantity <= 0:
                print("Please enter a positive quantity.")
                return
            bread_qty += quantity
            total += price * quantity
            print(f"Added {quantity} Bread(s) to your cart.")
        else:
            print("Invalid quantity. Please enter a number.")
            
    else:
        print("Invalid item. Please enter Rice, Egg, Milk, or Bread.")
    print("==========================")

def CheckOut():
    print("===== Order Summary ======")

    if rice_qty > 0:
        print(f"Rice x {rice_qty} = ₱{rice_qty * Rice}")
    if eggs_qty > 0:
        print(f"Eggs x {eggs_qty} = ₱{eggs_qty * Egg}")
    if milk_qty > 0:
        print(f"Milk x {milk_qty} = ₱{milk_qty * Milk}")
    if bread_qty > 0:
        print(f"Bread x {bread_qty} = ₱{bread_qty * Bread}")

    VAT = total * 0.12
    totalfinal = total + VAT
    print(f"Subtotal: ₱{total:.2f}")
    print(f"VAT (12%): ₱{VAT:.2f}")
    print(f"Total: ₱{totalfinal:.2f}")
    print("Thank you for shopping!")
    print("Please come again!")
    print("==========================")
    
def Menu():
    print("========= MENU ===========")
    print("1. View Items")
    print("2. Add to Cart")
    print("3. Checkout")
    print("4. Exit")
    print("==========================")

choice = 0
while choice != 4:
    Menu()
    user_input = input("Enter choice: ")
    if user_input == "":
        print("Empty input is not allowed. Please enter a number.")
        continue
        
    if user_input.isdigit():
        choice = int(user_input)
        if choice == 1:
            Items()
        elif choice == 2:
            AddtoCart()
        elif choice == 3:
            CheckOut()
            break
        elif choice == 4:
            print("See you next time!")
            break
        else:
            print("Invalid input. Please enter a number between 1 and 4.")
    else:
        print("Please enter a valid number.")