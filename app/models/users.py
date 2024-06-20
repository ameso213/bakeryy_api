from app.extensions import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    user_type = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    first_name = db.Column(db.String(50), nullable=True)
    last_name = db.Column(db.String(50), nullable=True)
    contact = db.Column(db.String(20), nullable=True)
    
    # Define relationship with Address model
    addresses = db.relationship('Address', backref='user', lazy=True)

    def __init__(self, first_name, last_name, email, contact, password, user_type):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.contact = contact
        self.password = password
        self.user_type = user_type

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
