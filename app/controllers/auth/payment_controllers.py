from flask import Blueprint, request, jsonify
from app.models import  payment
from app.extensions import db
payment_bp = Blueprint('payment_bp', __name__, url_prefix='/api/v1/payment')

@payment_bp.route('/payments', methods=['POST'])
def create_payment():
    data = request.get_json()
    order_id = data.get('order_id')
    amount = data.get('amount')
    payment_method = data.get('payment_method')
    status = data.get('status')
    transaction_id = data.get('transaction_id')

    new_payment = payment(order_id=order_id, amount=amount, payment_method=payment_method, status=status, transaction_id=transaction_id)
    db.session.add(new_payment)
    db.session.commit()

    return jsonify({'message': 'Payment created successfully'}), 201

@payment_bp.route('/payments', methods=['GET'])
def get_payments():
    payments = payment.query.all()
    result = []
    for payment in payments:
        result.append({
            'id': payment.id,
            'order_id': payment.order_id,
            'amount': payment.amount,
            'payment_method': payment.payment_method,
            'status': payment.status,
            'transaction_id': payment.transaction_id,
            'created_at': payment.created_at
        })
    return jsonify(result), 200

@payment_bp.route('/payments/<int:id>', methods=['GET'])
def get_payment(id):
    payment = payment.query.get_or_404(id)
    result = {
        'id': payment.id,
        'order_id': payment.order_id,
        'amount': payment.amount,
        'payment_method': payment.payment_method,
        'status': payment.status,
        'transaction_id': payment.transaction_id,
        'created_at': payment.created_at
    }
    return jsonify(result), 200

@payment_bp.route('/payments/<int:id>', methods=['PUT'])
def update_payment(id):
    data = request.get_json()
    payment = payment.query.get_or_404(id)

    payment.order_id = data.get('order_id', payment.order_id)
    payment.amount = data.get('amount', payment.amount)
    payment.payment_method = data.get('payment_method', payment.payment_method)
    payment.status = data.get('status', payment.status)
    payment.transaction_id = data.get('transaction_id', payment.transaction_id)

    db.session.commit()
    return jsonify({'message': 'Payment updated successfully'}), 200

@payment_bp.route('/payments/<int:id>', methods=['DELETE'])
def delete_payment(id):
    payment = payment.query.get_or_404(id)
    db.session.delete(payment)
    db.session.commit()
    return jsonify({'message': 'Payment deleted successfully'}), 200
