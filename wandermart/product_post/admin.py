from django.contrib import admin
from models import Product

# Register your models here.
class postAdmin(admin.ModelAdmin):
    pass

admin.site.register(Product, postAdmin)