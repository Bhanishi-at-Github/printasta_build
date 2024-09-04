from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from sp_api.api import FulfillmentInbound
import os

# Create your views here.

def home(request):
    return render(request, 'index.html')

def fba_Inventory(request):

    refresh_token= os.getenv('refresh_token')

    api = FulfillmentInbound(refresh_token=refresh_token)
    response = api.get_transport_details()

    return JsonResponse(response)

    

