from django.shortcuts import render
from django.http import HttpResponse
from sp_api.base import AccessTokenClient
import os

app_id = os.getenv('app_id')

def home(request):
    return render(request, 'index.html', app_id)

def authorization_url(request):
    url = 'https://sellingpartnerapi.amazon.com/authorize?response_type=code&app_id=' + app_id + '&redirect_uri=https://printasta-build.vercel.app/auth/redirect&state=state'
    return (url)

def redirect_view(request):
    auth_code = request.GET.get('spapi_oauth_code')
    print(auth_code)
    res = AccessTokenClient().authorize_auth_code(auth_code)
    print(res)
    return HttpResponse("Authorization successful")

