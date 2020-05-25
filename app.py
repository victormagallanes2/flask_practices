from flask import Flask
from .settings import Settings
from .users import users
from .authentication import authentication


def create_app():
    app = Flask(__name__)
    app.config.from_object(Settings)
    app.register_blueprint(users)
    app.register_blueprint(authentication)
    return app
