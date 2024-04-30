from django.contrib import admin
from apps.product.models import Product, ProductDetail
# Register your models here.
admin.site.register(ProductDetail)
admin.site.register(Product)