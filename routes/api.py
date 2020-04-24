from public.main import route
from app.controllers.AuthController import AuthController
AuthController = AuthController()

route.post('/login', AuthController.login)
route.post('/register', AuthController.register)
route.post('/user', AuthController.user)
route.post('/logout', AuthController.logout)
