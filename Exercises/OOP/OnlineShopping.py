class Product:
    def __init__(self, name, price, quantity):
        self.name = name.lower()
        self.price = price
        self.quantity = quantity

    def subtotal(self):
        return self.price * self.quantity

    def __str__(self):
        return f"{self.name.capitalize()} - ${self.price:.2f} x {self.quantity} = ${self.subtotal():.2f}"


class ShoppingCart:
    def __init__(self):
        self.cart = {}  # key: product name, value: Product instance

    def add_product(self):
        name = input("Enter product name: ").strip()
        price_input = input("Enter price: ").strip()
        quantity_input = input("Enter quantity: ").strip()

        # Input validation
        try:
            price = float(price_input)
            quantity = int(quantity_input)
            if price < 0 or quantity <= 0:
                print("Price must be non-negative and quantity must be at least 1.")
                return
        except ValueError:
            print("Invalid price or quantity.")
            return

        if name.lower() in self.cart:
            self.cart[name.lower()].quantity += quantity
            print(f"Updated quantity of {name}.")
        else:
            self.cart[name.lower()] = Product(name, price, quantity)
            print(f"Added {name} to the cart.")

    def remove_product(self):
        name = input("Enter product name to remove: ").strip().lower()
        if name in self.cart:
            del self.cart[name]
            print(f"{name.capitalize()} removed from cart.")
        else:
            print("Product not found in cart.")

    def view_cart(self):
        if not self.cart:
            print("Your cart is empty.")
        else:
            print("\nYour Shopping Cart:")
            for product in self.cart.values():
                print(product)

    def checkout(self):
        if not self.cart:
            print("Cart is empty. Nothing to checkout.")
            return
        total = sum(product.subtotal() for product in self.cart.values())
        print("\n===== Checkout =====")
        self.view_cart()
        print(f"Total Price: ${total:.2f}")
        print("Thank you for your purchase!")
        self.cart.clear()

    def menu(self):
        while True:
            print("\n===== Online Shopping Cart =====")
            print("1. Add Product")
            print("2. Remove Product")
            print("3. View Cart")
            print("4. Checkout")
            print("5. Exit")
            choice = input("Choose an option (1-5): ").strip()

            if choice == '1':
                self.add_product()
            elif choice == '2':
                self.remove_product()
            elif choice == '3':
                self.view_cart()
            elif choice == '4':
                self.checkout()
            elif choice == '5':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please select from 1 to 5.")


# Run the program
cart = ShoppingCart()
cart.menu()