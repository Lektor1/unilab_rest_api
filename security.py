from models.user import UserModel
from werkzeug.security import safe_str_cmp


def authentication(username, password):
    user = UserModel.find_by_username(username)

    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload):
    user_id = payload['identity']
    user = UserModel.find_by_userid(user_id)
    if user:
        return user
