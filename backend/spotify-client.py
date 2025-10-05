import os
import requests

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")

SCOPE = "playlist-read-private user-top-read"

def get_auth_url():
    import urllib.parse
    params = {
        "response_type": "code",
        "client_id": SPOTIFY_CLIENT_ID,
        "redirect_uri": REDIRECT_URI,
        "scope": SCOPE
    }
    return f"https://accounts.spotify.com/authorize?{urllib.parse.urlencode(params)}"

def get_tokens(auth_code):
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "authorization_code",
        "code": auth_code,
        "redirect_uri": REDIRECT_URI,
        "client_id": SPOTIFY_CLIENT_ID,
        "client_secret": SPOTIFY_CLIENT_SECRET
    }
    response = requests.post(url, data=data)
    return response.json()

def get_user_playlists(access_token):
    url = "https://api.spotify.com/v1/me/playlists"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    response = requests.get(url, headers=headers)
    return response.json()
