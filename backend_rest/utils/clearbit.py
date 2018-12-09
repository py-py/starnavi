import json
import requests
from django.conf import settings

from backend.models import User

__all__ = ('handle_clearbit',)


def handle_clearbit(user_id):
    user = User.objects.get(id=user_id)
    clearbit_settings = settings.CLEARBIT

    url = clearbit_settings['URL_ENRICHMENT_TEMPLATE']
    api_key = clearbit_settings['API_KEY']
    headers = {'Authorization': 'Bearer {key}'.format(key=api_key)}

    with requests.get(url.format(email=user.email), headers=headers) as response:
        if response.status_code == 200:
            result = response.json()
            user.clearbit = json.dumps(result)
            user.save()
