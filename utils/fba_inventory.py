'''
Retrive the inventory of a FBA warehouse
'''

import requests
import json
from utils.refresh_token import generate_access_token

def get_inventory(endpoint):

    '''Function to retrieve the inventory of a FBA without involving the database'''

    # Generate Access token using refresh token

    access_token = generate_access_token()
    print ('Getting Access Token')

    # Define the headers
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer {}'.format(access_token)
    }
    print ('Getting Headers')

    # Define the payload
    payload = {
        'granularity': 'US',
        'granularityId': 'ATVPDKIKX0DER', 
        'startDateTime': '2024-07-01T00:00:00Z',
        'endDateTime': '2024-08-31T23:59:59Z'
    }
    print ('Getting Payload')

    # Make the request

    if payload is not None:

        response = requests.post(endpoint, headers=headers, data=json.dumps(payload))
        print ('Getting Response', response)

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
            # Return an error message
            print('No Response')
            return {'error': 'No response from server'}    
        
    else:
        print('No Payload')
        return {'error': 'No payload provided'}



