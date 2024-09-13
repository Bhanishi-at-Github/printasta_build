'''
Retrive the inventory of a FBA warehouse
'''
from sp_api.api import Orders
from main.models import AppOrders
def get_inventory(endpoint):

    '''Function to retrieve the inventory of a FBA without involving the database'''

    url = {
        'base_URL': 'https://sandbox.sellingpartnerapi-na.amazon.com',
        'endpoint': endpoint
    }

    response = Orders.get_orders(url)
    
    # Check if response is a list or iterable
    if isinstance(response, list):
        # Store inventory in db
        for item in response:
            order = AppOrders(
                order_id=item['order_id'],
                order_date=item['order_date'],
                order_status=item['order_status'],
                order_total=item['order_total'],
                order_items=item['order_items'],
                order_customer=item['order_customer'],
                order_address=item['order_address']
            )
            order.save()
    else:
        # Handle the case where response is not as expected
        print("Unexpected response format:", response)
    
    return response

# Base URL for the API
# https://sandbox.sellingpartnerapi-na.amazon.com

# Endpoint for the API
# /orders/v0/orders