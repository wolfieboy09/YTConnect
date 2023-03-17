import requests
import json
from . import user
from . import Exceptions


class session:
    def login(key):
        try:
            r = requests.get(f'https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=PewDiePie&key={key}').json()['items']
        except:
            print("Error - Check your internet connection")