import requests


class Spotify:
    def __init__(self):
        pass

    def authorization(self):
        url = "https://accounts.spotify.com/authorize"
        r = requests.get(url)
        print(r.status_code)

    def retrieve(self):
        pass

    def create(self):
        pass