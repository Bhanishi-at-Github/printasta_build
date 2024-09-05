''' This file contains the code for the views of the appAuth app. '''

import os
import requests
from django.shortcuts import redirect
from django.http import HttpResponse
from django.http import JsonResponse

lwa_app_id = os.getenv('lwa_app_id')
lwa_client_id = os.getenv('lwa_client_id')
lwa_client_secret = os.getenv('lwa_client_secret')
redirect_uri = os.getenv('redirect_uri')


def state_define():

    '''This function defines the state for the authorization request.'''
    return "stateexample"

# f"https://sellercentral.amazon.com/apps/authorize/consent?
# application_id={lwa_app_id}
# &state={state}
# &version=beta"

def authorize(request):
    '''This function redirects the user to the Amazon authorization page.'''
    state = state_define()
    auth_url = {
        'base_url': 'https://sellercentral.amazon.com/apps/authorize/consent',
        'application_id': lwa_app_id,
        'state': state,
        'version': 'beta'
    }
    
    return redirect(request, auth_url)

def redirect_view(request):
    '''This function handles the redirection from the Amazon authorization page.'''

    auth_code = request.GET.get('spapi_oauth_code')

    # seller_id = request.GET.get('seller_id')

    if not auth_code:
        return HttpResponse("Error: spapi_oauth_code not received", status=400)

    try:

        token_url = "https://api.amazon.com/auth/o2/token"
        payload = {
            'grant_type': 'authorization_code',
            'code': auth_code,
            'client_id': lwa_client_id,
            'client_secret': lwa_client_secret,
            'redirect_uri': redirect_uri
        }

        response = requests.post(token_url, data=payload)
        response_data = response.json()

        if response.status_code != 200:

            return HttpResponse(
                f"Error during token exchange: {response_data}",
                status=response.status_code
            )

        refresh_token = response_data['refresh_token']
        access_token = response_data['access_token']

        # Refresh_Token.objects.create(
            # seller_id=seller_id, 
            # refresh_token=refresh_token, 
            # access_token=access_token
        # )

        return JsonResponse(
            {
                'message': 'Authorization successful',
                'refresh_token': refresh_token,
                'access_token': access_token
            }
        )

    except Exception as e:
        return HttpResponse(f"Error during authorization: {e}", status=500)
