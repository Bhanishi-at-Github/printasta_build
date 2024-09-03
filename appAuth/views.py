from django.shortcuts import render
from django.http import HttpResponse
from sp_api.base import AccessTokenClient
import os

APP_ID = os.getenv('app_id')

def home(request):
    return render(request, 'index.html', {'app_id': APP_ID})

def redirect_view(request):
    auth_code = request.GET.get('spapi_oauth_code')
    print(auth_code)
    res = AccessTokenClient().authorize_auth_code(auth_code)
    print(res)
    return HttpResponse("Authorization successful")

