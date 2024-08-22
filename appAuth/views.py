from django.shortcuts import render
from django.shortcuts import redirect, HttpResponse
import requests
import os
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import logging
import http.client
import urllib.parse
import json

# Set up logging
logger = logging.getLogger(__name__)

client_id = os.getenv('client_id')

client_secret = os.getenv('client_secret')

redirect_uri = os.getenv('redirect_uri')

app_id = os.getenv('app_id')

scope = "sellingpartnerapi::notifications sellingpartnerapi::migration profile"

response_type = "code"

version = "beta"

# Create your views here.


def amazonAuth(request):

    url = f'https://sellercentral.amazon.com/apps/authorize/consent?application_id={app_id}&scope={scope}&response_type=code&redirect_uri={redirect_uri}&version=beta'
    
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

    code = request.GET.get('code')
    logger.info(f"spapi_oauth_code: {code}")

    if not code:
        return JsonResponse({
            'message': 'Authorization code not provided,' + error,
            'status': 400
        })

    try:
        # Exchange the authorization code for tokens
        token_data = exchange_code_for_token(
            client_id=client_id,
            client_secret=client_secret,
            code=code,
            redirect_uri=redirect_uri
        )

        logger.info(f"Token data: {token_data}")
        
        # Extract tokens from the response
        access_token = token_data.get('access_token')
        refresh_token = token_data.get('refresh_token')

        return JsonResponse({
            'message': 'Successfully exchanged authorization code for tokens',
            'status': 200,
            'access_token': access_token,
            'refresh_token': refresh_token
        })
    
    except Exception as e:
        logger.error(f"Error exchanging authorization code for tokens: {str(e)}")
        return JsonResponse({
            'message': 'Failed to exchange authorization code for tokens',
            'status': 500,
            'error': str(e)
        })

    

def exchange_code_for_token(client_id, client_secret, code, redirect_uri):

    token_url = "https://api.amazon.com/auth/o2/token"
    data = {
        'grant_type': 'authorization_code',
        'code': code,
        'client_id': client_id,
        'client_secret': client_secret,
        'redirect_uri': redirect_uri
    }

    parsed_url = urllib.parse.urlparse(token_url)
    conn = http.client.HTTPSConnection(parsed_url.netloc)
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    conn.request("POST", parsed_url.path, urllib.parse.urlencode(data), headers)
    response = conn.getresponse()
    response_data = response.read().decode()
    conn.close()

    return json.loads(response_data)


def save_refresh_token(refresh_token):

    refresh_token = refresh_token

    refresh_token_file = 'refresh_token.txt'

    with open(refresh_token_file, 'w') as file:

        file.write(refresh_token)

    print('Refresh token saved')
