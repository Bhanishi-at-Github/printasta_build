'''Urls for appAuth app'''

from django.urls import path
from . import views

urlpatterns = [
    # path('register_user/', views.register_user, name='register_user'),
    path('redirect/', views.redirect_view, name='redirect'),
    path('authorize/', views.authorize, name='authorize'),
]
