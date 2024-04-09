import random
from config import Config


class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    @classmethod
    def create(cls, new_user=False):
        if new_user:
            random_suffix = random.randint(100, 999)
            username = f'{Config.RND_USER_NAME_PREFIX}{random_suffix}'
            email = f'{Config.RND_USER_NAME_PREFIX}{random_suffix}@{Config.RND_USER_MAIL_DOMAIN}'
            password = f'{random.randint(100000, 999999)}'
        else:
            username = Config.REGISTERED_USER_NAME
            email = Config.REGISTERED_USER_EMAIL
            password = Config.REGISTERED_USER_PASSWORD

        return cls(username, email, password)
