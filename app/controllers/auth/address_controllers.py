from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models import address

address_bp = Blueprint('address', __name__, url_prefix='/api/v1/address')

@address_bp.route('/create', methods=['POST'])
def create_address():
    data = request.get_json()

    new_address = address(
        users_id=data['users_id'],
        address_line1=data['address_line1'],
        address_line2=data.get('address_line2', None),
        city=data['city'],
        state=data['state'],
        zip_code=data['zip_code'],
        country=data['country']
    )

    db.session.add(new_address)
    db.session.commit()

    return jsonify({'message': 'New address created successfully!'}), 201

@address_bp.route('/addresses', methods=['GET'])
def get_addresses():
    addresses = address.query.all()
    addresses_list = []
    for address in addresses:
        address_data = {
            'id': address.id,
            'users_id': address.users_id,
            'address_line1': address.address_line1,
            'address_line2': address.address_line2,
            'city': address.city,
            'state': address.state,
            'zip_code': address.zip_code,
            'country': address.country
        }
        addresses_list.append(address_data)
    return jsonify(addresses_list)

@address_bp.route('/addresses/<int:id>', methods=['GET'])
def get_address(id):
    address = address.query.get_or_404(id)
    address_data = {
        'id': address.id,
        'users_id': address.users_id,
        'address_line1': address.address_line1,
        'address_line2': address.address_line2,
        'city': address.city,
        'state': address.state,
        'zip_code': address.zip_code,
        'country': address.country
    }
    return jsonify(address_data)

@address_bp.route('/addresses/<int:id>', methods=['PUT'])
def update_address(id):
    data = request.get_json()
    address = address.query.get_or_404(id)

    address.address_line1 = data.get('address_line1', address.address_line1)
    address.address_line2 = data.get('address_line2', address.address_line2)
    address.city = data.get('city', address.city)
    address.state = data.get('state', address.state)
    address.zip_code = data.get('zip_code', address.zip_code)
    address.country = data.get('country', address.country)

    db.session.commit()

    return jsonify({'message': 'Address updated successfully!'})

@address_bp.route('/addresses/<int:id>', methods=['DELETE'])
def delete_address(id):
    address = address.query.get_or_404(id)
    db.session.delete(address)
    db.session.commit()

    return jsonify({'message': 'Address deleted successfully!'})
