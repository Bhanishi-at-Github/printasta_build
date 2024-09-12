'''
Retrive the inventory of a FBA warehouse
'''

import requests
import json
from utils.refresh_token import generate_access_token
from sp_api.api import Orders

def get_inventory(endpoint):

    '''Function to retrieve the inventory of a FBA without involving the database'''

    # Generate Access token using refresh token

    access_token = generate_access_token()
    print ('Getting Access Token')

    # Define the headers
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {access_token["access_token"]}'
    }
    print ('Getting Headers')

    # Define the payload
    payload = None
    print ('Getting Payload')

    # Make the request
    response = requests.get(endpoint, headers=headers, data=payload)

    # Check if the request was successful
    if response is not None and response.status_code == 200:
        try:
            data = response.json()
            print('Returning Response')
            return data
        except json.JSONDecodeError as e:
            print(f'JSON Decode Error: {e}')
            return {'error': 'Failed to parse JSON response'}
    else:
        print('Unsuccessful Response')
        return {'error': f'Failed to retrieve inventory, status code: {response.status_code}'} 


