from django.contrib.auth.models import AbstractUser
from django.core.validators import (
    EmailValidator,
    MaxValueValidator,
    MinValueValidator,
    RegexValidator,
)
from django.db import models

from user.models import User


class News(models.Model):
    """ Модель новости."""
    author = models.ForeignKey(
        User,
        related_name='news',
        on_delete=models.CASCADE,
        verbose_name='Автор новости',
    )
    title = models.CharField(
        'Заголовок новости',
        max_length=200,
    )
    text = models.TextField('Текст новости')
    pub_date = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name='Дата публикации'
    )



    class Meta:
        ordering = ('-id',)
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return f'{self.pub_date} - {self.title} - {self.author}'
