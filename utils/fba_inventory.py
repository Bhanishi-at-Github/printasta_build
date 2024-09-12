'''
Retrive the inventory of a FBA warehouse
'''

import json
import os
import io
from django.shortcuts import redirect
from utils.refresh_token import generate_access_token
from sp_api.api import Orders

def get_inventory(endpoint):

    '''Function to retrieve the inventory of a FBA without involving the database'''

    # Generate a new access token
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
        return response.json()
        
    else:

        print('Unsuccessful Response')
        return redirect('error.html', {'content': {'error': 'Failed to retrieve inventory'}})


