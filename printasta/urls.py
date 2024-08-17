"""
URL configuration for printasta project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('appAuth.urls')),
    path ('', include('main.urls')),
    
]
