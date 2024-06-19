from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models import inventory
from datetime import datetime

inventory_bp = Blueprint('inventory', __name__)

@inventory_bp.route('/inventory', methods=['POST'])
def create_inventory():
    data = request.get_json()

    new_inventory =inventory(
        product_id=data['product_id'],
        quantity=data['quantity'],
        location=data.get('location'),
        supplier_id=data.get('supplier_id'),
        restock_date=datetime.strptime(data['restock_date'], '%Y-%m-%d %H:%M:%S') if data.get('restock_date') else None
    )

    db.session.add(new_inventory)
    db.session.commit()

    return jsonify({'message': 'New inventory record created successfully!'}), 201

@inventory_bp.route('/inventory', methods=['GET'])
def get_inventory():
    inventories = inventory.query.all()
    inventories_list = []
    for inventory in inventories:
        inventory_data = inventory.get_inventory_details()
        inventories_list.append(inventory_data)
    return jsonify(inventories_list)

@inventory_bp.route('/inventory/<int:id>', methods=['GET'])
def get_inventory_record(id):
    inventory = inventory.query.get_or_404(id)
    inventory_data = inventory.get_inventory_details()
    return jsonify(inventory_data)

@inventory_bp.route('/inventory/<int:id>', methods=['PUT'])
def update_inventory(id):
    data = request.get_json()
    inventory = inventory.query.get_or_404(id)

    inventory.product_id = data.get('product_id', inventory.product_id)
    inventory.quantity = data.get('quantity', inventory.quantity)
    inventory.location = data.get('location', inventory.location)
    inventory.supplier_id = data.get('supplier_id', inventory.supplier_id)
    inventory.restock_date = datetime.strptime(data['restock_date'], '%Y-%m-%d %H:%M:%S') if data.get('restock_date') else inventory.restock_date

    db.session.commit()

    return jsonify({'message': 'Inventory record updated successfully!'})

@inventory_bp.route('/inventory/<int:id>', methods=['DELETE'])
def delete_inventory(id):
    inventory = inventory.query.get_or_404(id)
    db.session.delete(inventory)
    db.session.commit()

    return jsonify({'message': 'Inventory record deleted successfully!'})

# Remember to register the blueprint in your app
# from app.inventory_controllers import inventory_bp
# app.register_blueprint(inventory_bp, url_prefix='/api')
