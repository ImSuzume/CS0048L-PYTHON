def classify_bp(systolic, diastolic):
    if systolic < 0 or diastolic < 0:
        raise ValueError("Invalid input: Blood pressure readings cannot be negative.")
    if systolic < 120 and diastolic < 80:
        return "Normal"
    elif 120 <= systolic < 130 and diastolic < 80:
        return "Elevated"
    else:
        return "High"

def main():
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

if __name__ == "__main__":
    main()
