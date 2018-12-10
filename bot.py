import os
from functools import wraps
from random import shuffle, choice

from dotenv import load_dotenv
import requests
from faker import Faker

load_dotenv()

NUMBER_USER = int(os.getenv('NUMBER_USER'))
MAX_POSTS_PER_USER = int(os.getenv('MAX_POSTS_PER_USER'))
MAX_LIKES_PER_USER = int(os.getenv('MAX_LIKES_PER_USER'))

HOST = os.getenv('HOST', 'localhost')
PORT = int(os.getenv('PORT', 8000))

BACKEND_URL = 'http://{host}:{port}/api/'.format(host=HOST, port=PORT)
URLS = {
    'signup': BACKEND_URL + 'signup/',
    'token': BACKEND_URL + 'token/',
    'posts': BACKEND_URL + 'posts/',
    'likes': BACKEND_URL + 'likes/',
}
fake = Faker()


def token_decorator(func):
    @wraps(func)
    def inner(self, *args, **kwargs):
        if self.token:
            return func(self, *args, **kwargs)
        raise Exception('Token is required!')
    return inner


class BotUser:
    def __init__(self, username=None, password=None, email=None, first_name=None, last_name=None):
        self.username = username or fake.user_name()
        self.password = password or fake.password()
        self.email = email or fake.email()
        self.first_name = first_name or fake.first_name()
        self.last_name = last_name or fake.first_name()

        self.user_data = {
            'username': self.username,
            'password': self.password,
        }
        self.user_data_extra = self.user_data.copy()
        self.user_data_extra.update({
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
        })
        self.token = None

    def generate_user(self):
        with requests.post(URLS['signup'], data=self.user_data_extra) as response:
            if response.status_code == 201:
                self.get_token()

    def get_token(self):
        with requests.post(URLS['token'], data=self.user_data) as response:
            if response.status_code == 200:
                self.token = response.json()['token']

    @token_decorator
    def generate_posts(self):
        for _ in range(MAX_POSTS_PER_USER):
            data = {
                'text': fake.text()
            }
            with requests.post(URLS['posts'], data=data, headers=self.headers) as response:
                if response.status_code == 201:
                    continue

    @token_decorator
    def generate_likes(self):
        post_ids = []
        with requests.get(URLS['posts']) as response:
            if response.status_code == 200:
                post_ids = [post['id'] for post in response.json()]
                shuffle(post_ids)

        for _ in range(MAX_LIKES_PER_USER):
            data = {
                'post_id': post_ids.pop(),
                'status': choice((-1, 0, 1)),
            }
            with requests.post(URLS['likes'], data=data, headers=self.headers) as response:
                if response.status_code == 200:
                    continue

    @property
    def headers(self):
        return {
            'Authorization': 'JWT ' + self.token
        }


class BotFactory:
    def __init__(self):
        self.user_bots = [BotUser() for _ in range(NUMBER_USER)]

    def run(self):
        self.generate_users()
        self.generate_posts()
        self.generate_likes()

    def generate_users(self):
        for user_bot in self.user_bots:
            user_bot.generate_user()

    def generate_posts(self):
        for user_bot in self.user_bots:
            user_bot.generate_posts()

    def generate_likes(self):
        for user_bot in self.user_bots:
            user_bot.generate_likes()


if __name__ == '__main__':
    factory = BotFactory()
    factory.run()
