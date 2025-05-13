from django.contrib import admin
from order.models import Order

# Register your models here.
class orderAdmin(admin.ModelAdmin):
    list_display = ('user', 'product')
    prepopulated_fields = {"slug": ("orderNum",)}

admin.site.register(Order, orderAdmin)