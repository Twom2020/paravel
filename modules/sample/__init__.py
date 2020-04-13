from core.module import Module
sample = Module('sample_module', __name__).set_prefix(False).set_route()

from .routes import web