'''
Retrive the inventory of a FBA warehouse
'''
from sp_api.api import Orders

def get_inventory(endpoint):

    '''Function to retrieve the inventory of a FBA without involving the database'''

    url = {
        'base_URL': 'https://sandbox.sellingpartnerapi-na.amazon.com',
        'endpoint': endpoint
    }

    # Make the request
    response = Orders().get_inventory(url)

    return response

# Base URL for the API
# https://sandbox.sellingpartnerapi-na.amazon.com

# Endpoint for the API
# /orders/v0/orders