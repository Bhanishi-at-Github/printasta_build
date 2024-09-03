from django.shortcuts import render
from django.http import HttpResponse
from sp_api.base import AccessTokenClient
import os
from rest_framework.response import Response

app_id = os.getenv('app_id')
redirect_uri = os.getenv('redirect_uri')

def home(request):
    return render(request, 'index.html', app_id)

def authorize(request):

    redirect_uri = os.getenv('redirect_uri')
    
    auth_url = {

        "base_url": "https://sellingpartnerapi-na.amazon.com/authorize",
        "app_id": app_id,
        "redirect_uri": redirect_uri,
        "state": "state",
        "version": "beta",
    }

    return Response(auth_url)

def redirect_view(request):
    auth_code = request.GET.get('spapi_oauth_code')
    print(auth_code)
    res = AccessTokenClient().authorize_auth_code(auth_code)
    print(res)
    return HttpResponse("Authorization successful")

