import requests
import json

class Spotify:
    def __init__(self, client_id, client_secret):
        self.access_token = ''
        self.base_url = 'https://api.spotify.com/v1'
        self.client_id = client_id
        self.client_secret = client_secret
        self.headers = {} 

    def authorization(self):
        url = "https://accounts.spotify.com/api/token"

        auth_response = requests.post(url, {
            'grant_type': 'client_credentials',
            'client_id': self.client_id,
            'client_secret': self.client_secret,
        })
        response_data = auth_response.json()

        self.access_token = response_data['access_token']
        self.headers['Authorization'] = 'Bearer %s' % self.access_token

    def get_current_users_playlists(self, user_id):
        url = self.base_url + '/users/%s/playlists' % user_id

        r = requests.get(url, headers=self.headers)
        print(r.json())

    def get_current_users_info(self, user_id):
        url = self.base_url + '/users/%s' % user_id
        
        r = requests.get(url, headers=self.headers)
        print(r.json())


    def retrieve(self):
        pass

    def create(self):
        pass