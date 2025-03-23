import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "my_super_secret_key_123")  # Change this!
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"  # Use SQLite for local database
    SQLALCHEMY_TRACK_MODIFICATIONS = False
