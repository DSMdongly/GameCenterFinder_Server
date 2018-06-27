from flask import Blueprint, request
from flask_restful import Api, Resource
from flasgger import swag_from

from app.doc.game import GAME_GET_SPEC
from app.view.support import api_helper, response_helper
from app.model.support import mongo_helper

api = Api(Blueprint('game-in-game-center-api', __name__))


@api.resource('/game')
class GameResource(Resource):
    @swag_from(GAME_GET_SPEC)
    def get(self):
        center_id = request.args['center_id']
        games = api_helper.search_games_from_game_center(center_id)

        if games is None:
            return 204, 'we could not found game center (Id: {})'.format(center_id)

        game_dicts = mongo_helper.mongo_set_to_python_list(games)
        return response_helper.unicode_safe_json_respnose(game_dicts)

