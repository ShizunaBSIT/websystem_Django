from django.db import models
from storefront.models import storefront
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

# Product listing status choices
PRODUCT_LISTING_STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published'),
    ('archived', 'Archived'),
)

# Product Listing Model
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    store = models.ForeignKey(storefront, on_delete=models.CASCADE, related_name='product_post_products')  # <-- changed here
    stock = models.BigIntegerField()
    publish = models.DateTimeField(default=timezone.now)
    dateadded = models.DateField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    page = models.SlugField(max_length=250, unique_for_date='publish')  # for URL purposes
    status = models.CharField(max_length=10, choices=PRODUCT_LISTING_STATUS_CHOICES, default='draft')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['price']

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={
            'year': self.publish.year,
            'month': self.publish.month,
            'day': self.publish.day,
            'product': self.page,
        })


# Product Review Model
class Review(models.Model):
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.product.name} by {self.user.username}"
