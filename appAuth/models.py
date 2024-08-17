from django.db import models

# Create your models here.

class AmazonAuthUsers(models.Model):

    seller_id = models.CharField(max_length=255)
    mws_auth_token = models.CharField(max_length=255)
    refresh_token = models.CharField(max_length=255)
    access_token = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.seller_id
    
    class Meta:

        verbose_name = 'Amazon Auth User'
        verbose_name_plural = 'Amazon Auth Users'
        db_table = 'amazon_auth_users'
        ordering = ['-created_at']

