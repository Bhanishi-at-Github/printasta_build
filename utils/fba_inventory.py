'''
Retrive the inventory of a FBA warehouse
'''

import json
import os
import io
from django.shortcuts import redirect, HttpResponse
from sp_api.api import Orders

def get_inventory(endpoint):

    '''Function to retrieve the inventory of a FBA without involving the database'''

    url = {
        'base_URL': 'https://sandbox.sellingpartnerapi-na.amazon.com',
        'endpoint': endpoint
    }

    # Make the request
    response = Orders().get_inventory(url)

    if response.status_code == 200:

        print ('Successful Response')

        try:
            # Retrieve the inventory according to vercel requirements
            
            file = 'tmp/temp.txt'

            with open(file, 'w') as f:
                f.write("Hello World")
            f.close()

            with open(file, 'r') as f:
                content = f.read()
            f.close()

            return content
        
        except Exception as e:

            print('Error:', str(e))
            return redirect('error.html', {'content': {'error': 'Failed to retrieve inventory'}})
        
    else:

        print('Unsuccessful Response')
        return redirect('error.html', {'content': {'error': 'Failed to retrieve inventory'}})

# Base URL for the API
# https://sandbox.sellingpartnerapi-na.amazon.com

# Endpoint for the API
# /orders/v0/orders