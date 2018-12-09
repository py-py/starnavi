import json
import requests
from django.conf import settings

from backend.models import User

__all__ = ('handle_emailhunter',)


def handle_emailhunter(user_id):
    user = User.objects.get(id=user_id)

    emailhunter_settings = settings.EMAILHUNTER
    url = emailhunter_settings['URL_EMAIL_VERIFICATION_TEMPLATE']
    api_key = emailhunter_settings['API_KEY']

    with requests.get(url.format(email=user.email, api_key=api_key)) as response:
        if response.status_code == 200:
            result = response.json()
            user.emailhunter = json.dumps(result)
            user.save()
