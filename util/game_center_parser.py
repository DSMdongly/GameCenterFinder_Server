from arcapi import get_game_centers_from_city, CITIES
from app.model.game_center import GameCenterDocument, GameDeviceDocument
from util.google_maps_helper import get_location_data_from_address


def parse():
    print('[info] arcade game center parsing was started')

    # parse arcade game centers
    _parse()

    print('[info] arcade game center parsing was finished')


def _parse():
    GameCenterDocument.drop_collection()

    for city_name in CITIES:
        print('[info] parsing game centers from {0}'.format(city_name))
        centers = get_game_centers_from_city(city_name)

        for c in centers:
            center = GameCenterDocument(city=city_name, name=c['name'])
            center.address = c.get('address')
            center.opening = c.get('opening')

            if center.address is not None:
                # Get Latitude and Longitude from Address
                location = get_location_data_from_address(center.address)
                center.location = [location['lng'], location['lat']]

            for g in c['games']:
                game = GameDeviceDocument(name=g['name'])
                game.price = g['price']
                game.count = g['count']
                game.etc = g['etc']

                center.games.append(game)

            center.save()
