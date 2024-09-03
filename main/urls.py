from django.urls import path 
from main import views

urlpatterns = [
    path('', views.home, name='home'),
    path('orders/', views.orders, name='orders'),
]