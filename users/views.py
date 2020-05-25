from . import users

@users.route('/')
def hello():
    return 'Hello, users'