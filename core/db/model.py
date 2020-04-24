from orator import Model
from core.db import db

Model.set_connection_resolver(db)
