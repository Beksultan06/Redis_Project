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

class Review(models.Model):
    last_name = models.CharField(
        max_length=155,
        verbose_name='имя'
    )
    email = models.EmailField(
        verbose_name='Электронная почта'
    )
    message = models.CharField(
        max_length=355,
        verbose_name='Сообщение'
    )

    def __str__(self) -> str:
        return self.last_name
    
    class Meta: 
        verbose_name_plural = 'Отзывы'


class Send_Email(models.Model):
    name = models.CharField(
        max_length=155,
        verbose_name='Имя'
    )
    email = models.EmailField(
        verbose_name='Почта'
    )
    message = models.TextField(
        verbose_name='Сообщение'
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = 'Форма обратного связи'
