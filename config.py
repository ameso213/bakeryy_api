# config.py

import os

class Config:
    # Database configuration
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/bakery_api'

    # JWT secret key configuration
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'BAKE256')
