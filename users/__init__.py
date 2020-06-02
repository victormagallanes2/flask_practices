from flask import Blueprint
from flask_restx import Api


blueprint = Blueprint('users', __name__, url_prefix='/api/')
api_user = Api(blueprint)

from . import views

