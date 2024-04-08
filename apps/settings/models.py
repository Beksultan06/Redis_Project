from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Settings(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name = 'Заголовок'
    )
    descriptions = models.CharField(
        max_length = 355,
        verbose_name = 'Описание'
    )
    image = models.ImageField(
        upload_to='settings/',
        verbose_name='Фото'
    )

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name_plural = 'настройка'

class About(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    descriptions = RichTextField(
        verbose_name='Описание'
    )

    def __Str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'О нас'
