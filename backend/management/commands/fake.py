import os
from random import choice, shuffle

from faker import Faker
from dotenv import load_dotenv
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from backend.models import *


class Command(BaseCommand):
    help = 'Insert fake data in database'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.users = []
        self.fake = Faker()


    def handle(self, *args, **options):
        load_dotenv()

        NUMBER_USER = os.getenv('NUMBER_USER', 0)
        MAX_POSTS_PER_USER = os.getenv('MAX_POSTS_PER_USER', 0)
        MAX_LIKES_PER_USER = os.getenv('MAX_LIKES_PER_USER', 0)

        self.generate_users(int(NUMBER_USER))
        self.generate_posts(int(MAX_POSTS_PER_USER))
        self.generate_likes(int(MAX_LIKES_PER_USER))

    def generate_users(self, count):
        for _ in range(count):
            user = User.objects.create_user(
                username=self.fake.user_name(),
                password=self.fake.password(),
                first_name=self.fake.first_name(),
                last_name=self.fake.last_name(),
                email=self.fake.email(),
            )
            self.users.append(user)

    def generate_posts(self, count):
        for user in self.users:
            posts = [Post(
                text=self.fake.text(),
                user=user,
                # date=self.fake.past_datetime(start_date="-30d", tzinfo=timezone.utc),
            ) for _ in range(count)]
            user.posts.bulk_create(posts)

    def generate_likes(self, count):
        for user in self.users:
            post_ids = list(Post.objects.exclude(user=user).values_list('id', flat=True))
            shuffle(post_ids)
            likes = [Like(user=user, post_id=post_ids.pop(), status=choice((-1, 0, 1))) for _ in range(count)]
            Like.objects.bulk_create(likes)
