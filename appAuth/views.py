import os
import logging
from django.shortcuts import redirect
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import requests

logger = logging.getLogger(__name__)

client_id = os.getenv('client_id')
client_secret = os.getenv('client_secret')
redirect_uri = os.getenv('redirect_uri')
app_id = os.getenv('app_id')

def amazonAuth(request):

    if request.method == 'GET':
        url = f'https://sellercentral.amazon.com/apps/authorize/consent?application_id={app_id}&redirect_uri={redirect_uri}&version=beta'

        
        return redirect(url)

    if url is not None:

        spapi_oauth_code = request.GET.get('spapi_oauth_code')
        amazon_state = request.GET.get('state')

        
        if spapi_oauth_code:
            # Handle the callback
            print("Amazon Callback")

            if not spapi_oauth_code:
                return JsonResponse({
                    'message': 'Authorization code not provided',
                    'status': 400
                })

            try:
                # Exchange the authorization code for tokens
                token_data = exchange_code_for_token(
                    client_id=client_id,
                    client_secret=client_secret,
                    spapi_oauth_code=spapi_oauth_code,
                    redirect_uri=redirect_uri,
                    state=amazon_state
                )

                print(token_data)
                
                # Extract tokens from the response
                access_token = token_data.get('access_token')
                refresh_token = token_data.get('refresh_token')

                return JsonResponse({
                    'message': 'Authorization successful',
                    'status': 200,
                    'access_token': access_token,
                    'refresh_token': refresh_token
                })
            except Exception as e:
                return JsonResponse({
                    'message': 'Failed to exchange authorization code for tokens',
                    'status': 500,
                    'error': str(e)
                })

def exchange_code_for_token(client_id, client_secret, spapi_oauth_code, amazon_state, redirect_uri):
    import http.client
    import urllib.parse
    import json

    token_url = "https://api.amazon.com/auth/o2/token"
    data = {
        'grant_type': 'authorization_code',
        'code': spapi_oauth_code,
        'client_id': client_id,
        'client_secret': client_secret,
        'state': amazon_state,
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