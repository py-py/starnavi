import os
from dotenv import load_dotenv
from django.contrib.auth.management.commands import createsuperuser

from backend.models import User


class Command(createsuperuser.Command):
    help = 'Create a superuser(customizated command)'

    def handle(self, *args, **options):
        load_dotenv()
        username = os.getenv('SUPERUSER_USERNAME')
        password = os.getenv('SUPERUSER_PASSWORD')
        email = os.getenv('SUPERUSER_EMAIL')

        User.objects.create_superuser(
            username=username,
            password=password,
            email=email,
        )
