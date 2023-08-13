from django.contrib.auth.models import AbstractUser
from django.core.validators import (
    EmailValidator,
    MaxValueValidator,
    MinValueValidator,
    RegexValidator,
)
from django.db import models

from user.models import User
from news.models import News


class Comment(models.Model):
    """Модель комментариев."""

    news = models.ForeignKey(
        News,
        related_name='comments',
        on_delete=models.CASCADE,
        verbose_name='Новость',
    )
    text = models.TextField(
        verbose_name='Комментарий',
    )
    author = models.ForeignKey(
        User,
        related_name='comments',
        on_delete=models.CASCADE,
        verbose_name='Автор комментария',
    )
    pub_date = models.DateTimeField(
        auto_now_add=True, db_index=True, verbose_name='Дата публикации'
    )

    class Meta:
        ordering = ('-pub_date',)
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.text[:42]


class Like(models.Model):
    """Модель лайки."""

    news = models.ForeignKey(
        News,
        on_delete=models.CASCADE,
        related_name='like',
        verbose_name='Новость',
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='like',
        verbose_name='Пользователь',
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'news'], name="unique_like"
            )
        ]
