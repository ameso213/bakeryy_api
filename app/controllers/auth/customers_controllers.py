from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models import customers
from datetime import datetime

customers_bp = Blueprint('customers', __name__, url_prefix='/api/v1/customers',)

@customers_bp.route('/create', methods=['POST'])
def create_customer():
    data = request.get_json()

    new_customer = customers(
        user_id=data['user_id'],
        first_name=data['first_name'],
        last_name=data['last_name'],
        email=data['email'],
        contact=data['contact'],
        address=data['address'],
        date_of_birth=datetime.strptime(data['date_of_birth'], '%Y-%m-%d') if data.get('date_of_birth') else None,
        gender=data.get('gender')
    )

    db.session.add(new_customer)
    db.session.commit()

    return jsonify({'message': 'New customer created successfully!'}), 201

@customers_bp.route('/get', methods=['GET'])
def get_customers():
    customers = customers.query.all()
    customers_list = []
    for customer in customers:
        customer_data = customer.get_customer_details()
        customers_list.append(customer_data)
    return jsonify(customers_list)

@customers_bp.route('/customers/<int:id>', methods=['GET'])
def get_customer(id):
    customer = customers.query.get_or_404(id)
    customer_data = customer.get_customer_details()
    return jsonify(customer_data)

@customers_bp.route('/customers/<int:id>', methods=['PUT'])
def update_customer(id):
    data = request.get_json()
    customer = customer.query.get_or_404(id)

    customer.first_name = data.get('first_name', customer.first_name)
    customer.last_name = data.get('last_name', customer.last_name)
    customer.email = data.get('email', customer.email)
    customer.contact = data.get('contact', customer.contact)
    customer.address = data.get('address', customer.address)
    customer.date_of_birth = datetime.strptime(data['date_of_birth'], '%Y-%m-%d') if data.get('date_of_birth') else customer.date_of_birth
    customer.gender = data.get('gender', customer.gender)

    db.session.commit()

    return jsonify({'message': 'Customer updated successfully!'})

@customers_bp.route('/customers/<int:id>', methods=['DELETE'])
def delete_customer(id):
    customer = customers.query.get_or_404(id)
    db.session.delete(customer)
    db.session.commit()

    return jsonify({'message': 'Customer deleted successfully!'})

# Remember to register the blueprint in your app
# from app.customers_controllers import customers_bp
# app.register_blueprint(customers_bp, url_prefix='/api')
