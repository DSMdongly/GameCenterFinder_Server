import os


class Config:
    DEBUG = False
    REMOTE_HOST = 'agcf.herokuapp.com'

    HOST = 'localhost'
    PORT = os.getenv('PORT', 5000)

    SERVICE_NAME = 'agcf'
    SECRET = os.getenv('SECRET_KEY', '78OC34B1ABC11263A357R8FBM99Y7221D7DB')

    SWAGGER = {
        'title': SERVICE_NAME,
        'specs_route': os.getenv('SWAGGER_URI', '/docs/'),
        'uiversion': 3,

        'info': {
            'title': SERVICE_NAME + ' API',
            'version': '1.0',
            'description': 'Arcade Game Center Finder Backend API Spec'
        },

        'schemes': [
            'https'
        ],

        'host': '{}'.format(REMOTE_HOST) if REMOTE_HOST else None,
        'basepath': '/',
    }

    if REMOTE_HOST is None:
        SWAGGER['host'] = '{}:{}'.format(HOST, PORT)

    MONGO = {
        'host': 'ds219040.mlab.com',
        'port': 19040,
        'db': '{}'.format(SERVICE_NAME),
        'username': 'gdh0608',
        'password': 'kim0608'
    }

    GOOGLE_MAPS = {
        'api_key': 'AIzaSyBKhlSA-XQ9WVLVw6OKw5g48PUDYn1gxHk'
    }

