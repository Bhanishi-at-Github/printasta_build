'''
Retrive the inventory of a FBA warehouse
'''

import json
import os
import io
from django.shortcuts import redirect
from sp_api.api import Orders

def get_inventory(endpoint):

    '''Function to retrieve the inventory of a FBA without involving the database'''

    endpoint = endpoint

    # Make the request
    orders = Orders(
        marketplace='US',
        refresh_token=os.getenv('refresh_token'),
    )
    response = orders.get_orders()
    print ('Getting Response for Inventory')

    # Check if the request was successful

    if response.status_code == 200:

        print ('Successful Response')
        
        try:
            # Use in-memory storage instead of writing to a file
            temp_storage = io.StringIO()
            temp_storage.write(response.text)
            temp_storage.seek(0)  # Reset cursor to the beginning if you need to read it later
            return json.loads(temp_storage.read())  # Example of reading from in-memory storage

        except json.JSONDecodeError as e:
            print(f'JSON Decode Error: {e}')
            return {'error': 'Failed to parse JSON response'}
        
        
    else:

        print('Unsuccessful Response')
        return redirect('error.html', {'content': {'error': 'Failed to retrieve inventory'}})


