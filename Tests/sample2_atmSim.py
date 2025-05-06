'''
ATM Simulator Program
'''

#global variable
balance = 1000


def atm_machine():
    global balance
    while True:
        print ("\nATM MENU")
        print ("1. Check Balance")
        print ("2. Deposit")
        print ("3. Withdraw")
        print ("4. Exit")
        
        choice = input ("Enter your choice from 1- 4: ")
        
        if choice == "1":
            print (f"Your balance is {balance:.2f}")
        elif choice == "2":
            amount = float (input("Enter amount to deposit "))
            if amount > 0:
                balance += amount
                print (f"Deposited {amount:.2f}, New balance is {balance:.2f}")
            else:
                print ("Invalid amount")
        elif choice == "3":
            amount = float (input("Enter amount to withdraw "))
            if amount > balance:
                print ("Insufficient funds")
            elif amount <= 0:
                print ("Invalid amount")
            else:
                balance -= amount
                print (f"Withdrew amount {amount:.2f}, New Balance {balance:.2f}")
        elif choice == "4":
            print ("Thank you for using the ATM system")
            break 
        else:
            print ("Invalid Choice, Try again")
    
    
atm_machine()




'''
ATM Simulator Program
'''

#global variable
balance = 1000


def atm_machine():
    global balance
    while True:
        print ("\nATM MENU")
        print ("1. Check Balance")
        print ("2. Deposit")
        print ("3. Withdraw")
        print ("4. Exit")
        
        choice = input ("Enter your choice from 1- 4: ")
        
        if choice == "1":
            print (f"Your balance is {balance:.2f}")
        elif choice == "2":
            amount = float (input("Enter amount to deposit "))
            if amount > 0:
                balance += amount
                print (f"Deposited {amount:.2f}, New balance is {balance:.2f}")
            else:
                print ("Invalid amount")
        elif choice == "3":
            amount = float (input("Enter amount to withdraw "))
            if amount > balance:
                print ("Inssufient funds")
            elif amount <= 0:
                print ("Invalid amount")
            else:
                balance -= amount
                print (f"Withdrew amount {amount:.2f}, New Balance {balance:.2f}")
        elif choice == "4":
            print ("Thank you for using the ATM system")
            break 
        else:
            print ("Invalid Choice, Try again")
    
    
atm_machine()