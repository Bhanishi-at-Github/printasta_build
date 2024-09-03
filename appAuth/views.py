from django.shortcuts import render, redirect
from django.http import HttpResponse
from sp_api.base import AccessTokenClient
import os

lwa_app_id = os.getenv('lwa_app_id')
lwa_client_secret = os.getenv('lwa_client_secret')
redirect_uri = os.getenv('redirect_uri')


def state_define():
    import random
    state = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=14))
    return state

def home(request):
    return render(request, 'index.html', lwa_app_id)

def authorize(request):

    state = state_define()
    auth_url = f"https://sellercentral.amazon.com/apps/authorize/consent?application_id={lwa_app_id}&state={state}&version=beta"

    return redirect(auth_url)

def redirect_view(request):

    auth_code = request.GET.get('spapi_oauth_code')

    if not auth_code:
        return HttpResponse("Error: spapi_oauth_code not received", status=400)
    
    try:
        # Initialize AccessTokenClient with credentials
        client = AccessTokenClient(lwa_client_secret, redirect_uri)

        # Exchange the authorization code for an access token and refresh token
        tokens = client.exchange_auth_code_for_tokens(auth_code)

        refresh_token = tokens['refresh_token']
        access_token = tokens['access_token']



        return HttpResponse("Authorization successful", status=200)
    
    except Exception as e:
        return HttpResponse(f"Error during authorization: {e}", status=500)
    


