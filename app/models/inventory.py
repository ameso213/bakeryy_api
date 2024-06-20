from datetime import datetime
from app.extensions import db
#from flask_sqlalchemy import SQLAlchemy

#b = SQLAlchemy()

class Inventory(db.Model):
    __tablename__ = 'inventory'
    id = db.Column(db.Integer, primary_key=True)
    #product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    restock_date = db.Column(db.DateTime, nullable=False, default=datetime.now)
    location = db.Column(db.String(255), nullable=True)
    #supplier_id = db.Column(db.Integer, db.ForeignKey('supplier.id'), nullable=True)

    # Relationships
    product = db.relationship('Product', back_populates='inventories')
    supplier = db.relationship('Supplier', back_populates='inventories')

    def __init__(self, product_id, quantity, location, supplier_id, restock_date=None):
        self.product_id = product_id
        self.quantity = quantity
        self.location = location
        self.supplier_id = supplier_id
        self.restock_date = restock_date if restock_date else datetime.utcnow()

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity

    def update_restock_date(self, new_restock_date):
        self.restock_date = new_restock_date

    def update_location(self, new_location):
        self.location = new_location

    def update_supplier(self, new_supplier):
        self.supplier = new_supplier

    def get_inventory_details(self):
        return {
            'product_id': self.product_id,
            'quantity': self.quantity,
            'location': self.location,
            'supplier_id': self.supplier_id,
            'restock_date': self.restock_date.strftime('%Y-%m-%d %H:%M:%S')  # Format date as string
        }
