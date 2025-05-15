from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

STORE_STATUS_CHOICES = (
    ('open','Open'),
    ('closed','Closed'),
    ('removed','Removed'),
)

# storefront
class Storefront(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    storename = models.CharField(max_length=100, unique=True)
    address = models.TextField(default="No Physical Store")
    phonecontact = models.CharField(max_length=11)
    emailcontact = models.CharField(max_length=100)
    storestatus = models.CharField(max_length=10, choices=STORE_STATUS_CHOICES, default='open')
    datecreated = models.DateField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(default="")


    def __str__(self):
        return self.storename
    
    def get_absolute_url(self):
        return reverse("storefront_detail", 
                       args=[
                           self.slug
                       ])
    
    
