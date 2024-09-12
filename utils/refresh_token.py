''' Generate a new access token using the refresh token '''

import requests
import json
import os

# Credentials

client_id = os.getenv('lwa_client_id')
client_secret = os.getenv('lwa_client_secret')
refresh_token = os.getenv('lwa_refresh_token')


def generate_access_token():

    '''Function to generate a new access token using the refresh token'''

    # Define the headers
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    print ('Getting Headers')

    # Define the payload
    payload = {
        'grant_type': 'refresh_token',
        'client_id': client_id,
        'client_secret': client_secret,
        'refresh_token': refresh_token
    }
    print ('Getting Payload')

    # Make the request
    response = requests.post('https://api.amazon.com/auth/o2/token', headers=headers, data=payload)

    # Check if the request was successful

    if response is not None:

        print(f'Response Status Code: {response.status_code}')
        print(f'Response Content: {response.text}')

        if response.status_code == 200:

            try:
                data = response.json()
                print('Returning Response')
                return data['access_token']
            
            except json.JSONDecodeError as e:
                print(f'JSON Decode Error: {e}')
                return {'error': 'Failed to parse JSON response'}
        else:
            print('Unsuccessful Response')
            return {'error': f'Failed to generate access token, status code: {response.status_code}'}
        
    else:
        # Return an error message
        print('No Response')
        return {'error': 'No response from server'}
    
