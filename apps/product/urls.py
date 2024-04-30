from django.urls import path
from .views import ProductDetailView, ProductView

urlpatterns = [
    path('product', ProductView.as_view(), name='product'),
     path('product/<int:product_id>/', ProductDetailView.as_view(), name='product_detail'),
]
