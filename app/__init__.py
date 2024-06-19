from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

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
    from app.models.ingredients import Ingredient
    from app.models.inventory import Inventory
    from app.models.orders import Order
    from app.models.products import Product
    from app.models.users import User
    from app.models.orderItem import OrderItem
    from app.models.payment import Payment
    from app.models.address import Address
    from app.models.review import Review




    # Import controllers (ensure db is imported correctly in each controller)
    from app.controllers.auth.orders_controllers import orders_bp
    from app.controllers.auth.customers_controllers import customers_bp
    from app.controllers.auth.category_controllers import category_bp
    from app.controllers.auth.products_controllers import products_bp
    from app.controllers.auth.ingredients_controllers import ingredients_bp
    from app.controllers.auth.inventory_controllers import inventory_bp
    from app.controllers.auth.orderItem_controllers import order_item_bp
    from app.controllers.auth.payment_controllers import payment_bp
    from app.controllers.auth.review_controllers import review_bp
    from app.controllers.auth.address_controllers import address_bp


    # Register blueprints
    app.register_blueprint(orders_bp, url_prefix='/api')
    app.register_blueprint(customers_bp, url_prefix='/api')
    app.register_blueprint(category_bp, url_prefix='/api')
    app.register_blueprint(products_bp, url_prefix='/api')
    app.register_blueprint(ingredients_bp, url_prefix='/api')
    app.register_blueprint(inventory_bp, url_prefix='/api')
    app.register_blueprint(order_item_bp, url_prefix='/api')
    app.register_blueprint(payment_bp, url_prefix='/api')
    app.register_blueprint(address_bp, url_prefix='/api')
    app.register_blueprint(review_bp, url_prefix='/api')

    
    @app.route('/')
    def home():
        return "Welcome to our bakery shop"
    return app
    
