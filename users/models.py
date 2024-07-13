from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Класс для описания модели Пользователя."""

    username = None

    email = models.EmailField(unique=True, verbose_name='почта')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return f'{self.email}'
