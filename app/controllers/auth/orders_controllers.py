from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models import orders
from datetime import datetime

orders_bp = Blueprint('orders', __name__, url_prefix='/api/v1/orders')

@orders_bp.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()

    new_order = orders(
        customer_id=data['customer_id'],
        product_id=data['product_id'],
        status=data['status'],
        quantity=data['quantity'],
        total_price=data['total_price'],
        order_date=datetime.strptime(data['order_date'], '%Y-%m-%d %H:%M:%S') if data.get('order_date') else None
    )

    db.session.add(new_order)
    db.session.commit()

    return jsonify({'message': 'New order created successfully!'}), 201

@orders_bp.route('/orders', methods=['GET'])
def get_orders():
    orders = order.query.all()
    orders_list = []
    for order in orders:
        order_data = order.get_order_details()
        orders_list.append(order_data)
    return jsonify(orders_list)

@orders_bp.route('/orders/<int:id>', methods=['GET'])
def get_order(id):
    order = order.query.get_or_404(id)
    order_data = order.get_order_details()
    return jsonify(order_data)

@orders_bp.route('/orders/<int:id>', methods=['PUT'])
def update_order(id):
    data = request.get_json()
    order = order.query.get_or_404(id)

    order.customer_id = data.get('customer_id', order.customer_id)
    order.product_id = data.get('product_id', order.product_id)
    order.status = data.get('status', order.status)
    order.quantity = data.get('quantity', order.quantity)
    order.total_price = data.get('total_price', order.total_price)
    order.order_date = datetime.strptime(data['order_date'], '%Y-%m-%d %H:%M:%S') if data.get('order_date') else order.order_date

    db.session.commit()

    return jsonify({'message': 'Order updated successfully!'})

@orders_bp.route('/orders/<int:id>', methods=['DELETE'])
def delete_order(id):
    order = orders.query.get_or_404(id)
    db.session.delete(order)
    db.session.commit()

    return jsonify({'message': 'Order deleted successfully!'})

# Remember to register the blueprint in your app
# from app.orders_controllers import orders_bp
# app.register_blueprint(orders_bp, url_prefix='/api')
