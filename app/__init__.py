from flask import Flask
from .extensions import api, db
from.resources import ns

def create_app():
    app = Flask(__name__)

    # Configuration
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Initialize extensions
    api.init_app(app)
    db.init_app(app)
    
    api.add_namespace(ns)

    return app
app = create_app()
