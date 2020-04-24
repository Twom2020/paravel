from core.auth.base_auth import BaseAuth
from .AuthToken import AuthToken
from flask import request
import jwt, datetime, random, string


class ApiAuthenticate(BaseAuth):

    def login(self, user):
        return self.login_by_id(user.id)

    def login_by_id(self, id):
        try:
            expire_time = str(
                datetime.datetime.now()
                +
                datetime.timedelta(minutes=(self.config['expire_time'] if 'expire_time' in self.config else (1 * 60)))
            )
            letters = string.ascii_lowercase
            token = jwt.encode({
                "data": str(id) + ":::" + str(request.user_agent) + ":::" + str(request.remote_addr),
                "random": ''.join(random.choice(letters) for i in range(120)),
                "user_agent": str(request.user_agent),
                "ip": request.remote_addr,
                "expire_time": expire_time
            }, self.secret)

            AuthToken.create({
                "user_id": id,
                "token": token,
                "expire_time": expire_time,
                "created_at": datetime.datetime.now(),
            })
            return True
        except:
            return False

    def user(self):
        token = request.headers.get('Authorization')
        check = AuthToken.where("token", token).where("expire_time", ">", datetime.datetime.now()).first()
        if not check:
            return False
        return check.user()

    def logout(self):
        token = request.headers.get('Authorization')
        AuthToken.where("token", token).delete()
        return True
