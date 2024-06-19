from flask import Blueprint, request, jsonify
from app.models import  orderItem
from app.extensions import db

order_item_bp = Blueprint('order_item_bp', __name__)

@order_item_bp.route('/order_items', methods=['POST'])
def create_order_item():
    data = request.get_json()
    order_id = data.get('order_id')
    product_id = data.get('product_id')
    quantity = data.get('quantity')
    price = data.get('price')

    new_order_item = orderItem(order_id=order_id, product_id=product_id, quantity=quantity, price=price)
    db.session.add(new_order_item)
    db.session.commit()

    return jsonify({'message': 'Order item created successfully'}), 201

@order_item_bp.route('/order_items', methods=['GET'])
def get_order_items():
    order_items = orderItem.query.all()
    result = []
    for item in order_items:
        result.append({
            'id': item.id,
            'order_id': item.order_id,
            'product_id': item.product_id,
            'quantity': item.quantity,
            'price': item.price
        })
    return jsonify(result), 200

@order_item_bp.route('/order_items/<int:id>', methods=['GET'])
def get_order_item(id):
    order_item = orderItem.query.get_or_404(id)
    result = {
        'id': order_item.id,
        'order_id': order_item.order_id,
        'product_id': order_item.product_id,
        'quantity': order_item.quantity,
        'price': order_item.price
    }
    return jsonify(result), 200

@order_item_bp.route('/order_items/<int:id>', methods=['PUT'])
def update_order_item(id):
    data = request.get_json()
    order_item = orderItem.query.get_or_404(id)

    order_item.order_id = data.get('order_id', order_item.order_id)
    order_item.product_id = data.get('product_id', order_item.product_id)
    order_item.quantity = data.get('quantity', order_item.quantity)
    order_item.price = data.get('price', order_item.price)

    db.session.commit()
    return jsonify({'message': 'Order item updated successfully'}), 200

@order_item_bp.route('/order_items/<int:id>', methods=['DELETE'])
def delete_order_item(id):
    order_item = orderItem.query.get_or_404(id)
    db.session.delete(order_item)
    db.session.commit()
    return jsonify({'message': 'Order item deleted successfully'}), 200
