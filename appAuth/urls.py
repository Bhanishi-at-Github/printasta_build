from django.urls import path
from appAuth import views

urlpatterns = [

    path('', views.amazonAuth, name='amazonAuth'),
    path('callback/', views.amazon_callback, name='amazon_callback'),
    path('token/', views.get_token, name='get_token'),

]


