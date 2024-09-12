'''
Retrive the inventory of a FBA warehouse
'''

import json
import os
from django.shortcuts import redirect
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
    print ('Getting Headers for Inventory')

    # Define the payload
    payload = None
    print ('Getting Payload for Inventory')

    # Make the request
    orders = Orders(
        marketplace='US',
        refresh_token=os.getenv('refresh_token'),
    )
    response = orders.get_orders()
    print ('Getting Response for Inventory')

    # Check if the request was successful

    if response is not None and response.status_code == 200:

        try:
            data = response.json()
            print('Returning Response for Inventory')
            return data

        except json.JSONDecodeError as e:
            print(f'JSON Decode Error: {e}')
            return {'error': 'Failed to parse JSON response'}
        
    else:

        print('Unsuccessful Response')
        return redirect('error.html', {'content': {'error': 'Failed to retrieve inventory'}})


