from .AuthToken import AuthToken
from orator.orm import has_one


class HasApiToken:
    @has_one
    def token(self):
        return AuthToken
