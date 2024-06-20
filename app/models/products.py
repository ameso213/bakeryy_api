from datetime import datetime
from app.extensions import db
#from flask_sqlalchemy import SQLAlchemy


#db = SQLAlchemy()

class Product(db.Model):
    __tablename__ = 'products' 
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    #category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)  # Corrected foreign key reference
    stock_quantity = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(255), nullable=True)  # URL or file path
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

   

    def __init__(self, name, description, price, category_id, stock_quantity, image=None):
        self.name = name
        self.description = description
        self.price = price
        self.category_id = category_id
        self.stock_quantity = stock_quantity
        self.image = image

    def get_full_product_name(self):
        return self.name
