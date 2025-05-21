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
    discount = 0
    if total_before_discount > 50:
        discount = total_before_discount * 0.05

    final_total = total_before_discount - discount
    return subtotal, service_charge, discount, final_total

def main():
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

if __name__ == "__main__":
    main()
