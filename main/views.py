from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from sp_api.api import FulfillmentInbound
import os
import logging

# Configure logging
logging.basicConfig(level=logging.ERROR)

# Create your views here.

def home(request):
    return render(request, 'index.html')

def fba_Inventory(request):

    refresh_token = os.getenv('refresh_token')

    # Validate refresh token
    if not refresh_token:
        return JsonResponse({'error': 'Refresh token not found'})
    
    # Create an instance of the FulfillmentInbound class
    confuse_dir_value = os.getenv('CONFUSE_DIR')
    fba = FulfillmentInbound(refresh_token=refresh_token, confuse_dir=confuse_dir_value)

    # Get inventory
    try:
        api = fba.get_transport_information()

        # Get the response
        response = api.payload({
            'transportDetails': api.payload['TransportDetails'],
            'shipmentId': api.payload['ShipmentId'],
            'status': api.payload['Status'],
        })

        return JsonResponse(response)
    
    except Exception as e:
        return JsonResponse({'error': str(e)})
    