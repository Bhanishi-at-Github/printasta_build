''' Generate a new access token using the refresh token '''

import requests
import json
import os

# Credentials

client_id = os.getenv('lwa_client_id')
client_secret = os.getenv('lwa_client_secret')
refresh_token = os.getenv('refresh_token')


def generate_access_token():

    '''Function to generate a new access token using the refresh token'''

    # Define the headers
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    print ('Getting Headers for Access Token')

    # Define the payload
    payload = {
        'grant_type': 'refresh_token',
        'client_id': client_id,
        'client_secret': client_secret,
        'refresh_token': refresh_token
    }
    print ('Getting Payload for Access Token')

    # Make the request
    response = requests.post('https://api.amazon.com/auth/o2/token', headers=headers, data=payload)

    # Check if the request was successful

    if response is not None and response.status_code == 200:


        try:
            data = response.json()
            print('Returning Response for Access Token')
            return data
            
        except json.JSONDecodeError as e:
            print(f'JSON Decode Error: {e}')
            return {'error': 'Failed to parse JSON response'}
    else:
        print('Unsuccessful Response')
        return {'error': f'Failed to generate access token, status code: {response.status_code}'}
    
