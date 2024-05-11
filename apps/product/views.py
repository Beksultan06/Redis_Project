from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView, View
from .models import Product, ProductDetail, Send_Email
from django.core.paginator import Paginator
from apps.product.utils import send_contact_email


class ProductListView(ListView):
    model = Product, Send_Email
    template_name = 'product/product.html'
    context_object_name = 'products'
    paginate_by = 3  # Укажите количество продуктов на странице

    def get_queryset(self):
        return Product.objects.all().order_by('-created')

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        send_mail(
            'Cheff Contact',
            f"""Здравствуйте.
                    Спасибо за обратную связь, мы скоро свами свяжемся.
                    Ваше Имя: {name}
                    Ваш email: {email}
                    Ваше сообщение: {message}...

                    Если вы ошиблись при указании данных можете обратно зайти на сайт и оставить новый отзыв с исправленными
                    данными! """,
            "noreply@somehost.local",
            ["nurlanuuulubeksultan@gmail.com"]
        )
        send_contact_email.delay(name, email, message)

        return redirect('index')



class ProductDetailView(View):
    model = ProductDetail
    template_name = 'product/product_detail.html'  # Шаблон для детального просмотра продукта

    def get(self, request, product_id):
        # Получаем объект продукта по его ID или возвращаем 404, если продукт не найден
        product = get_object_or_404(Product, pk=product_id)
        return render(request, self.template_name, {'product': product})