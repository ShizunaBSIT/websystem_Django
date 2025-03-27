from django.db import models
from storefront.models import storefront

# product listing status choices
PRODUCT_LISTING_STATUS_CHOICES = (
    ('draft','Draft'),
    ('published','Published'),
    ('archived','Archived'),
) 

# Product Listing
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    store = models.ForeignKey(storefront, on_delete=models.CASCADE)
    stock = models.BigIntegerField()
    dateadded = models.DateField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True) 
    page = models.SlugField(unique_for_date='dateadded')
    status = models.CharField(max_length=10, choices=PRODUCT_LISTING_STATUS_CHOICES, default='draft')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ['price']
