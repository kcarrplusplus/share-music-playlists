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


    def get_playlist(self):
        # POST https://api.spotify.com/v1/users/{user_id}/playlists
        pass

    def create_playlist(self, user_id, name_of_playlist, description='', public=True, collaborative=False):
        # TODO: Have to use authorization code flow or implicit grant flow detailed in link below
        # https://developer.spotify.com/documentation/general/guides/authorization-guide/
        url = self.base_url + '/users/%s/playlists' % user_id
        post_headers = self.headers
        post_headers['Content-Type'] = 'application/json'
        post_headers['Accept'] = 'application/json'

        payload = {
            'name': name_of_playlist, 
            'public': public,
            'collaborative': collaborative,
            'description': description
        }
        print(post_headers)
        r = requests.post(url, headers=post_headers, data=payload)

        print(r.text)
        print(r.status_code)