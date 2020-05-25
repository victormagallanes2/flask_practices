from . import authentication

@authentication.route('/')
def authentication():
    return 'Hello, authentication'