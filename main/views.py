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
    
    if not refresh_token:
        logging.error("Refresh token not found in environment variables")
        return HttpResponse("Server configuration error: Refresh token not found", status=500)
    
    try:
        # Initialize FulfillmentInbound with credentials
        api = FulfillmentInbound(refresh_token=refresh_token)
        response = api.get_transport_details()

        return JsonResponse(response, safe=False)
    
    except Exception as e:
        logging.error(f"Error during fetching inventory: {e}")
        return HttpResponse(f"Error during fetching inventory: {e}", status=500)