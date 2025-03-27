from django.contrib import admin
from product_post.models import Product

# Register your models here.
class postAdmin(admin.ModelAdmin):
    pass

admin.site.register(Product, postAdmin)