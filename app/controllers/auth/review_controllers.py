from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models import review, users, products
from datetime import datetime

review_bp = Blueprint('review_bp', __name__, url_prefix='/api/v1/review')

@review_bp.route('/create', methods=['POST'])
def create_review():
    data = request.get_json()

    user_id = data.get('user_id')
    product_id = data.get('product_id')
    rating = data.get('rating')
    comment = data.get('comment')

    # Check if user_id and product_id exist
    user = users.query.get(user_id)
    product = product.query.get(product_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    if not product:
        return jsonify({'error': 'Product not found'}), 404

    new_review = review(user_id=user_id, product_id=product_id, rating=rating, comment=comment)
    db.session.add(new_review)
    db.session.commit()

    return jsonify({'message': 'Review created successfully', 'review_id': new_review.id}), 201

@review_bp.route('/reviews', methods=['GET'])
def get_reviews():
    reviews = review.query.all()
    review_list = []
    for review in reviews:
        review_data = {
            'id': review.id,
            'user_id': review.user_id,
            'product_id': review.product_id,
            'rating': review.rating,
            'comment': review.comment,
            'created_at': review.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }
        review_list.append(review_data)

    return jsonify(review_list)

@review_bp.route('/reviews/<int:id>', methods=['GET'])
def get_review(id):
    review = review.query.get_or_404(id)
    review_data = {
        'id': review.id,
        'user_id': review.user_id,
        'product_id': review.product_id,
        'rating': review.rating,
        'comment': review.comment,
        'created_at': review.created_at.strftime('%Y-%m-%d %H:%M:%S')
    }

    return jsonify(review_data)

@review_bp.route('/reviews/<int:id>', methods=['PUT'])
def update_review(id):
    data = request.get_json()
    review = review.query.get_or_404(id)

    review.rating = data.get('rating', review.rating)
    review.comment = data.get('comment', review.comment)

    db.session.commit()

    return jsonify({'message': 'Review updated successfully'})

@review_bp.route('/reviews/<int:id>', methods=['DELETE'])
def delete_review(id):
    review = review.query.get_or_404(id)
    db.session.delete(review)
    db.session.commit()

    return jsonify({'message': 'Review deleted successfully'})
