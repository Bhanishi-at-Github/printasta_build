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
from django.contrib.auth.models import User

# Set up logging
logger = logging.getLogger(__name__)

client_id = os.getenv('client_id')

client_secret = os.getenv('client_secret')

redirect_uri = os.getenv('redirect_uri')

app_id = os.getenv('app_id')

scope = "sellingpartnerapi::notifications sellingpartnerapi::migration profile::user_id"

# Create your views here.


def amazonAuth(request):

    url = f'https://sellercentral.amazon.com/apps/authorize/consent?application_id={app_id}&scope={scope}&redirect_uri={redirect_uri}&response_type=code&version=beta'
    
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

        # Extract the authorization code and state from the query parameters
        # code = request.GET.get('spapi_oauth_code')
        state = request.GET.get('amazon_state')
        seller_id = request.GET.get('selling_partner_id')
    
    if request.method == 'POST':

        seller_name = request.POST.get('seller_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.create_user(username=seller_name, email=email)
        user.set_password(password)

        user.save()

        context = {
            
            'state': state,
            'seller_id': seller_id,

        }

        return render(request, 'appAuth/callback.html', context=context)

        
def get_refresh_token(request):

    if request.method=='GET':

        code = request.GET.get('code')

        token_data = exchange_code_for_token(client_id, client_secret, code, redirect_uri)

        refresh_token = token_data['refresh_token']

        save_refresh_token(refresh_token)

        return JsonResponse({

            'message': 'Refresh token saved',
            'status': 200
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
