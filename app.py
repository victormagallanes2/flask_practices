import os
from flask import Flask
from .users.models import db
from .users import blueprint as users
from .authentication import blueprint as authentication
from flask_restx import Api, Resource
from dotenv import load_dotenv


def create_app():
    # Variables
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dotenv_path = os.path.join(BASE_DIR, '.env')
    load_dotenv(dotenv_path)
    # Fask instance
    app = Flask(__name__)
    # Data base config
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}/flask_practices/test.db'.format(BASE_DIR)
    db.init_app(app)
    # Register Blueprint
    app.register_blueprint(users)
    app.register_blueprint(authentication)
    return app
