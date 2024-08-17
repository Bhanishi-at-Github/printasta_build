"""
URL configuration for printasta project.
"""
from django.contrib import admin
from django.urls import path
from appAuth.views import amazonAuth

urlpatterns = [
    path('admin/', admin.site.urls),
    path('amazon/auth', amazonAuth),

]
