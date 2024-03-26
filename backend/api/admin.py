from django.contrib import admin
from .models import *

# Unregister the old Product admin
if admin.site.is_registered(Product):
    admin.site.unregister(Product)

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'prescription_required']

admin.site.register(Review)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["user","createdAt","totalPrice"]