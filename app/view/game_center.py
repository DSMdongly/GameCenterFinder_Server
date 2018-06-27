from app.view.support.response_helper import unicode_safe_json_respnose
from app.view.support import api_helper

from app.doc.game_center import GAME_CENTER_GET_SPEC
from app.model.support import mongo_helper

from flask import Blueprint, request
from flask_restful import Api, Resource
from flasgger import swag_from


api = Api(Blueprint('game-center-api', __name__))


@api.resource('/center')
class GameCenterResource(Resource):
    @swag_from(GAME_CENTER_GET_SPEC)
    def get(self):
        centers = api_helper.search_game_centers(center_city_name=request.args.get('city_name'),
                                                 center_name=request.args.get('center_name'),
                                                 center_game_name=request.args.get('game_name'),
                                                 target_lng=request.args.get('target_lng'),
                                                 target_lat=request.args.get('target_lat'),
                                                 search_radius=request.args.get('search_radius'))

        center_dicts = [mongo_helper.mongo_doc_to_dict(c, ['games']) for c in centers]
        return unicode_safe_json_respnose(center_dicts)
