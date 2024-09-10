'''Models for the appAuth app'''

from django.db import models

class User(models.Model):
    
    '''Model Configuration for User'''

    seller_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    refresh_token = models.CharField(max_length=255, null=True)
    access_token = models.CharField(max_length=255, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.seller_name
