from mongoengine import *


class GameDeviceDocument(EmbeddedDocument):
    name = StringField()
    price = StringField()
    count = StringField()
    etc = StringField()


class GameCenterDocument(Document):
    meta = {
        'collection': 'game_center'
    }

    city = StringField()
    name = StringField()
    kind = StringField()
    address = StringField()
    location = PointField()
    opening = StringField()

    games = EmbeddedDocumentListField(GameDeviceDocument, default=list)
