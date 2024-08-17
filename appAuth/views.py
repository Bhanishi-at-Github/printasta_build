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
    

@require_http_methods(["GET"])
def amazon_callback(request):

    print ("Amazon Callback")

    code = request.GET.get('code')
    print(code)

    if not code:
        return JsonResponse({
            'message': 'Authorization code not provided',
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

        print(token_data)
        
        # Extract tokens from the response
        access_token = token_data.get('access_token')
        refresh_token = token_data.get('refresh_token')

        # Store the refresh token securely (this is just an example, use your method)
        save_refresh_token(refresh_token)

        print('Access token:', access_token)

        return JsonResponse({
            'message': 'Authorization successful',
            'status': 200,
            'access_token': access_token,
        })
    

    except Exception as e:
        
        return JsonResponse({
            'message': 'Failed to exchange authorization code for tokens',
            'status': 500,
            'error': str(e)
        })


def exchange_code_for_token(client_id, client_secret, code, redirect_uri):

    import http.client
    import urllib.parse
    import json

    print("Exchange code for token")
    token_url = "https://api.amazon.com/auth/o2/token"
    data = {
        'grant_type': 'authorization_code',
        'code': code,
        'client_id': client_id,
        'client_secret': client_secret,
        'redirect_uri': redirect_uri
    }

    print("Data:", data)

    # Parse the URL
    parsed_url = urllib.parse.urlparse(token_url)
    conn = http.client.HTTPSConnection(parsed_url.netloc)

    # Encode the data
    encoded_data = urllib.parse.urlencode(data)
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    try:
        # Send the POST request
        conn.request("POST", parsed_url.path, encoded_data, headers)
        response = conn.getresponse()
        response_data = response.read()
        
        # Check for successful response
        if response.status != 200:
            raise Exception(f"Request failed: {response.status} {response.reason}")
        
        # Parse the response JSON
        response_json = json.loads(response_data)
        print("Response JSON:", response_json)
        return response_json
    except Exception as e:
        print(f"Request failed: {e}")
    finally:
        conn.close()

def save_refresh_token(refresh_token):

    refresh_token = refresh_token

    refresh_token_file = 'refresh_token.txt'

    with open(refresh_token_file, 'w') as file:

        file.write(refresh_token)

    print('Refresh token saved')







