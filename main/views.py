from django.shortcuts import render
import logging
from utils.fba_inventory import get_inventory
from utils.refresh_token import generate_access_token

# Configure logging
logging.basicConfig(level=logging.ERROR)

# Create your views here.

def home(request):
    return render(request, 'index.html')

def test(request):

    endpoint = '/orders/v0/orders'

    try:
        # Retrieve the inventory
        inventory = get_inventory(endpoint)
        return render(request, 'test.html', {'content': inventory})
    
    except Exception as e:

        # Log the error
        logging.error(str(e))

        # Return an error message
        return render(request, 'error.html', {'content': {'error': 'Failed to retrieve inventory'}})

