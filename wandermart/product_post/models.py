from django.db import models
from storefront.models import storefront
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils import timezone

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
    store = models.ForeignObject(storefront, on_delete=models.CASCADE)
    stock = models.BigIntegerField()
    publish = models.DateTimeField(default=timezone.now)
    dateadded = models.DateField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True) 
    page = models.SlugField(max_length=250, unique_for_date='publish') # for URL purposes
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



# absolute page url
def get_absolute_url(self):
    return reverse("product:product_post", args=[
        self.publish.year, 
        self.publish.month, 
        self.publish.day, 
        self.page])