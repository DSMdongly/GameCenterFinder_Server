class Router:
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        from app.view import game_center
        app.register_blueprint(game_center.api.blueprint)

        from app.view import game
        app.register_blueprint(game.api.blueprint)
