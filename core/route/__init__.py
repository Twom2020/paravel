class Route:
    prefix_str = ''
    namespace_str = ''

    @staticmethod
    def bind(app):
        return Route(app)

    def __init__(self, app):
        self.app = app
        self.last_prefix_str = ''

    def get(self, route, controller):
        self.add_route(route, controller, methods=['GET'])

    def post(self, route, controller):
        self.add_route(route, controller, methods=['POST'])

    def add_route(self, route, controller, **params):
        route = Route.prefix_str + route
        self.app.route(route, **params)(controller)

    def group(self, prefix, callback: callable):
        self.last_prefix_str = Route.prefix_str
        Route.prefix_str = prefix
        callback()
        Route.prefix_str = self.last_prefix_str
        self.last_prefix_str = ''
