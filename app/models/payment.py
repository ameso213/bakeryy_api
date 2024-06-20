from app.extensions import db
from datetime import datetime
#from flask_sqlalchemy import SQLAlchemy

#db = SQLAlchemy()

class Payment(db.Model):
    __tablename__ = 'payments'
    id = db.Column(db.Integer, primary_key=True)
    #order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    payment_method = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    transaction_id = db.Column(db.String(100), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)

    # Relationships
    order = db.relationship('Order', back_populates='payments')

    def __init__(self, order_id, amount, payment_method, status, transaction_id):
        self.order_id = order_id
        self.amount = amount
        self.payment_method = payment_method
        self.status = status
        self.transaction_id = transaction_id

    def get_payment_details(self):
        return {
            'id': self.id,
            'order_id': self.order_id,
            'amount': self.amount,
            'payment_method': self.payment_method,
            'status': self.status,
            'transaction_id': self.transaction_id,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }

    @staticmethod
    def get_payment_by_id(payment_id):
        return Payment.query.get(payment_id)

    def update_payment(self, amount=None, payment_method=None, status=None, transaction_id=None):
        if amount is not None:
            self.amount = amount
        if payment_method is not None:
            self.payment_method = payment_method
        if status is not None:
            self.status = status
        if transaction_id is not None:
            self.transaction_id = transaction_id
        db.session.commit()

    def delete_payment(self):
        db.session.delete(self)
        db.session.commit()
