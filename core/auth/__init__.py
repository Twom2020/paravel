from config.auth import config
import hashlib, binascii, os
from core.auth.drivers.ApiAuthenticate import ApiAuthenticate


class Auth:
    @staticmethod
    def driver(driver=None):
        return AuthClass(driver)

    @staticmethod
    def login(user):
        return Auth.driver().login(user)

    @staticmethod
    def user():
        return Auth.driver().user()

    @staticmethod
    def login_by_id(id):
        return Auth.driver().login_by_id(id)

    @staticmethod
    def check():
        return Auth.driver().check()

    @staticmethod
    def logout():
        return Auth.driver().logout()

    @staticmethod
    def hash_password(password):
        """Hash a password for storing."""
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                      salt, 100000)
        pwdhash = binascii.hexlify(pwdhash)
        return (salt + pwdhash).decode('ascii')

    @staticmethod
    def verify_password(stored_password, provided_password):
        """Verify a stored password against one provided by user"""
        salt = stored_password[:64]
        stored_password = stored_password[64:]
        pwdhash = hashlib.pbkdf2_hmac('sha512',
                                      provided_password.encode('utf-8'),
                                      salt.encode('ascii'),
                                      100000)
        pwdhash = binascii.hexlify(pwdhash).decode('ascii')
        return pwdhash == stored_password


class AuthClass:
    def __init__(self, driver=None):
        self.config = config[driver if driver is not None else config['default']]
        if self.config['driver'] == "api":
            self.driver = ApiAuthenticate()

    def login(self, user):
        return self.driver.login(user)

    def user(self):
        return self.driver.user()

    def login_by_id(self, id):
        return self.driver.login_by_id(id)

    def check(self):
        return self.driver.check()

    def logout(self):
        return self.driver.logout()
