""""
The goal of this machine problem is to create a program to simulate a fitness tracker. 
Users can add steps to their total step count, view their total steps, and calculate the calories burned based on their steps.
"""

totalSteps = 0

def AddSteps():
    global totalSteps
    user_input = input("How many steps? ")
    if user_input == "":
        print("Empty input is not allowed. Please enter a number.")
        return
        
    if user_input.isdigit():
        steps = int(user_input)
        if steps <= 0:
            print("Please enter a positive number of steps.")
        else:
            totalSteps += steps
            print(f"{steps} steps added!")
    else:
        print("Please enter a valid number of steps.")

def ViewTotalSteps():
    print(f"Total Steps: {totalSteps}")

def ViewCaloriesBurned():
    caloriesBurned = totalSteps * 0.04
    print(f"Calories Burned: {caloriesBurned:.2f} cal")

def Menu():
    print("===== Fitness Tracker =====")
    print("1. Add Steps")
    print("2. View Total Steps")
    print("3. View Calories Burned")
    print("4. Exit")
    print("===========================")

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
            AddSteps()
        elif choice == 2:
            ViewTotalSteps()
        elif choice == 3:
            ViewCaloriesBurned()
        elif choice == 4:
            print("Keep moving! Goodbye!")
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
    else:
        print("Please enter a valid number.")