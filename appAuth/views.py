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
        
    
def amazon_callback(request):

    logger.info("Amazon Callback triggered")

    if request.method == 'GET':

        code = request.GET.get('code')

        state = request.GET.get('state')

        url = f'https://api.amazon.com/auth/o2/token'

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        data = {
            'grant_type': 'authorization_code',
            'code': code,
            'client_id': client_id,
            'client_secret': client_secret,
            'redirect_uri': redirect_uri
        }

        try:

            response = requests.post(url, headers=headers, data=data)

            response_data = response.json()

            access_token = response_data['access_token']

            refresh_token = response_data['refresh_token']

            selling_partner_id = response_data['selling_partner_id']

            amazon_state = state

            amazon_callback_uri = redirect_uri

            return JsonResponse({
                'message': 'Amazon Auth successful',
                'status': 200,
                'access_token': access_token,
                'refresh_token': refresh_token,
                'selling_partner_id': selling_partner_id,
                'amazon_state': amazon_state,
                'amazon_callback_uri': amazon_callback_uri
            })

        except requests.exceptions.RequestException as e:

            return JsonResponse({
                'message': 'Failed to get Amazon Auth',
                'status': 500,
                'error': str(e)
            })
        
    else:
            
        return JsonResponse({
            'message': 'Method not allowed',
            'status': 405
        })


def amazon_refresh_token(request):

    if request.method == 'POST':

        refresh_token = request.POST.get('refresh_token')

        url = f'https://api.amazon.com/auth/o2/token'

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        data = {
            'grant_type': 'refresh_token',
            'refresh_token': refresh_token,
            'client_id': client_id,
            'client_secret': client_secret
        }

        try:

            response = requests.post(url, headers=headers, data=data)

            response_data = response.json()

            access_token = response_data['access_token']

            refresh_token = response_data['refresh_token']

            return JsonResponse({
                'message': 'Amazon Refresh Token successful',
                'status': 200,
                'access_token': access_token,
                'refresh_token': refresh_token
            })

        except requests.exceptions.RequestException as e:

            return JsonResponse({
                'message': 'Failed to refresh Amazon Token',
                'status': 500,
                'error': str(e)
            })
        
    else:
            
        return JsonResponse({
            'message': 'Method not allowed',
            'status': 405
        })
    