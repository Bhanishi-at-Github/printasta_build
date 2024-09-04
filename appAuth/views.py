from django.shortcuts import render, redirect
from django.http import HttpResponse
import os
import requests
from django.http import JsonResponse
from .models import Refresh_Token  # Ensure you have this model defined


lwa_app_id = os.getenv('lwa_app_id')
lwa_client_id = os.getenv('lwa_client_id')
lwa_client_secret = os.getenv('lwa_client_secret')
redirect_uri = os.getenv('redirect_uri')

def state_define():
    # Define your state generation logic

    return "stateexample"

def authorize(request):
    state = state_define()
    auth_url = f"https://sellercentral.amazon.com/apps/authorize/consent?application_id={lwa_app_id}&state={state}&version=beta"
    return redirect(auth_url)

def redirect_view(request):
    auth_code = request.GET.get('spapi_oauth_code')
    seller_id = request.GET.get('seller_id')  
    # Assuming seller_id is passed as a query parameter

    if not auth_code:
        return HttpResponse("Error: spapi_oauth_code not received", status=400)
    
    try:

        # Define the token endpoint and payload
        token_url = "https://api.amazon.com/auth/o2/token"
        payload = {
            'grant_type': 'authorization_code',
            'code': auth_code,
            'client_id': lwa_client_id,
            'client_secret': lwa_client_secret,
            'redirect_uri': redirect_uri
        }

        # Make the POST request to exchange the authorization code for tokens
        response = requests.post(token_url, data=payload)
        response_data = response.json()

        if response.status_code != 200:
            return HttpResponse(f"Error during token exchange: {response_data}", status=response.status_code)

        refresh_token = response_data['refresh_token']
        access_token = response_data['access_token']

        # # Save the refresh token in the database
        # Refresh_Token.objects.create(seller_id=seller_id, refresh_token=refresh_token, access_token=access_token)

        return JsonResponse(
            {
                'message': 'Authorization successful',
                'refresh_token': refresh_token,
                'access_token': access_token
            }
        )
    
    except Exception as e:
        return HttpResponse(f"Error during authorization: {e}", status=500)