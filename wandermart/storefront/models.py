from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

STORE_STATUS_CHOICES = (
    ('open', 'Open'),
    ('closed', 'Closed'),
    ('removed', 'Removed'),
)

# Storefront model
class storefront(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    storename = models.CharField(max_length=100, unique=True)
    address = models.TextField(default="No Physical Store")
    phonecontact = models.CharField(max_length=11)
    emailcontact = models.CharField(max_length=100)
    storestatus = models.CharField(max_length=10, choices=STORE_STATUS_CHOICES, default='open')
    datecreated = models.DateField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slugpage = models.SlugField(default="")

    def __str__(self):
        return self.storename

# Product model
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    store = models.ForeignKey(storefront, on_delete=models.CASCADE, related_name='store_products')  # Added related_name
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # This will return the URL for the product detail page
        return reverse('product_detail', kwargs={'product_id': self.id})