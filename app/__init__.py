from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt

from flask_jwt_extended import JWTManager
from config import Config


from app.extensions import db, migrate

def create_app():
    app = Flask(__name__)

    # Load configuration
    app.config.from_object(Config)

    # Initialize SQLAlchemy and Migrate
    db.init_app(app)
    migrate.init_app(app, db)

    # Import models (ensure db is imported correctly in each model)
    from app.models.category import Category
    from app.models.customers import Customer
    
    from app.models.inventory import Inventory
    from app.models.orders import Order
    from app.models.products import Product
    from app.models.User import User
    


    # Import controllers (ensure db is imported correctly in each controller)
    from app.controllers.auth.orders_controllers import orders_bp
    from app.controllers.auth.customers_controllers import customers_bp
    from app.controllers.auth.category_controllers import category_bp
    from app.controllers.auth.products_controllers import products_bp
    
    from app.controllers.auth.inventory_controllers import inventory_bp
    
    from app.controllers.auth.users_controllers import auth


    # Register blueprints
    app.register_blueprint(orders_bp, url_prefix='/api')
    app.register_blueprint(customers_bp, url_prefix='/api')
    app.register_blueprint(category_bp, url_prefix='/api')
    app.register_blueprint(products_bp, url_prefix='/api')
    
    app.register_blueprint(inventory_bp, url_prefix='/api')
    
    
    app.register_blueprint(auth, url_prefix='/api/v1/auth')
    
    @app.route('/')
    def home():
        return "Welcome to our bakery shop"
    return app
    
