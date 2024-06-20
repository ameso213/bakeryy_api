from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models import category

category_bp = Blueprint('category', __name__, url_prefix='/api/v1/category')

@category_bp.route('/categories', methods=['POST'])
def create_category():
    data = request.get_json()

    new_category = category(
        name=data['name'],
        description=data.get('description')
    )

    db.session.add(new_category)
    db.session.commit()

    return jsonify({'message': 'New category created successfully!'}), 201

@category_bp.route('/categories', methods=['GET'])
def get_categories():
    categories = category.query.all()
    categories_list = []
    for category in categories:
        category_data = {
            'id': category.id,
            'name': category.name,
            'description': category.description
        }
        categories_list.append(category_data)
    return jsonify(categories_list)

@category_bp.route('/categories/<int:id>', methods=['GET'])
def get_category(id):
    category = category.query.get_or_404(id)
    category_data = {
        'id': category.id,
        'name': category.name,
        'description': category.description
    }
    return jsonify(category_data)

@category_bp.route('/categories/<int:id>', methods=['PUT'])
def update_category(id):
    data = request.get_json()
    category = category.query.get_or_404(id)

    category.name = data.get('name', category.name)
    category.description = data.get('description', category.description)

    db.session.commit()

    return jsonify({'message': 'Category updated successfully!'})

@category_bp.route('/categories/<int:id>', methods=['DELETE'])
def delete_category(id):
    category = category.query.get_or_404(id)
    db.session.delete(category)
    db.session.commit()

    return jsonify({'message': 'Category deleted successfully!'})

# Remember to register the blueprint in your app
# from app.category_controllers import category_bp
# app.register_blueprint(category_bp, url_prefix='/api')
