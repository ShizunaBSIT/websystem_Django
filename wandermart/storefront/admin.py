from django.contrib import admin
from models import storefront

# Register your models here.
class storefrontAdmin(admin.ModelAdmin):
    pass

admin.site.register(storefront, storefrontAdmin)