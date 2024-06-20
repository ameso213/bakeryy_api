from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models import users  # Ensure correct import
from werkzeug.security import generate_password_hash, check_password_hash

users_bp = Blueprint('users', __name__, url_prefix='/api/v1/auth')

@users_bp.route('/create', methods=['POST'])
def create_user():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='sha256')
    
    new_user = users(
        first_name=data.get('first_name'),
        last_name=data.get('last_name'),
        email=data['email'],
        contact=data.get('contact'),
        password=hashed_password,
        user_type=data['user_type']
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'New user created successfully!'}), 201

@users_bp.route('/users', methods=['GET'])
def get_users():
    users = users.query.all()  # Correct model name
    users_list = []
    for user in users:
        user_data = {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'contact': user.contact,
            'user_type': user.user_type
        }
        users_list.append(user_data)
    return jsonify(users_list)

@users_bp.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = users.query.get_or_404(id)  # Correct model name
    user_data = {
        'id': user.id,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'contact': user.contact,
        'user_type': user.user_type
    }
    return jsonify(user_data)

@users_bp.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    user = users.query.get_or_404(id)  # Correct model name

    user.first_name = data.get('first_name', user.first_name)
    user.last_name = data.get('last_name', user.last_name)
    user.email = data.get('email', user.email)
    user.contact = data.get('contact', user.contact)
    user.user_type = data.get('user_type', user.user_type)

    if 'password' in data:
        user.password = generate_password_hash(data['password'], method='sha256')

    db.session.commit()

    return jsonify({'message': 'User updated successfully!'})

@users_bp.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = users.query.get_or_404(id)  # Correct model name
    db.session.delete(user)
    db.session.commit()

    return jsonify({'message': 'User deleted successfully!'})
