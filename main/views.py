from django.shortcuts import render
import logging
from utils.fba_inventory import get_inventory

# Configure logging
logging.basicConfig(level=logging.ERROR)

# Create your views here.

def home(request):
    return render(request, 'index.html')

def test(request):

    inventory = get_inventory()
    return render(request, 'test.html', {'content': inventory})
