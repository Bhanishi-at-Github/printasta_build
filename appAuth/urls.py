'''Urls for appAuth app'''

from django.urls import path
from . import views

urlpatterns = [
    path('redirect/', views.redirect_view, name='redirect'),
    path('authorize/', views.authorize, name='authorize'),
]
