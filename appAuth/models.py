'''Models for the appAuth app'''

from django.db import models

class RefreshToken(models.Model):

    '''Model Configuration for Refresh Token'''

    seller_id = models.CharField(default=None, max_length=255)
    refresh_token = models.CharField(max_length=255)
    access_token = models.CharField(default=None,max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:

        '''Meta Class for Refresh Token'''

        verbose_name = 'Refresh Token'
        verbose_name_plural = 'Refresh Tokens'

        permissions = [
            ('can_manage_refresh_tokens', 'Can manage Refresh Tokens'),
        ]
