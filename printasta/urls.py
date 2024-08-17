"""
URL configuration for printasta project.
"""
from django.contrib import admin
from django.urls import path
from appAuth.views import amazonAuth, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('amazon/auth', amazonAuth),

]
