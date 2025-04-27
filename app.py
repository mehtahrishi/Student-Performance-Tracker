from flask import Flask
from config import Config
from flask_pymongo import PyMongo

app = Flask(__name__, template_folder="templates")
app.config.from_object(Config)

# Initialize PyMongo with Flask app
mongo = PyMongo(app)

# Import routes after setting up mongo
from routes import *

if __name__ == "__main__":
    app.run(debug=True)
