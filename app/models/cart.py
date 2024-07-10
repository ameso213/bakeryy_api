class Cart:
    def __init__(self):
        self.items = []

    def add_to_cart(self, item_name, price, quantity):
        # Check if item already exists in cart
        for item in self.items:
            if item['name'] == item_name:
                item['quantity'] += quantity
                break
        else:
            # If item doesn't exist, add new item to cart
            self.items.append({'name': item_name, 'price': price, 'quantity': quantity})
        
        # Display cart contents (you can update UI here)
        self.display_cart()

    def remove_from_cart(self, item_name):
        # Remove item from cart
        self.items = [item for item in self.items if item['name'] != item_name]

        # Display cart contents (you can update UI here)
        self.display_cart()

    def update_quantity(self, item_name, quantity):
        # Update item quantity in the cart
        for item in self.items:
            if item['name'] == item_name:
                item['quantity'] = quantity
                break
        
        # Display cart contents (you can update UI here)
        self.display_cart()

    def calculate_total(self):
        total = sum(item['price'] * item['quantity'] for item in self.items)
        return f"${total:.2f}"  # Ensure total is formatted to 2 decimal places

    def display_cart(self):
        # Output cart contents (example implementation)
        print("Bakery Cart Contents:")
        for item in self.items:
            print(f"{item['name']} - ${item['price']:.2f} x {item['quantity']}")
        print(f"Total: {self.calculate_total()}")


if __name__ == "__main__":
    bakery_cart = Cart()

    bakery_cart.add_to_cart("Croissant", 2.50, 2)
    bakery_cart.add_to_cart("Baguette", 3.50, 1)

    bakery_cart.update_quantity("Croissant", 3)

    bakery_cart.remove_from_cart("Baguette")
