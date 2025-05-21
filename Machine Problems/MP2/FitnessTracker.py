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

    # Weight input and validation
    try:
        weight_input = input("Enter your weight in kg: ")
        weight = float(weight_input)
    except ValueError:
        print("Invalid input. Please enter a valid number for weight.")
        return

    if weight < 0:
        print("Weight cannot be negative")
        return
    elif weight == 0:
        print("Weight cannot be zero")
        return

    while True:
        activity = input("Enter activity (walking, running, cycling or 'done' to finish): ").lower()
        if activity == 'done':
            break

        if activity not in ['walking', 'running', 'cycling']:
            print(f"Invalid activity type: {activity}")
            continue

        # Duration input and validation
        duration_input = input("Enter duration in minutes: ")
        try:
            duration = float(duration_input)
        except ValueError:
            print("Invalid input. Please enter a valid number for duration.")
            continue

        if duration < 0:
            print("Duration cannot be negative")
            continue

        try:
            calories = calculate_calories(activity, duration, weight)
            print(f"Calories burned for {activity}: {calories:.2f}")
            total_calories += calories
        except ValueError as ve:
            print(ve)

    print(f"Total calories burned: {total_calories:.2f}")
    if total_calories > 500:
        print("Congratulations! You've achieved your daily goal.")


if __name__ == "__main__":
    main()
