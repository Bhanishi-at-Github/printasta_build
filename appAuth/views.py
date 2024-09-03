from django.shortcuts import render, redirect
from django.http import HttpResponse
from sp_api.base import AccessTokenClient
import os

app_id = os.getenv('app_id')
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
    print(auth_code)
    res = AccessTokenClient().authorize_auth_code(auth_code)
    print(res)
    return HttpResponse("Authorization successful")

