# Restaurant Order Management System
---

## Problem Statement 1

This machine problem aims to create a simple program to manage orders at the "Python Restaurant." Users can select items from a menu, and the program will calculate the total cost of their order. If the total exceeds ₱500, a 10% discount is applied.

### Requirements:
1. Display a menu with predefined items.
2. Allow users to repeatedly select items until they choose to exit.
3. Calculate the total cost and apply discounts if applicable.
4. Do not use arrays, lists, or dictionaries to store the menu items.
5. Use `if-elif` statements to handle menu choices.

---

## Features

- Displays a menu with predefined items and prices.
- Allows users to add items to their order dynamically.
- Calculates the total cost of the order.
- Applies a 10% discount if the total exceeds ₱500.
- Provides a clear order summary at the end.

--- Welcome to Python Restaurant ---

--- Your Order ---

Menu:
1. Burger - ₱120
2. Pizza - ₱300
3. Pasta - ₱250
4. Fries - ₱80
5. Exit
Select an item: 1
Added Burger to your order.

Menu:
1. Burger - ₱120
2. Pizza - ₱300
3. Pasta - ₱250
4. Fries - ₱80
5. Exit
Select an item: 2
Added Pizza to your order.

Menu:
1. Burger - ₱120
2. Pizza - ₱300
3. Pasta - ₱250
4. Fries - ₱80
5. Exit
Select an item: 5

--- Order Summary ---

Total before discount: ₱420

Final Amount to Pay: ₱420


# Grocery Store Management System

## Problem Statement 2

The goal of this machine problem is to create a program to manage a grocery store. Users can view available items, add items to their cart, and calculate the total cost of their purchase, including VAT (12%).

### Requirements:
1. Display a list of available items and their prices.
2. Allow users to add items to their cart and specify quantities.
3. Calculate the subtotal, VAT, and total amount during checkout.
4. Use `if-elif` statements to handle menu choices and item tracking.

---

## Features

- Displays a list of available items and their prices.
- Allows users to add items to their cart dynamically.
- Tracks quantities of items in the cart.
- Calculates the subtotal, VAT (12%), and total amount during checkout.
- Provides a clear and user-friendly interface.

---

--- Grocery Store ---
1. View Items
2. Add to Cart
3. Checkout
4. Exit
Enter choice: 1

Rice: ₱50
Eggs: ₱7
Milk: ₱60
Bread: ₱35

--- Grocery Store ---
1. View Items
2. Add to Cart
3. Checkout
4. Exit
Enter choice: 2
Enter item to add: Rice
Enter quantity: 2
Added 2 Rice(s) to cart.

--- Grocery Store ---
1. View Items
2. Add to Cart
3. Checkout
4. Exit
Enter choice: 3

--- Cart Summary ---

Rice x 2 = ₱100

Subtotal: ₱100

VAT (12%): ₱12

Total: ₱112


# Fitness Tracker

---

## Problem Statement 3

The goal of this machine problem is to create a program to simulate a fitness tracker. Users can add steps to their total step count, view their total steps, and calculate the calories burned based on their steps.

### Requirements:
1. Provide a menu with the following options:
   - Add Steps: Allow the user to add steps to their total step count.
   - View Total Steps: Display the total number of steps added so far.
   - View Calories Burned: Calculate and display the calories burned based on the total steps (assume 0.04 calories per step).
   - Exit: End the program with a friendly message.
2. Track the total number of steps using a single variable.
3. Use the formula `calories = steps * 0.04` to calculate calories burned.
4. Provide clear feedback after each operation.
5. Handle invalid inputs gracefully.

---

## Features

- Allows users to add steps to their total step count.
- Displays the total number of steps added so far.
- Calculates and displays the calories burned based on the total steps.
- Provides a user-friendly interface with clear feedback.
- Handles invalid inputs gracefully.

---

--- Fitness Tracker ---
1. Add Steps
2. View Total Steps
3. View Calories Burned
4. Exit
Enter choice: 1
How many steps? 500
500 steps added!

--- Fitness Tracker ---
1. Add Steps
2. View Total Steps
3. View Calories Burned
4. Exit
Enter choice: 1
How many steps? 300
300 steps added!

--- Fitness Tracker ---
1. Add Steps
2. View Total Steps
3. View Calories Burned
4. Exit
Enter choice: 2
Total Steps: 800

--- Fitness Tracker ---
1. Add Steps
2. View Total Steps
3. View Calories Burned
4. Exit
Enter choice: 3
Calories Burned: 32.00 calories

--- Fitness Tracker ---
1. Add Steps
2. View Total Steps
3. View Calories Burned
4. Exit
Enter choice: 4
Keep moving! Goodbye!



