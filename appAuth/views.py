from django.shortcuts import render, redirect
from django.http import HttpResponse
from sp_api.base import AccessTokenClient
import os

app_id = os.getenv('lwa_app_id')
client_secret = os.getenv('lwa_client_secret')
redirect_uri = os.getenv('redirect_uri')

def home(request):
    return render(request, 'index.html', app_id)

def authorize(request):

    if not app_id or not redirect_uri:
        return HttpResponse("app_id or redirect_uri not set", status=400)
    
    auth_url = f"https://sellercentral.amazon.com/apps/authorize/consent?application_id={app_id}&state=stateexample&version=beta"

    return redirect(auth_url)

def redirect_view(request):

    auth_code = request.GET.get('spapi_oauth_code')

    if not auth_code:
        return HttpResponse("Error: spapi_oauth_code not received", status=400)
    
    try:
        # Initialize AccessTokenClient with credentials
        client = AccessTokenClient(
            lwa_app_id=app_id,
            lwa_client_secret=client_secret,
        )
        res = client.authorize_auth_code(auth_code)
        print(res)
        return HttpResponse("Authorization successful")
    
        # After successful authorization, you can store the refresh token in a secure location
        # and use it to get access tokens in the future
    
    except Exception as e:
        return HttpResponse(f"Error during authorization: {e}", status=500)
    


