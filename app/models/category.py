from app.extensions import db
from datetime import datetime
#from flask_sqlalchemy import SQLAlchemy

#b = SQLAlchemy()




class Category(db.Model):
    __tablename__ = 'category'  
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(255), nullable=True)

    def __repr__(self): 
        return f'<Category {self.name}>'

    @staticmethod
    def get_category_by_id(category_id):
        return Category.query.get(category_id)

    def update_category(self, name=None, description=None):
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        db.session.commit()

    def delete_category(self):
        db.session.delete(self)
        db.session.commit()
