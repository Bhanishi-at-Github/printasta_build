''' This file contains the code for the views of the appAuth app. '''

import os
import requests
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from appAuth.models import User

lwa_app_id = os.getenv('lwa_app_id')
lwa_client_id = os.getenv('lwa_client_id')
lwa_client_secret = os.getenv('lwa_client_secret')
redirect_uri = os.getenv('redirect_uri')

# def register_user(request):

#     '''This function registers the user for the Amazon authorization.'''

#     if request.method=='POST':

#         try:
            
#             seller_name = request.POST.get('seller_name')
#             email = request.POST.get('email')
#             password = request.POST.get('password')

#             # Register the user
#             if not seller_name or not email or not password:
#                 return HttpResponse("Error: Missing required fields", status=400)

#             if User.objects.filter(email=email).exists():
#                 return HttpResponse("Error: User already exists", status=400)

#             user = User.objects.create(
#                 seller_name=seller_name,
#                 email=email,
#             )

#             user.set_password(password)
#             user.save()

#             return redirect(request, 'authorize.html')

#         except Exception as e:

#             return HttpResponse(
#                 f"Error during registration: {e}",
#                 status=500
#             )
        
#     return render(request, 'register_user.html')



def state_define():

    '''This function defines the state for the authorization request.'''
    import random
    import string

    state = ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))

    return state


def authorize(request):
    '''This function redirects the user to the Amazon authorization page.'''
    state = state_define()
    auth_url = f"https://sellercentral.amazon.com/apps/authorize/consent?application_id={lwa_app_id}&state={state}&version=beta"

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
        return HttpResponse(
            f"Error during authorization: {e}",
            status=500
        )
