from . import api_authentication
from flask_restx import Resource


authentication = api_authentication.namespace('authentication', description='authentication operations')

@authentication.route('/<id>')
@authentication.doc(params={'id': 'An ID'})
class Authentication(Resource):

    def get(self, id):
        return {'token': 'token'}

    @authentication.doc(responses={403: 'Not Authorized'})
    def post(self, id):
        api.abort(403)