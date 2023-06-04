from django.contrib import admin
from .models import Customer, Product


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_on']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'customer', 'status', 'created_on']


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
