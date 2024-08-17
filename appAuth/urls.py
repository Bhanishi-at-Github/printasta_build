from django.urls import path
from appAuth import views

urlpatterns = [
    path('auth/', views.amazonAuth, name='amazonAuth'),
    path('auth/callback', views.amazon_callback, name='amazon_callback'),

]


