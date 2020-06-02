from . import api_user
from flask_restx import Resource


users = api_user.namespace('users', description='Users operations')

@users.route('/<id>')
@users.doc(params={'id': 'An ID'})
class Users(Resource):

    def get(self, id):
        return {}

    @users.doc(responses={403: 'Not Authorized'})
    def post(self, id):
        api.abort(403)