"""
The goal of this machine problem is to create a program to manage a grocery store. 
Users can view available items, add items to their cart, and calculate the total cost of 
their purchase, including VAT (12%).
"""

#value
Rice = 50
Eggs = 7
Milk = 60
Bread = 35
total = 0
choice = 0

def Items():
    print ("============================")
    print (f"1. Rice - ₱{Rice}")
    print (f"2. Eggs - ₱{Eggs}")
    print (f"3. Milk - ₱{Milk}")
    print (f"4. Bread - ₱{Bread}")
    print ("============================")

def AddtoCart():
        choice=input("Select an item: ").lower()
        if (choice == 'rice'):
            print ("Added Rice to your order.")
            total += Rice
        elif (choice == 'egg'):
            print ("Added Eggs to your order.")
            total += Eggs
        elif (choice == 'milk'):
            print ("Added Milk to your order.")
            total += Milk
        elif (choice == 'bread'):
            print ("Added Bread to your order.")
            total += Bread
        else:
            print("Invalid input.")
            
def CheckOut(total):
    print ("====== Order Summary =======")
    VAT = total*.12
    totalfinal = total+VAT
    print (f"Total before VAT: ₱{total:.2f}")
    print (f"VAT: ₱{VAT:.2f}")
    print (f"Final Amount to Pay: ₱{totalfinal:.2f}")
    
def Menu():
    print ("============================")
    print (f"1. View Items")
    print (f"2. Add to Cart")
    print (f"3. Checkout")
    print (f"4. Exit")
    print ("============================")

def main():
    while (Choice !=4):
        Menu()
        Choice = eval(input("Enter choice: "))
        if (Choice == 1):
            Items()
        elif (choice == 2):
            AddtoCart()
        elif (choice == 3):
           CheckOut()
        elif (choice == 4):
            print("Thank you!")
        else:
            print("Invalid input.")