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
    if total_before_discount >= 50:
        discount = total_before_discount * 0.05

    final_total = total_before_discount - discount
    return subtotal, service_charge, discount, final_total

def display_menu():
    print("Menu:")
    for item, price in MENU.items():
        print(f"{item.capitalize()}: ${price}")
    print()  # Blank line for spacing

def main():
    display_menu()

    order = {}

    while True:
        item = input("Enter item (or 'done' to finish): ").strip().lower()
        if item == 'done':
            break
        if item not in MENU:
            print(f"Invalid item. Please select a valid menu item.")
            continue
        qty_input = input(f"Enter quantity of {item}: ").strip()
        if not qty_input.isdigit():
            print("Invalid quantity. Please enter a valid number.")
            continue
        qty = int(qty_input)
        if qty <= 0:
            print("Invalid quantity. Please enter a positive number.")
            continue
        order[item] = order.get(item, 0) + qty

    subtotal, service_charge, discount, final_total = calculate_bill(order)

    print("\n--- Final Bill ---")
    if not order:
        print("No items ordered")
    else:
        for item, qty in order.items():
            item_display = item.capitalize()
            if qty > 1:
                if item_display.endswith('s'):
                    item_display += 'es'
                else:
                    item_display += 's'
            print(f"{qty} {item_display}: ${MENU[item] * qty}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Service charge (10%): ${service_charge:.2f}")
    if discount > 0:
        print(f"Discount (5%): -${discount:.2f}")
    else:
        print("No discount (total bill < $50)")
    print(f"Final bill: ${final_total:.2f}")
    print("Itemized details:")
    if not order:
        print("No items ordered")
    else:
        for item, qty in order.items():
            print(f"{qty} {item.capitalize()}{'s' if qty > 1 else ''}: ${MENU[item] * qty}")
    print(f"Total: ${final_total:.2f}")

if __name__ == "__main__":
    main()
