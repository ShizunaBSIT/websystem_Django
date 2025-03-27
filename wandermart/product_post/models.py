from django.db import models
from storefront.models import storefront
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

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
    page = models.SlugField(default="") # for URL purposes
    status = models.CharField(max_length=10, choices=PRODUCT_LISTING_STATUS_CHOICES, default='draft')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['price']

# product reviews
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=1, validators=[MinValueValidator(1),MaxValueValidator(5)])
    text = models.TextField()
    dateadded = models.DateField(auto_now_add=True)

