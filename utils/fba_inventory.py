'''
Retrive the inventory of a FBA warehouse
'''

import requests
import json

def get_inventory():

    '''Function to retrieve the inventory of a FBA without involving the database'''

    # Define the endpoint
    endpoint = 'https://api.amazon.com/fba/inventory/v1/summaries'
    print ('Getting Endpoint')

    # Define the headers
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer '
    }
    print ('Getting Headers')

    # Define the payload
    payload = {
        'granularity': 'Marketplace',
        'granularityId': 'ATVPDKIKX0DER',
        'startDateTime': '2021-01-01T00:00:00Z',
        'endDateTime': '2021-12-31T23:59:59Z'
    }
    print ('Getting Payload')

    # Make the request
    response = requests.post(endpoint, headers=headers, data=json.dumps(payload))
    print ('Getting Response')

    # Check if the request was successful
    if response is not None:

        # Return the inventory
        print ('Returning Response')
        data = response.json()
        return data
        
    else:
        # Return an error message
        print ('Unsuccessful Response')
        return {'error': 'Failed to retrieve inventory'}
        
    
    



