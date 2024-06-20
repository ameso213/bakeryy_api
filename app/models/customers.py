from app.extensions import db
from datetime import datetime
#from flask_sqlalchemy import SQLAlchemy

#db = SQLAlchemy()

class Customer(db.Model):
    __tablename__ = 'customers'  
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)  
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    contact = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    join_date = db.Column(db.DateTime, nullable=False, default=datetime.now())
    loyalty_points = db.Column(db.Integer, default=0)
    date_of_birth = db.Column(db.Date, nullable=True)
    gender = db.Column(db.String(10), nullable=True)

    # Relationships
    user = db.relationship('User', back_populates='customer')

    def __init__(self, user_id, first_name, last_name, email, contact, address, date_of_birth=None, gender=None):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.contact = contact
        self.address = address
        self.date_of_birth = date_of_birth
        self.gender = gender

    def update_contact(self, new_contact):
        self.contact = new_contact

    def update_address(self, new_address):
        self.address = new_address

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_customer_details(self):
        return {
            'user_id': self.user_id,
            'full_name': self.get_full_name(),
            'email': self.email,
            'contact': self.contact,
            'address': self.address,
            
            'loyalty_points': self.loyalty_points,
            'date_of_birth': self.date_of_birth.strftime('%Y-%m-%d') if self.date_of_birth else None,  # Format date as string
            'gender': self.gender
        }
