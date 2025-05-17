import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "my_super_secret_key_123")
    # MongoDB Atlas URI: Replace <db_password> with your actual password
    MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://mehtahrishi45:mehtahrishi45@cluster0.zbozo.mongodb.net/Student_List?retryWrites=true&w=majority&appName=Cluster0")
