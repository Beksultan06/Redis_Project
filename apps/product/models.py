from django.db import models
from ckeditor.fields import RichTextField


class Product(models.Model):
    title = models.CharField(
        max_length=100, 
        verbose_name='Заголовка'
        )
    description = models.TextField(
        verbose_name='описание'
        )
    image = models.ImageField(
        upload_to='product', 
        verbose_name='фото'
        )
    created = models.DateTimeField(
        auto_now_add=True, 
        verbose_name='дата созлание'
        )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Продукты'

class ProductDetail(models.Model):
    price = models.CharField(
        max_length=100,
        verbose_name='Цена'
    )
    extra_info = RichTextField(
        verbose_name='Описание продукта'
    )

    def __str__(self) -> str:
        return self.price

    class MEta:
        verbose_name_plural = 'Детально продукты'