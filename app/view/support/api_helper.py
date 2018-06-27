from app.model.game_center import GameCenterDocument
from bson.objectid import ObjectId


def paging_items(items, page_index, page_length):
    # get start and end index to slicing object
    start_index = (page_index - 1) * page_length
    end_index = page_index * page_length

    # return sliced items
    return items[start_index:end_index]


def search_game_centers(**kwargs):
    # dictionary for store mongo engine query
    query = {}

    # argument for name based search game center
    city_name = kwargs.get('city_name')
    center_name = kwargs.get('center_name')
    game_name = kwargs.get('game_name')

    # argument for location based search game center
    target_lng = kwargs.get('target_lng')
    target_lat = kwargs.get('target_lat')
    search_radius = kwargs.get('search_radius')

    # generate city query to find by city name
    if city_name:
        query['city'] = city_name

    # generate name__icontains query to find by game center name
    if center_name:
        query['name__icontains'] = center_name

    # generate games__match query to find by game device name in game list
    if game_name:
        query['games__match'] = {'name': game_name}

    # generate near query to find by target longitude and latitude
    if target_lng and target_lat:
        query['location__near'] = [float(target_lng), float(target_lat)]

        # generate max_distance to determine search radius
        if search_radius:
            query['location__max_distance'] = int(search_radius)

    # execute query with query parameter dictionary
    result = GameCenterDocument.objects(**query)

    return result


def search_games_from_game_center(center_id):
    centers = GameCenterDocument.objects(id=ObjectId(center_id))

    if not centers:
        return None

    center = centers[0]
    return center.games


