from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, template_folder="templates")
app.config.from_object(Config)

db = SQLAlchemy(app)

from routes import *

if __name__ == "__main__":
    app.run(debug=True)
