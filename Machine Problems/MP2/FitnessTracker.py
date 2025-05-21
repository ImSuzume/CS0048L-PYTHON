def calculate_calories(activity, duration, weight):
    calorie_rates = {
        'walking': 5,
        'running': 10,
        'cycling': 8
    }
    if activity not in calorie_rates:
        raise ValueError(f"Invalid activity type: {activity}")
    if duration < 0:
        raise ValueError("Duration cannot be negative")
    if weight <= 0:
        raise ValueError("Weight cannot be negative or zero")
    
    rate = calorie_rates[activity]
    return rate * duration * (weight / 70)


def main():
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
        except Exception:
            print("Invalid input. Please enter valid values.")

    print(f"Total calories burned: {total_calories:.2f}")
    if total_calories > 500:
        print("Congratulations! You've achieved your daily goal.")

if __name__ == "__main__":
    main()
