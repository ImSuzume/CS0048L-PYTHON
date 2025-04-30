class pythonRestaurant:
    def initializeVal(self):
        self.burger = 120
        self.pizza = 300
        self.pasta = 250
        self.fries = 80
        self.total = 0
        self.choice = 0

    def menu(self):
        print("==============================")
        print(f"1. Burger - ₱{self.burger}")
        print(f"2. Pizza - ₱{self.pizza}")
        print(f"3. Pasta - ₱{self.pasta}")
        print(f"4. Fries - ₱{self.fries}")
        print("5. Exit")
        print("==============================")

    def order(self):
        self.initializeVal()
        while self.choice != 5:
            self.menu()
            choice_input = input("Select an item: ")
            if choice_input == "":
                print("Please enter a number. Empty input is not allowed.")
                continue
            
            if choice_input.isdigit():
                self.choice = int(choice_input)
                if self.choice == 1:
                    print("Added Burger to your order.")
                    self.total += self.burger
                elif self.choice == 2:
                    print("Added Pizza to your order.")
                    self.total += self.pizza
                elif self.choice == 3:
                    print("Added Pasta to your order.")
                    self.total += self.pasta
                elif self.choice == 4:
                    print("Added Fries to your order.")
                    self.total += self.fries
                elif self.choice == 5:
                    print("======= Order Summary ========")
                    if self.total > 500:
                        totalFinal = self.total * 0.9
                    else:
                        totalFinal = self.total
                    print(f"Total before discount: ₱{self.total:.2f}")
                    print(f"Final Amount to Pay: ₱{totalFinal:.2f}")
                    print("==============================")
                else:
                    print("Invalid input. Please enter a number between 1 and 5.")
            else:
                print("Invalid input. Please enter a number.")


class groceryStore:
    def initializeVal(self):
        self.rice = 50
        self.egg = 7
        self.milk = 60
        self.bread = 35
        self.total = 0
        self.riceQty = 0
        self.eggsQty = 0
        self.milkQty = 0
        self.breadQty = 0

    def items(self):
        print("========= ITEM LIST ==========")
        print(f"1. Rice - ₱{self.rice}")
        print(f"2. Eggs - ₱{self.egg}")
        print(f"3. Milk - ₱{self.milk}")
        print(f"4. Bread - ₱{self.bread}")
        print("==============================")

    def addToCart(self):
        item = input("Enter item to add (Rice, Egg, Milk, Bread): ").lower()
        
        if item == "":
            print("Empty input is not allowed. Please enter an item name.")
            return
            
        if item == "rice":
            price = self.rice
            qty_input = input(f"Enter quantity of Rice to add: ")
            if qty_input == "":
                print("Empty input is not allowed. Please enter a quantity.")
                return
                
            if qty_input.isdigit():
                quantity = int(qty_input)
                if quantity <= 0:
                    print("Please enter a positive quantity.")
                    return
                self.riceQty += quantity
                self.total += price * quantity
                print(f"Added {quantity} Rice(s) to your cart.")
            else:
                print("Invalid quantity. Please enter a number.")
                
        elif item == "egg":
            price = self.egg
            qty_input = input(f"Enter quantity of Eggs to add: ")
            if qty_input == "":
                print("Empty input is not allowed. Please enter a quantity.")
                return
                
            if qty_input.isdigit():
                quantity = int(qty_input)
                if quantity <= 0:
                    print("Please enter a positive quantity.")
                    return
                self.eggsQty += quantity
                self.total += price * quantity
                print(f"Added {quantity} Egg(s) to your cart.")
            else:
                print("Invalid quantity. Please enter a number.")
                
        elif item == "milk":
            price = self.milk
            qty_input = input(f"Enter quantity of Milk to add: ")
            if qty_input == "":
                print("Empty input is not allowed. Please enter a quantity.")
                return
                
            if qty_input.isdigit():
                quantity = int(qty_input)
                if quantity <= 0:
                    print("Please enter a positive quantity.")
                    return
                self.milkQty += quantity
                self.total += price * quantity
                print(f"Added {quantity} Milk(s) to your cart.")
            else:
                print("Invalid quantity. Please enter a number.")
                
        elif item == "bread":
            price = self.bread
            qty_input = input(f"Enter quantity of Bread to add: ")
            if qty_input == "":
                print("Empty input is not allowed. Please enter a quantity.")
                return
                
            if qty_input.isdigit():
                quantity = int(qty_input)
                if quantity <= 0:
                    print("Please enter a positive quantity.")
                    return
                self.breadQty += quantity
                self.total += price * quantity
                print(f"Added {quantity} Bread(s) to your cart.")
            else:
                print("Invalid quantity. Please enter a number.")
                
        else:
            print("Invalid item. Please enter Rice, Egg, Milk, or Bread.")
        print("==============================")
        
    def checkout(self):
        print("======= Order Summary ========")

        if self.riceQty > 0:
            print(f"Rice x {self.riceQty} = ₱{self.riceQty * self.rice}")
        if self.eggsQty > 0:
            print(f"Eggs x {self.eggsQty} = ₱{self.eggsQty * self.egg}")
        if self.milkQty > 0:
            print(f"Milk x {self.milkQty} = ₱{self.milkQty * self.milk}")
        if self.breadQty > 0:
            print(f"Bread x {self.breadQty} = ₱{self.breadQty * self.bread}")

        vat = self.total * 0.12
        totalFinal = self.total + vat
        print(f"Subtotal: ₱{self.total:.2f}")
        print(f"VAT (12%): ₱{vat:.2f}")
        print(f"Total: ₱{totalFinal:.2f}")
        print("Thank you for shopping!")
        print("Please come again!")
        print("==============================")

    def menu(self):
        print("=========== MENU =============")
        print("1. View Items")
        print("2. Add to Cart")
        print("3. Checkout")
        print("4. Exit")
        print("==============================")

    def shop(self):
        self.initializeVal()
        choice = 0
        while choice != 4:
            self.menu()
            userInput = input("Enter choice: ")
            if userInput == "":
                print("Empty input is not allowed. Please enter a number.")
                continue
                
            if userInput.isdigit():
                choice = int(userInput)
                if choice == 1:
                    self.items()
                elif choice == 2:
                    self.addToCart()
                elif choice == 3:
                    self.checkout()
                    break
                elif choice == 4:
                    print("See you next time!")
                    break
                else:
                    print("Invalid input. Please enter a number between 1 and 4.")
            else:
                print("Please enter a valid number.")
        

class fitnessTracker:
    def initializeVal(self):
        self.totalSteps = 0

    def addSteps(self):
        userInput = input("How many steps? ")
        if userInput == "":
            print("Empty input is not allowed. Please enter a number.")
            return
            
        if userInput.isdigit():
            steps = int(userInput)
            if steps <= 0:
                print("Please enter a positive number of steps.")
            else:
                self.totalSteps += steps
                print(f"{steps} steps added!")
        else:
            print("Please enter a valid number of steps.")

    def viewTotalSteps(self):
        print(f"Total Steps: {self.totalSteps}")

    def viewCaloriesBurned(self):
        caloriesBurned = self.totalSteps * 0.04
        print(f"Calories Burned: {caloriesBurned:.2f} cal")

    def menu(self):
        print("====== Fitness Tracker =======")
        print("1. Add Steps")
        print("2. View Total Steps")
        print("3. View Calories Burned")
        print("4. Exit")
        print("==============================")

    def track(self):
        self.initializeVal()
        choice = 0
        while choice != 4:
            self.menu()
            userInput = input("Enter choice: ")
            if userInput == "":
                print("Empty input is not allowed. Please enter a number.")
                continue
                
            if userInput.isdigit():
                choice = int(userInput)
                if choice == 1:
                    self.addSteps()
                elif choice == 2:
                    self.viewTotalSteps()
                elif choice == 3:
                    self.viewCaloriesBurned()
                elif choice == 4:
                    print("Keep moving! Goodbye!")
                else:
                    print("Invalid choice. Please enter a number between 1 and 4.")
            else:
                print("Please enter a valid number.")


while True:
    print("========= Main Menu ==========")
    print("1. Python Restaurant")
    print("2. Grocery Store")
    print("3. Fitness Tracker")
    print("4. Exit")
    print("==============================")

    choice = input("Select an option: ")
    if choice == "":
        print("Empty input is not allowed. Please enter a number.")
        continue
        
    if choice.isdigit():
        if choice == '1':
            restaurant = pythonRestaurant()
            restaurant.order()
        elif choice == '2':
            store = groceryStore()
            store.shop()
        elif choice == '3':
            tracker = fitnessTracker()
            tracker.track()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please enter a number between 1 and 4.")
    else:
        print("Invalid option. Please enter a number.")