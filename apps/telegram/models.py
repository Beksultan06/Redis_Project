from django.db import models
from django.utils import timezone

# Create your models here.
class Telegram(models.Model):
    id_user = models.CharField(
        max_length=100,
        verbose_name="ID пользователя telegram"
    )
    username = models.CharField(
        max_length=255,
        verbose_name="Имя пользователя",
        blank=True, null=True
    )
    name = models.CharField(
        max_length = 155,
        verbose_name = 'Имя'
    )
    email = models.CharField(
        max_length = 155,
        verbose_name = 'Почта'
    )
    message = models.CharField(
        max_length = 155,
        verbose_name = 'Сообщение'
    )
    chat_id = models.CharField(
        max_length=100,
        verbose_name="Чат ID"
    )
    created = models.DateTimeField(
        default=timezone.now,
        verbose_name="Дата регистрации"
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural='Телеграм бот'