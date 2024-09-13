import json
import os
from django.http import HttpResponse
from django.shortcuts import redirect
from utils.refresh_token import generate_access_token
from sp_api.api import Orders
from sp_api.base import Marketplaces
from main.models import AppOrder  # Ensure you import your model

def get_inventory(endpoint):
    '''Function to retrieve the inventory of a FBA without involving the database'''

    try:
        # Generate a new access token
        access_token = generate_access_token()
        print('Getting Access Token')

        # Define the headers
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {access_token["access_token"]}'
        }
        print('Getting Headers for Inventory')

        # Define the base URL
        base_url = "https://sandbox.sellingpartnerapi-na.amazon.com"

        # Define the URL
        url = base_url + endpoint

        # Make the request

        orders_client = Orders(
            marketplace=Marketplaces.US,
            refresh_token=os.getenv('refresh_token'),
        )

        # Make the request
        response = orders_client.get_orders()
        print('Getting Response for Inventory')

        # Debugging: Print the response object
        print("Response object:", response)

        # Check if response is a list or iterable
        if isinstance(response, list):
            print('Successful Response')
            # Store inventory in db
            for item in response:
                order = AppOrder(
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
            return HttpResponse(json.dumps({'error': 'Unexpected response format'}), content_type='application/json')
        
        return HttpResponse(json.dumps(response), content_type='application/json')

    except Exception as e:
        print(f'An error occurred: {e}')
        return HttpResponse(json.dumps({'error': 'An unexpected error occurred'}), content_type='application/json')