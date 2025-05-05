from django.contrib import admin
from product_post.models import Product
from product_post.models import Review

# Register your models here.
class postAdmin(admin.ModelAdmin):
    list_display = ('name', 'store','dateadded',)
    prepopulated_fields = {"page": ("name","store")}

admin.site.register(Product, postAdmin)
admin.site.register(Review)