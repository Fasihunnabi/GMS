from django.contrib import admin

# Register your models here.

from .models import *


admin.site.register(ProductImage)


class MessageAdmin(admin.ModelAdmin):
    model = Message
    list_display = ['name', 'phone', 'email', 'msg']
    ordering = []
    search_fields = ['name']
    list_filter = ['name']


admin.site.register(Message, MessageAdmin)


class ProductCategoryAdmin(admin.ModelAdmin):
    model = ProductCategory
    list_display = ['name']
    ordering = []
    search_fields = ['name']


admin.site.register(ProductCategory, ProductCategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ['name', 'sku', 'category', 'original_price', 'sale_price', 'description']
    ordering = []
    search_fields = ['name']
    list_filter = ['category']


admin.site.register(Product, ProductAdmin)