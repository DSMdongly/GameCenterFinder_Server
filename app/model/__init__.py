from mongoengine import *


class Mongo:
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        # get mongo config
        mongo = app.config['MONGO']

        # initialize mongo connection
        connect(db=mongo['db'],
                host=mongo['host'],
                port=mongo['port'],
                username=mongo.get('username'),
                password=mongo.get('password'))
