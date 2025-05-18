from django.db import models
from storefront.models import Storefront
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils import timezone
from django.db.models import Avg
from cloudinary.models import CloudinaryField
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import UploadedFile

from taggit.managers import TaggableManager

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')

# product listing status choices
PRODUCT_LISTING_STATUS_CHOICES = (
    ('draft','Draft'),
    ('published','Published'),
    ('archived','Archived'),
) 


####### CLOUDINARY
FILE_UPLOAD_MAX_MEMORY_SIZE = 1024 * 1024 * 10  # 10mb


def file_validation(file):
    if not file:
        raise ValidationError("No file selected.")

    # For regular upload, we get UploadedFile instance, so we can validate it.
    # When using direct upload from the browser, here we get an instance of the CloudinaryResource
    # and file is already uploaded to Cloudinary.
    # Still can perform all kinds on validations and maybe delete file, approve moderation, perform analysis, etc.
    if isinstance(file, UploadedFile):
        if file.size > FILE_UPLOAD_MAX_MEMORY_SIZE:
            raise ValidationError("File shouldn't be larger than 10MB.")

## https://cloudinary.com/documentation/python_sample_projects


################# Product Listing
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    store = models.ForeignKey(Storefront, on_delete=models.CASCADE)
    stock = models.BigIntegerField()
    publish = models.DateTimeField(default=timezone.now)
    dateadded = models.DateField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True) 
    slug = models.SlugField(max_length=250, unique_for_date='publish') # for URL purposes
    status = models.CharField(max_length=10, choices=PRODUCT_LISTING_STATUS_CHOICES, default='draft')
    #image = models.ImageField(upload_to='products/', null=True, blank=True)
    image = CloudinaryField('image',validators=[file_validation], null=True, blank=True)
    avg_rating = models.FloatField(default=0.0)
    published = PublishedManager()

    tags = TaggableManager()

    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-avg_rating','price']

    # absolute page url
    def get_absolute_url(self):
        return reverse("product_post:product_detail", args=[
            self.publish.year, 
            self.publish.month, 
            self.publish.day, 
            self.slug])

# product reviews
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=1, validators=[MinValueValidator(1),MaxValueValidator(5)])
    text = models.TextField()
    dateadded = models.DateField(auto_now_add=True)
    dateupdated = models.DateField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('dateadded',)
    
    def __str__(self):
        return f'Comment by {self.user} on {self.product}'
    
    # average rating change
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.product.avg_rating = self.product.reviews.aggregate(Avg('rating'))['rating__avg']
        self.product.save()



