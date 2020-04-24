from flask import Flask

main_app = Flask(__name__)

from core.route import Route

route = Route.bind(main_app)

import routes.web
import routes.api

from modules import modules

for module in modules:
    main_app.register_blueprint(module.app, **module.get_params())
