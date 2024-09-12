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
        'granularity': 'US',
        'granularityId': 'ATVPDKIKX0DER',
        'startDateTime': '2024-07-01T00:00:00Z',
        'endDateTime': '2024-08-31T23:59:59Z'
    }
    print ('Getting Payload')

    # Make the request
    response = requests.post(endpoint, headers=headers, data=json.dumps(payload))
    print ('Getting Response')

    # Check if the request was successful
    if response is not None:
        print(f'Response Status Code: {response.status_code}')
        print(f'Response Content: {response.text}')

        if response.status_code == 200:
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
    else:
        # Return an error message
        print('No Response')
        return {'error': 'No response from server'}    
    
    



