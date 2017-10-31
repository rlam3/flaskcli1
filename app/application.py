from flask_script import Manager, Shell, Server

from flask import Flask
from app.extensions import db

def create_app():
    app = Flask(__name__)

    register_extensions(app)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    return app

def register_extensions(app):
    db.init_app(app)
