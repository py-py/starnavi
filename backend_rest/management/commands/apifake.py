import os
from random import shuffle, choice

from django.urls import reverse
from django.core.management.base import BaseCommand
from dotenv import load_dotenv
from faker import Faker
from rest_framework.test import APIClient

load_dotenv()
NUMBER_USER = int(os.getenv('NUMBER_USER', 0))
MAX_POSTS_PER_USER = int(os.getenv('MAX_POSTS_PER_USER', 0))
MAX_LIKES_PER_USER = int(os.getenv('MAX_LIKES_PER_USER', 0))
fake = Faker()


class UserBot:
    def __init__(self):
        self.user_data = {
            'username': fake.user_name(),
            'password': fake.password(),
        }
        self.user_data_extra = self.user_data.copy()
        self.user_data_extra.update({
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'email': fake.email(),
        })
        self.client = APIClient()
        self.token = None

    def create_user(self):
        user_response = self.client.post(reverse('signup-list'), data=self.user_data_extra)
        if user_response.status_code == 201:
            token_response = self.client.post(reverse('token'), data=self.user_data)
            token_data = token_response.json()
            self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token_data['token'])
        else:
            raise Exception(user_response.json())

    def generate_posts(self):
        for _ in range(MAX_POSTS_PER_USER):
            post_data = {
                'text': fake.text(),
            }
            self.client.post(reverse('post-list'), data=post_data)

    def generate_likes(self):
        post_response = self.client.get(reverse('post-list'))
        post_data = post_response.json()
        post_ids = [post['id'] for post in post_data]
        shuffle(post_ids)
        for _ in range(MAX_LIKES_PER_USER):
            like_data = {
                'post_id': post_ids.pop(),
                'status': choice((-1, 0, 1))
            }
            self.client.post(reverse('likes'), data=like_data)


class Command(BaseCommand):
    help = 'Insert fake data in database using api'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def handle(self, *args, **options):
        bots = []
        for _ in range(NUMBER_USER):
            bot = UserBot()
            bot.create_user()
            bot.generate_posts()
            bots.append(bot)

        for bot in bots:
            bot.generate_likes()
