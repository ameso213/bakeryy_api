from flask import Blueprint, request, jsonify
from jwt import DecodeError
import validators
from app.models.User import User
from app.extensions import db, bcrypt
from flask_jwt_extended import create_access_token, jwt_required
from http import HTTPStatus

auth = Blueprint('auth', __name__, url_prefix='/api/v1/auth')

@auth.route('/register', methods=['POST'])
def register_user():
    data = request.json
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')
    password = data.get('password')
    user_type = data.get('user_type')

    if not all([first_name, last_name, email, password, user_type]):
        return jsonify({'error': 'All fields are required'}), HTTPStatus.BAD_REQUEST

    if len(password) < 8:
        return jsonify({'error': 'Password is too short'}), HTTPStatus.BAD_REQUEST

    if not validators.email(email):
        return jsonify({'error': 'Email is not valid'}), HTTPStatus.BAD_REQUEST

    try:
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        
        new_user = User(first_name=first_name, last_name=last_name, email=email, password=hashed_password, user_type=user_type)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({
            'message': f'{new_user.get_full_name()} has been successfully registered as an {new_user.user_type}',
            'user': {
                'id': new_user.id,
                'email': new_user.email,
                'first_name': new_user.first_name,
                'last_name': new_user.last_name,
            }
        }), HTTPStatus.CREATED

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to register user. Please try again later.'}), HTTPStatus.INTERNAL_SERVER_ERROR



@auth.route('/update_user/<int:id>', methods=['PUT'])
def update_user(id):
    user = User.query.get_or_404(id)
    data = request.get_json()
    try:
        if 'email' in data:
            user.email = data['email']
        if 'first_name' in data:
            user.first_name = data['first_name']
        if 'last_name' in data:
            user.last_name = data['last_name']
        if 'password' in data:
            user.password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
        if 'user_type' in data:
            user.user_type = data['user_type']

        db.session.commit()
        return jsonify({'message': 'User updated successfully'}), HTTPStatus.OK
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), HTTPStatus.BAD_REQUEST


@auth.route('/login', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')

    if not email or not password:
        return jsonify({'error': "Email and password are required"}), HTTPStatus.BAD_REQUEST

    user = User.query.filter_by(email=email).first()

    if user and bcrypt.check_password_hash(user.password, password):
        access_token = create_access_token(identity=user.id)
        return jsonify({
            'user': {
                'id': user.id,
                'email': user.email,
                'access_token': access_token,
            },
            'message': "You have successfully logged into your account"
        }), HTTPStatus.OK

    return jsonify({"error": "Invalid email or password"}), HTTPStatus.UNAUTHORIZED

@auth.route('/users', methods=['GET'])
def get_all_users():
    try:
        users = User.query.all()
        user_list = []
        for user in users:
            user_data = {
                'id': user.id,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'user_type': user.user_type,
                'created_at': user.created_at.strftime('%Y-%m-%d %H:%M:%S') if user.created_at else None,
                'updated_at': user.updated_at.strftime('%Y-%m-%d %H:%M:%S') if user.updated_at else None
            }
            user_list.append(user_data)

        return jsonify({'users': user_list}), HTTPStatus.OK

    except Exception as e:
        return jsonify({'error': str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR
    

@auth.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    try:
        user = User.query.get(user_id)
        if not user:
            return jsonify({'error': 'User not found'}), HTTPStatus.NOT_FOUND

        user_data = {
            'id': user.id,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'user_type': user.user_type,
            'created_at': user.created_at.strftime('%Y-%m-%d %H:%M:%S') if user.created_at else None,
            'updated_at': user.updated_at.strftime('%Y-%m-%d %H:%M:%S') if user.updated_at else None
        }

        return jsonify({'user': user_data}), HTTPStatus.OK

    except Exception as e:
        return jsonify({'error': str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR

@auth.route('/delete-user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        user = User.query.get(user_id)
        if not user:
            return jsonify({'error': 'User not found'}), HTTPStatus.NOT_FOUND

        db.session.delete(user)
        db.session.commit()

        return jsonify({'message': 'User deleted successfully'}), HTTPStatus.OK

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to delete user. Please try again later.'}), HTTPStatus.INTERNAL_SERVER_ERROR

