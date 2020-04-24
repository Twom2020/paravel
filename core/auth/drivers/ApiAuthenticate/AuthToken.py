from core.db.model import Model


class AuthToken(Model):
    __fillable__ = ['user_id', 'token', 'expire_time', 'created_at']
    __timestamps__ = False

    def user(self):
        return self.belongs_to('users', 'user_id')
