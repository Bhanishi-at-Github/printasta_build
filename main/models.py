from django.db import models

# Create your models here.

class AppOrder(models.Model):
    order_id = models.CharField(max_length=50)
    order_date = models.DateField()
    order_status = models.CharField(max_length=50)
    order_total = models.DecimalField(max_digits=10, decimal_places=2)
    order_items = models.IntegerField()
    order_customer = models.CharField(max_length=50)
    order_address = models.CharField(max_length=100)

    def __str__(self):
        return self.order_id
    
