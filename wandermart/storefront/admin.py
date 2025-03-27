from django.contrib import admin
from storefront.models import storefront

# Register your models here.
class storefrontAdmin(admin.ModelAdmin):
    list_display = ('storename','owner',)
    prepopulated_fields = {"slugpage": ("storename",)}
    

admin.site.register(storefront, storefrontAdmin)