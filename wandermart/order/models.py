from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from product_post.models import Product

# Create your models here.
class Order(models.Model):
    productName = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    address = models.TextField()
    phoneContact = models.IntegerField
    placedDate = models.DateField(auto_now_add=True)
    confirmDate = models.DateField(null=True, auto_now=True)
    deliveryDate = models.DateField(null=True)
    isDelivered = models.BooleanField(default=False)
    
    class Meta:
        ordering = ('placedDate',)
    
    def __str__(self):
        return self.productName
