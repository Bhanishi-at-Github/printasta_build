from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('redirect/', views.redirect_view, name='redirect'),
    path('authorize/', views.authorize, name='authorize'),
]
