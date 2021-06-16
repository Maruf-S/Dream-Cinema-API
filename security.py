from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp

from Dream_Cinema_API.models.user import *
from Dream_Cinema_API.resources.user import UsersRegister
from Dream_Cinema_API import bcrypt


def authenticate(username, password):
    user = UserModel.find_by_email(username)
    if user and bcrypt.check_password_hash(user.Password, password):
        return user

def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)











