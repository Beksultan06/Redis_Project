from django.views import View
from .models import Product, ProductDetail
from django.shortcuts import get_object_or_404, render

class ProductView(View):
    model = Product
    template_name = 'product/product.html'

    def get(self, request):
        products = Product.objects.all()
        return render(request, self.template_name, {'products': products})

class ProductDetailView(View):
    model = ProductDetail
    template_name = 'product/product_detail.html'  # Шаблон для детального просмотра продукта

    def get(self, request, product_id):
        # Получаем объект продукта по его ID или возвращаем 404, если продукт не найден
        product = get_object_or_404(Product, pk=product_id)
        return render(request, self.template_name, {'product': product})