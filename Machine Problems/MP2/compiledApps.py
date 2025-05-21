def fitness_tracker():
    def calculate_calories(activity, duration, weight):
        calorie_rates = {'walking': 5, 'running': 10, 'cycling': 8}
        if activity not in calorie_rates:
            raise ValueError(f"Invalid activity type: {activity}")
        if duration < 0:
            raise ValueError("Duration cannot be negative")
        if weight <= 0:
            raise ValueError("Weight cannot be negative or zero")
        rate = calorie_rates[activity]
        return rate * duration * (weight / 70)

    total_calories = 0
    try:
        weight = float(input("Enter your weight in kg: "))
        if weight <= 0:
            raise ValueError("Weight cannot be negative or zero")
    except ValueError:
        print("Invalid input. Please enter a valid number for weight.")
        return

    while True:
        activity = input("Enter activity (walking, running, cycling or 'done' to finish): ").lower()
        if activity == 'done':
            break
        try:
            duration = float(input("Enter duration in minutes: "))
            calories = calculate_calories(activity, duration, weight)
            print(f"Calories burned for {activity}: {calories:.2f}")
            total_calories += calories
        except ValueError as ve:
            print(ve)

    print(f"Total calories burned: {total_calories:.2f}")
    if total_calories > 500:
        print("Congratulations! You've achieved your daily goal.")

def health_monitoring():
    def classify_bp(systolic, diastolic):
        if systolic < 0 or diastolic < 0:
            raise ValueError("Invalid input: Blood pressure readings cannot be negative.")
        if systolic < 120 and diastolic < 80:
            return "Normal"
        elif 120 <= systolic < 130 and diastolic < 80:
            return "Elevated"
        else:
            return "High"

    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    summary = {'Normal': 0, 'Elevated': 0, 'High': 0}

    for day in days:
        print(f"\nEnter readings for {day}:")
        try:
            systolic = int(input("  Systolic: "))
            diastolic = int(input("  Diastolic: "))
            category = classify_bp(systolic, diastolic)
            print(f"  Classification: {category}")
            summary[category] += 1
        except ValueError as ve:
            print(f"  Error: {ve}")

    print("\nSummary Report:")
    for category, count in summary.items():
        print(f"{category}: {count} day(s)")
    if summary["High"] > 3:
        print("Warning: More than 3 days classified as High. Please consult a doctor.")

def banking_app():
    transactions = []
    balance = 0.0

    def deposit(amount):
        nonlocal balance
        if amount <= 0:
            raise ValueError("Invalid amount. Please enter a positive number.")
        balance += amount
        transactions.append(f"Deposited ${amount}")
        return balance

    def withdraw(amount):
        nonlocal balance
        if amount <= 0:
            raise ValueError("Invalid amount. Please enter a positive number.")
        if amount > balance:
            transactions.append(f"Attempted to withdraw ${amount} (declined)")
            raise ValueError("Insufficient funds. Transaction declined.")
        balance -= amount
        transactions.append(f"Withdrew ${amount}")
        return balance

    def check_balance():
        transactions.append("Checked balance")
        return balance

    try:
        balance = float(input("Enter initial balance: $"))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    while True:
        print("\nOptions: deposit, withdraw, check, exit")
        action = input("Choose an action: ").lower()

        if action == "deposit":
            try:
                amount = float(input("Enter amount to deposit: $"))
                print(f"Updated balance: ${deposit(amount)}")
            except ValueError as ve:
                print(ve)

        elif action == "withdraw":
            try:
                amount = float(input("Enter amount to withdraw: $"))
                print(f"Updated balance: ${withdraw(amount)}")
            except ValueError as ve:
                print(ve)

        elif action == "check":
            print(f"Current balance: ${check_balance()}")

        elif action == "exit":
            break

        else:
            print("Invalid action. Please choose a valid option.")

    print("\nTransaction Summary:")
    for t in transactions:
        print(t)
    print("End of session.")

def restaurant_order():
    MENU = {
        "burger": 5,
        "pizza": 10,
        "salad": 7
    }

    def calculate_bill(order):
        subtotal = 0
        for item, qty in order.items():
            subtotal += MENU[item] * qty
        service_charge = subtotal * 0.10
        total_before_discount = subtotal + service_charge
        discount = total_before_discount * 0.05 if total_before_discount > 50 else 0
        final_total = total_before_discount - discount
        return subtotal, service_charge, discount, final_total

    order = {}
    while True:
        item = input("Enter item (or 'done' to finish): ").lower()
        if item == 'done':
            break
        if item not in MENU:
            print(f"Invalid item. Please select a valid menu item.")
            continue
        try:
            qty = int(input(f"Enter quantity of {item}: "))
            if qty <= 0:
                print("Invalid quantity. Please enter a positive number.")
                continue
            order[item] = order.get(item, 0) + qty
        except ValueError:
            print("Invalid quantity. Please enter a valid number.")

    subtotal, service_charge, discount, final_total = calculate_bill(order)
    print("\n--- Final Bill ---")
    for item, qty in order.items():
        print(f"{qty} {item.capitalize()}(s): ${MENU[item] * qty}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Service Charge (10%): ${service_charge:.2f}")
    if discount > 0:
        print(f"Discount (5%): -${discount:.2f}")
    print(f"Total: ${final_total:.2f}")

def main_menu():
    while True:
        print("\n====== MAIN MENU ======")
        print("1. Fitness Tracker")
        print("2. Health Monitoring System")
        print("3. Banking Application")
        print("4. Restaurant Order Management")
        print("5. Exit")
        choice = input("Select an option (1-5): ")

        if choice == "1":
            fitness_tracker()
        elif choice == "2":
            health_monitoring()
        elif choice == "3":
            banking_app()
        elif choice == "4":
            restaurant_order()
        elif choice == "5":
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid selection. Please choose between 1 and 5.")

if __name__ == "__main__":
    main_menu()
