from django.contrib import admin
from apps.product.models import Product, ProductDetail, Send_Email
# Register your models here.
admin.site.register(ProductDetail)
admin.site.register(Product)
admin.site.register(Send_Email)