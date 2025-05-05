from django.contrib import admin
from storefront.models import Storefront

# Register your models here.
class storefrontAdmin(admin.ModelAdmin):
    list_display = ('storename','owner',)
    prepopulated_fields = {"slug": ("storename",)}
    

admin.site.register(Storefront, storefrontAdmin)