from django.shortcuts import render
from django.shortcuts import redirect, HttpResponse
import requests
import os
from django.http import JsonResponse

import logging
import http.client
import urllib.parse
import json
from django.contrib.auth.models import User
from sp_api.base import AccessTokenClient



# Set up logging
logger = logging.getLogger(__name__)

client_id = os.getenv('client_id')

client_secret = os.getenv('client_secret')

redirect_uri = os.getenv('redirect_uri')

app_id = os.getenv('app_id')

refresh_token = os.getenv('refresh_token')


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

# def amazon_callback(request):

#     logger.info("Amazon Callback triggered")

#     if request.method == 'GET':
#         # Extract the authorization code and state from the query parameters
#         code = request.GET.get('spapi_oauth_code')

#         if not code:
#             logger.error("spapi_oauth_code not received")
#             return HttpResponse("Error: spapi_oauth_code not received", status=400)

#         logger.info(f"Received spapi_oauth_code: {code}")

#         try:
#             res = AccessTokenClient().authorize_auth_code(code)
#             logger.info(f"Authorization response: {res}")

#             code_for_token = exchange_code_for_token(client_id, client_secret, code, redirect_uri)
#             refresh_token = code_for_token['refresh_token']

#             save_refresh_token(refresh_token)

#             return JsonResponse({
#                 'message': 'Refresh token saved',
#                 'status': 200
#             })
        

#         except Exception as e:
#             logger.error(f"Error authorizing auth code: {e}")
#             return HttpResponse(f"Error authorizing auth code: {e}", status=500)

#         # context = {
#         #     'code': code,
#         #     'state': state,
#         #     'seller_id': seller_id,
#         # }

#         # return render(request, 'callback.html', context=context)

#     # if request.method == 'POST':
#     #     seller_name = request.POST.get('seller_name')
#     #     email = request.POST.get('email')
#     #     password = request.POST.get('password')
#     #     state = request.POST.get('state')
#     #     seller_id = request.POST.get('seller_id')

#     #     # Handle POST request logic here

#     # return HttpResponse("Invalid request method", status=405)

        
# # def get_refresh_token(request):

# #     if request.method=='GET':

# #         code = request.GET.get('code')

# #         token_data = exchange_code_for_token(client_id, client_secret, code, redirect_uri)

# #         refresh_token = token_data['refresh_token']

# #         save_refresh_token(refresh_token)

# #         return JsonResponse({

# #             'message': 'Refresh token saved',
# #             'status': 200
# #         })
    

# def exchange_code_for_token(client_id, client_secret, code, redirect_uri):

#     token_url = "https://api.amazon.com/auth/o2/token"
#     data = {
#         'grant_type': 'authorization_code',
#         'code': code,
#         'client_id': client_id,
#         'client_secret': client_secret,
#         'redirect_uri': redirect_uri
#     }

#     parsed_url = urllib.parse.urlparse(token_url)
#     conn = http.client.HTTPSConnection(parsed_url.netloc)
#     headers = {'Content-Type': 'application/x-www-form-urlencoded'}
#     conn.request("POST", parsed_url.path, urllib.parse.urlencode(data), headers)
#     response = conn.getresponse()
#     response_data = response.read().decode()
#     conn.close()

#     return json.loads(response_data)


# def save_refresh_token(refresh_token):

#     refresh_token = refresh_token

#     refresh_token_file = 'refresh_token.txt'

#     with open(refresh_token_file, 'w') as file:

#         file.write(refresh_token)

#     print('Refresh token saved')


def get_orders(request):

    refresh_token = os.getenv('refresh_token')

    url = 'https://api.amazon.com/auth/o2/token'

    data = {
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token,
        'client_id': client_id,
        'client_secret': client_secret
    }

    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    response = requests.post(url, data=data, headers=headers)

    access_token = response.json()['access_token']

    url = 'https://api.amazon.com/v1/orders'

    headers = {
        'Authorization': f'Bearer {access_token}',
        'Amazon-Advertising-API-Scope': 'sellingpartnerapi::orders'
    }

    response = requests.get(url, headers=headers)

    return JsonResponse(response.json())