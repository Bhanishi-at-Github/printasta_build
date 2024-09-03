from django.db import models

# Create your models here.

class Refresh_Token(models.Model):
    
    seller_id = models.CharField(default=None, max_length=255)
    refresh_token = models.CharField(max_length=255)
    access_token = models.CharField(default=None,max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.seller_id
    
    class Meta:
        verbose_name = 'Refresh Token'
        verbose_name_plural = 'Refresh Tokens'

        