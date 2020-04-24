from core.db.model import Model
from core.auth.drivers.ApiAuthenticate.HasApiToken import HasApiToken


class User(Model, HasApiToken):
    __fillable__ = ['username', 'email', 'password']
    __hidden__ = ['password']
    __timestamps__ = False
