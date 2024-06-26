from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models import products
from datetime import datetime

products_bp = Blueprint('products', __name__, url_prefix='/api/v1/products')

@products_bp.route('/create', methods=['POST'])
def create_product():
    data = request.get_json()

    new_product = products(
        name=data['name'],
        description=data.get('description'),
        price=data['price'],
        category=data['category'],
        stock_quantity=data['stock_quantity'],
        image=data.get('image')
    )

    db.session.add(new_product)
    db.session.commit()

    return jsonify({'message': 'New product created successfully!'}), 201

@products_bp.route('/products', methods=['GET'])
def get_products():
    products = products.query.all()
    products_list = []
    for product in products:
        product_data = {
            'id': product.id,
            'name': product.name,
            'description': product.description,
            'price': str(product.price),  # Convert Numeric to string for JSON serialization
            'category': product.category,
            'stock_quantity': product.stock_quantity,
            'image': product.image,
            'created_at': product.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'updated_at': product.updated_at.strftime('%Y-%m-%d %H:%M:%S')
        }
        products_list.append(product_data)
    return jsonify(products_list)

@products_bp.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    product = products.query.get_or_404(id)
    product_data = {
        'id': product.id,
        'name': product.name,
        'description': product.description,
        'price': str(product.price),  # Convert Numeric to string for JSON serialization
        'category': product.category,
        'stock_quantity': product.stock_quantity,
        'image': product.image,
        'created_at': product.created_at.strftime('%Y-%m-%d %H:%M:%S'),
        'updated_at': product.updated_at.strftime('%Y-%m-%d %H:%M:%S')
    }
    return jsonify(product_data)

@products_bp.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    data = request.get_json()
    product = products.query.get_or_404(id)

    product.name = data.get('name', product.name)
    product.description = data.get('description', product.description)
    product.price = data.get('price', product.price)
    product.category = data.get('category', product.category)
    product.stock_quantity = data.get('stock_quantity', product.stock_quantity)
    product.image = data.get('image', product.image)

    db.session.commit()

    return jsonify({'message': 'Product updated successfully!'})

@products_bp.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = products.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()

    return jsonify({'message': 'Product deleted successfully!'})

# Remember to register the blueprint in your app
# from app.products_controllers import products_bp
# app.register_blueprint(products_bp, url_prefix='/api')
