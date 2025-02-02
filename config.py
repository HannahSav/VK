import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://username:password@localhost/ecommerce_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MEDIA_FOLDER = os.getenv('MEDIA_FOLDER', 'media/')
