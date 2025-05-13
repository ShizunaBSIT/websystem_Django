from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from product_post.models import Product
from django.urls import reverse
import random

# Create your models here.
class Order(models.Model):
    orderNum = models.CharField(max_length=150, default=str(random.randint(10000, 99999)))
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    address = models.TextField()
    phoneContact = models.IntegerField(default=0)
    placedDate = models.DateField(default=timezone.now)
    confirmDate = models.DateField(null=True, auto_now=True)
    deliveryDate = models.DateField(null=True)
    isDelivered = models.BooleanField(default=False)
    slug = models.SlugField()
    
    class Meta:
        ordering = ('user','placedDate')
    
    def __str__(self):
        return self.orderNum
    
    def get_absolute_url(self):
        return reverse("order:order_page", 
                       args=[
                           self.slug,
                       ])
    
