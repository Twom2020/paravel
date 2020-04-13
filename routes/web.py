from public.main import route
from app.controllers.HomeController import HomeController

HomeController = HomeController()


def home_groups():
    route.get('/test', HomeController.test)


route.group("/home", home_groups)

route.post("/index", HomeController.index)
