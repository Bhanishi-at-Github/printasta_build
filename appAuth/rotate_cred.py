# Rotate Credentials

from appAuth.models import Refresh_Token
import requests
import os

def rotate_refresh_token():

    # Get the refresh token from the database
    refresh_token = Refresh_Token.objects.first().refresh_token

    # Define the token endpoint and payload
    token_url = "https://api.amazon.com/auth/o2/token"
    payload = {
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token,
        'client_id': os.getenv('lwa_client_id'),
        'client_secret': os.getenv('lwa_client_secret'),
    }

    # Make the POST request to exchange the refresh token for a new access token
    response = requests.post(token_url, data=payload)
    response_data = response.json()

    if response.status_code != 200:
        raise Exception(f"Error during token exchange: {response_data}")

    # Update the refresh token in the database
    Refresh_Token.objects.update(refresh_token=response_data['refresh_token'], access_token=response_data['access_token'])

    return response_data['access_token']

def rotate_client_secret():

    # Define the token endpoint and payload
    token_url = "https://api.amazon.com/auth/o2/token"
    payload = {
        'grant_type': 'client_credentials',
        'client_id': os.getenv('lwa_client_id'),
        'client_secret': os.getenv('lwa_client_secret'),
    }

    # Make the POST request to exchange the client credentials for a new access token
    response = requests.post(token_url, data=payload)
    response_data = response.json()

    if response.status_code != 200:
        raise Exception(f"Error during token exchange: {response_data}")

    return response_data['access_token']