from flask import Blueprint
from core.route import Route


class Module:
    def __init__(self, name: str = None, __name: str = None):
        self.name = name
        self.__name = __name
        self.app = self.create_app()
        self.route = None
        self.prefix = "/" + name

    def boot(self):
        self.app = self.app()

    def create_app(self):
        return Blueprint(self.name, self.__name)

    def set_prefix(self, prefix):
        self.prefix = prefix
        return self

    def set_route(self):
        self.route = Route(self.app)
        return self

    def get_params(self):
        params = {}
        if self.prefix:
            params['url_prefix'] = self.prefix
        return params
