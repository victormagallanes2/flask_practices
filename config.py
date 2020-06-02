


class Config(object):
    import os
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DEBUG = False
    SECRET_KEY = 'SUPER_SECRET'
    TESTING = False
    DATABASE_URI = 'sqlite:///{}/flask_practices/test.db'.format(BASE_DIR)


class Local(Config):
    DEBUG = True


class Testing(Config):
    TESTING = True


class Production(Config):
    TESTING = True

	 
		
