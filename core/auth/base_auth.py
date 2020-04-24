from config.auth import config


class BaseAuth:
    def __init__(self):
        self.config = config[config['default']]
        self.secret = self.config['secret'] if 'secret' in self.config else 'secret'

    def login(self, user):
        pass

    def user(self):
        pass

    def login_by_id(self, id):
        pass

    def check(self):
        pass

    def logout(self):
        pass
