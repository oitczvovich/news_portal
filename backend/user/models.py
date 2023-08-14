from django.contrib.auth.models import AbstractUser
from django.core.validators import (
    EmailValidator,
    MaxValueValidator,
    MinValueValidator,
    RegexValidator,
)
from django.db import models


class User(AbstractUser):
    """Модель юзер."""

    USER = 'user'
    ADMIN = 'admin'
    USER_ROLE = [
        ('user', USER),
        ('admin', ADMIN),
    ]

    username = models.CharField(
        'Имя пользователя',
        max_length=150,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^[\w.@+-_]+$',
                message='Недопустимое имя',
            )
        ],
    )
    email = models.EmailField(
        'Электронная почта',
        max_length=254,
        unique=True,
        validators=[EmailValidator],
    )
    role = models.CharField(
        'Роль', max_length=30, choices=USER_ROLE, default='user'
    )

    password = models.CharField('Пароль', max_length=150, blank=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    @property
    def is_user(self):
        return self.role == self.USER

    @property
    def is_admin(self):
        return self.role == self.ADMIN

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('id',)

        constraints = [
            models.UniqueConstraint(
                fields=('username', 'email'),
                name='unique_username_email',
            ),
        ]

    def __str__(self):
        return self.username
