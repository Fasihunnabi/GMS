from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(OrderDetail)
admin.site.register(Order)



# admin.site.register(OrderProductItem)