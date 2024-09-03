from django.shortcuts import render
from django.http import HttpResponse
from sp_api.base import AccessTokenClient
import os

app_id = os.getenv('app_id')

def home(request):
    
    app_id = os.getenv('app_id')

    return render(request, 'index.html', {'app_id': app_id})

def redirect_view(request):
    auth_code = request.GET.get('spapi_oauth_code')
    print(auth_code)
    res = AccessTokenClient().authorize_auth_code(auth_code)
    print(res)
    return HttpResponse("Authorization successful")

