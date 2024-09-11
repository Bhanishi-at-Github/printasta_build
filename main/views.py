from django.shortcuts import render, HttpResponse
import os
import logging
from sp_api.base import Marketplaces

# Configure logging
logging.basicConfig(level=logging.ERROR)

# Create your views here.

def home(request):
    return render(request, 'index.html')


def marketplaces(request):
    return HttpResponse(Marketplaces.get_marketplaces())