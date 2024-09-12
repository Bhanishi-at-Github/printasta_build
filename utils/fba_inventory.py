'''
Retrive the inventory of a FBA warehouse
'''

import requests
import json
import os
from datetime import datetime
from django.conf import settings

def get_inventory():

    '''Function to retrieve the inventory of a FBA without involving the database'''

    # Define the endpoint

    endpoint = 'https://api.amazon.com/fba/inventory/v1/summaries'

    # Define the headers

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer '
    }

    # Define the payload

    payload = {
        'granularity': 'Marketplace',
        'granularityId': 'ATVPDKIKX0DER',
        'startDateTime': '2021-01-01T00:00:00Z',
        'endDateTime': '2021-12-31T23:59:59Z'
    }

    # Make the request

    response = requests.post(endpoint, headers=headers, data=json.dumps(payload))

    # Check if the request was successful

    if response.status_code == 200:

        # Return the inventory

        return response.json()
    
    else:

        # Return an error message

        return {'error': 'Failed to retrieve inventory'}
    
    



