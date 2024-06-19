from app.extensions import db
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Ingredient(db.Model):
    __tablename__ = 'ingredients'  
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    unit = db.Column(db.String(20), nullable=False)
    supplier_id = db.Column(db.Integer, db.ForeignKey('suppliers.id'), nullable=False)

    supplier = db.relationship('Supplier', backref='ingredients')

    def __init__(self, name, quantity, unit, supplier_id):
        self.name = name
        self.quantity = quantity
        self.unit = unit
        self.supplier_id = supplier_id

    def get_ingredient_details(self):
        return {
            'id': self.id,
            'name': self.name,
            'quantity': self.quantity,
            'unit': self.unit,
            'supplier_id': self.supplier_id
        }
