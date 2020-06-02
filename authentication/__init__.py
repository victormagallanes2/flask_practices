from flask import Blueprint
from flask_restx import Api


blueprint = Blueprint('authentication', __name__, url_prefix='/api/')
api_authentication = Api(blueprint)

from . import views

