from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models import ingredients

ingredients_bp = Blueprint('ingredients', __name__)

@ingredients_bp.route('/ingredients', methods=['POST'])
def create_ingredient():
    data = request.get_json()

    new_ingredient = ingredients(
        name=data['name'],
        quantity=data['quantity'],
        unit=data['unit'],
        supplier_id=data['supplier_id']
    )

    db.session.add(new_ingredient)
    db.session.commit()

    return jsonify({'message': 'New ingredient created successfully!'}), 201

@ingredients_bp.route('/ingredients', methods=['GET'])
def get_ingredients():
    ingredients = ingredients.query.all()
    ingredients_list = []
    for ingredient in ingredients:
        ingredient_data = ingredient.get_ingredient_details()
        ingredients_list.append(ingredient_data)
    return jsonify(ingredients_list)

@ingredients_bp.route('/ingredients/<int:id>', methods=['GET'])
def get_ingredient(id):
    ingredient = ingredient.query.get_or_404(id)
    ingredient_data = ingredient.get_ingredient_details()
    return jsonify(ingredient_data)

@ingredients_bp.route('/ingredients/<int:id>', methods=['PUT'])
def update_ingredient(id):
    data = request.get_json()
    ingredient = ingredient.query.get_or_404(id)

    ingredient.name = data.get('name', ingredient.name)
    ingredient.quantity = data.get('quantity', ingredient.quantity)
    ingredient.unit = data.get('unit', ingredient.unit)
    ingredient.supplier_id = data.get('supplier_id', ingredient.supplier_id)

    db.session.commit()

    return jsonify({'message': 'Ingredient updated successfully!'})

@ingredients_bp.route('/ingredients/<int:id>', methods=['DELETE'])
def delete_ingredient(id):
    ingredient = ingredient.query.get_or_404(id)
    db.session.delete(ingredient)
    db.session.commit()

    return jsonify({'message': 'Ingredient deleted successfully!'})

# Remember to register the blueprint in your app
# from app.ingredients_controllers import ingredients_bp
# app.register_blueprint(ingredients_bp, url_prefix='/api')
