from django.db import models
from product.models import Product, ProductImage


# Create your models here.


class OrderDetail(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_detail_sku = models.CharField(max_length=50, null=True, blank=True)
    order_detail_quantity = models.IntegerField()
    order_detail_price = models.IntegerField()

    def __str__(self):
        return str(self.order_detail_sku) + ' | ' + str(self.order_detail_quantity)


class Order(models.Model):
    order_detail = models.ManyToManyField(OrderDetail, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField(max_length=100, blank=True, null=True)
    customer_phone = models.CharField(max_length=20)
    shipping_address = models.TextField()

    order_cost = models.IntegerField(blank=True, null=True)

    status = models.CharField(choices=(
        ('received', 'received'),
        ('acknowledged', 'acknowledged'),
        ('deleivered', 'deleivered'),
    ), max_length=12, default='received')

    def __str__(self):
        return str(self.date)

    def get_order_number(self):
        base_id = 10000
        return base_id + self.id