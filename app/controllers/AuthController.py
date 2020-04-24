import core.request as request
from core.response import res
from cerberus import Validator
from app.models.User import User
from werkzeug.security import generate_password_hash, check_password_hash
from core.auth import Auth


class AuthController:
    def login(self):
        validator = Validator({
            "email": {
                "type": "string",
                "regex": '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',
                "required": True,
            },
            "password": {
                "type": "string",
                "minlength": 6,
                "required": True,
            },
        })
        validate = validator.validate(request.post())
        if not validate:
            return res().response(status_code=422, error=validator.errors)

        user = User.where("email", request.post('email')).first()

        if not user:
            return res().response(status_code=404)

        check_password = check_password_hash(user.password, request.post('password'))
        # check_password = Auth.verify_password(user.password, request.post('password'))

        if not check_password:
            return res().response(status_code=401)

        if Auth.login(user) is False:
            return res().response(message="error in login", status_code=400)

        user.token()

        return res().response(data=user.token.to_dict())

    def register(self):
        validator = Validator({
            "email": {
                "type": "string",
                "regex": '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',
                "required": True,
            },
            "username": {
                "type": "string",
                "maxlength": 60,
                "minlength": 5,
                "required": True,
            },
            "password": {
                "type": "string",
                "minlength": 6,
                "required": True,
            },
        })

        validate = validator.validate(request.post())

        if not validate:
            return res().response(status_code=422, error=validator.errors)

        user = User.create(
            username=request.post('username'),
            email=request.post('email'),
            # password=Auth.hash_password(request.post('password')),
            password=generate_password_hash(request.post('password')),
        )

        return res().response(data=user.to_dict())

    def user(self):
        user = Auth.user()
        if not user:
            return res().response(status_code=403)
        return res().response(data=user.to_dict())

    def logout(self):
        Auth.logout()
        return res().response()
