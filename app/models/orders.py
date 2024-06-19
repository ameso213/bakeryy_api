from app.extensions import db
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Order(db.Model):
    __tablename__ = 'orders'  
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    order_date = db.Column(db.DateTime, nullable=False, default=datetime.now)

    def __init__(self, customer_id, product_id, status, quantity, total_price, order_date=None):
        self.customer_id = customer_id
        self.product_id = product_id
        self.status = status
        self.quantity = quantity
        self.total_price = total_price
        self.order_date = order_date if order_date else datetime.now()

    def get_order_details(self):
        return {
            'customer_id': self.customer_id,
            'product_id': self.product_id,
            'status': self.status,
            'quantity': self.quantity,
            'total_price': self.total_price,
            'order_date': self.order_date.strftime('%Y-%m-%d %H:%M:%S')  # Format date as string
        }

    # Relationships
    customer = db.relationship('User', back_populates='orders')
    product = db.relationship('Product', back_populates='orders')
