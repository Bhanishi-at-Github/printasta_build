from django.urls import path
from appAuth.views import AmazonAuth

urlpatterns = [

    path('', AmazonAuth.as_view(), name='amazon_auth'),
]


