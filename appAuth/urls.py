from django.urls import path
from appAuth import views

urlpatterns = [

    path('', views.amazonAuth, name='amazonAuth'),
    path('callback/', views.amazon_callback, name='amazon_callback'),
    path('get_orders/', views.get_orders, name='get_orders'),

]
