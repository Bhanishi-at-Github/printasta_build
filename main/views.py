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

    