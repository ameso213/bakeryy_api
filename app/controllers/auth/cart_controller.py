from flask import Blueprint, jsonify, request

# Define a Blueprint for the cart routes
cart_bp = Blueprint('cart',__name__, url_prefix='/api/v1/cart')

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
        return round(total, 2)  # Ensure total is rounded to 2 decimal places

    def display_cart(self):
        # This is for demonstration, replace with appropriate UI update logic
        print("Bakery Cart Contents:")
        for item in self.items:
            print(f"{item['name']} - ${item['price']:.2f} x {item['quantity']}")
        print(f"Total: ${self.calculate_total():.2f}")

# Create an instance of BakeryCart
bakery_cart = Cart()

# Define routes and their corresponding view functions
@cart_bp.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    data = request.json
    item_name = data['name']
    price = float(data['price'])
    quantity = int(data['quantity'])
    
    bakery_cart.add_to_cart(item_name, price, quantity)
    
    return jsonify({'message': 'Item added to cart'}), 200

@cart_bp.route('/remove_from_cart', methods=['DELETE'])
def remove_from_cart():
    data = request.json
    item_name = data['name']
    
    bakery_cart.remove_from_cart(item_name)
    
    return jsonify({'message': 'Item removed from cart'}), 200

@cart_bp.route('/update_quantity', methods=['PUT'])
def update_quantity():
    data = request.json
    item_name = data['name']
    quantity = int(data['quantity'])
    
    bakery_cart.update_quantity(item_name, quantity)
    
    return jsonify({'message': 'Item quantity updated'}), 200

@cart_bp.route('/display_cart', methods=['GET'])
def display_cart():
    # This endpoint could return HTML or a JSON response depending on your frontend needs
    cart_contents = {
        'items': bakery_cart.items,
        'total': bakery_cart.calculate_total()
    }
    
    return jsonify(cart_contents), 200
