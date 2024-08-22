from django.db import models

# Create your models here.

class AmazonAuth(models.Model):

    selling_partner_id = models.CharField(max_length=255, null=True, blank=True)
    amazon_state = models.CharField(max_length=255, null=True, blank=True)
    amazon_callback_uri = models.CharField(max_length=255, null=True, blank=True)
    access_token = models.CharField(max_length=255, null=True, blank=True)
    refresh_token = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.selling_partner_id
    
    class Meta:

        verbose_name = 'Amazon Auth'
        verbose_name_plural = 'Amazon Auths'
        db_table = 'amazon_auth'
        ordering = ['-created_at']
