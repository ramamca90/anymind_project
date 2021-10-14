'''
    It has authenticate related methods for FLASK APP
'''
from werkzeug.security import safe_str_cmp
from src.user import User

# only below users can access this API , TODO - passwords hardcoded here, should be encrypted
users = [
    User(1, 'user1', 'password1'),
    User(2, 'user2', 'password2'),
]

username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}


def authenticate(username, password):
    user = username_table.get(username, None)
    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)
