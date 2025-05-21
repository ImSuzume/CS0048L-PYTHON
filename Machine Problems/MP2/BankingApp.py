transactions = []
balance = 0.0

def deposit(amount):
    global balance
    if amount <= 0:
        raise ValueError("Invalid amount. Please enter a positive number.")
    balance += amount
    transactions.append(f"Deposited ${amount}")
    return balance

def withdraw(amount):
    global balance
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

def main():
    global balance
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

if __name__ == "__main__":
    main()
