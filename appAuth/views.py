from django.shortcuts import render
from django.http import HttpResponse
from sp_api.base import AccessTokenClient
import os

app_id = os.getenv('app_id')

def home(request):
    
    app_id = os.getenv('app_id')
    
    url = 'https://sellingpartner.amazon.com/apps/authorize/consent?application_id=' + app_id + '&state=state&version=beta'

    return render(request, 'index.html', {'app_id': app_id, 'url': url})

def redirect_view(request):
    auth_code = request.GET.get('spapi_oauth_code')
    print(auth_code)
    res = AccessTokenClient().authorize_auth_code(auth_code)
    print(res)
    return HttpResponse("Authorization successful")

