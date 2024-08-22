from django.shortcuts import render
from django.shortcuts import redirect, HttpResponse
import requests
import os
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import logging

# Set up logging
logger = logging.getLogger(__name__)

client_id = os.getenv('client_id')

client_secret = os.getenv('client_secret')

redirect_uri = os.getenv('redirect_uri')

app_id = os.getenv('app_id')

# Create your views here.


def amazonAuth(request):

    url = f'https://sellercentral.amazon.com/apps/authorize/consent?application_id={app_id}&redirect_uri={redirect_uri}&version=beta'
    
    if request.method == 'GET':

        try:

            return redirect (url)
        
        except requests.exceptions.RequestException as e:

            return JsonResponse({
                'message': 'Failed to redirect to Amazon',
                'status': 500,
                'error': str(e)
            })
        









# https://sellercentral.amazon.com/apps/authorize/