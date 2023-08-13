from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.validators import UniqueValidator


from user.models import User
from news.models import News
from comments.models import Comment, Like


class UserRegistrSerializer(serializers.ModelSerializer):
    """Сериализатор для регистраци пользователей."""

    username = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())],
    )
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())],
    )

    class Meta:
        model = User
        fields = [
            'username',
            'email',
        ]

    def validate_username(self, user):
        if user.lower() == 'me':
            raise serializers.ValidationError('username не может быть "me".')
        return user


class NewsSerializer (serializers.ModelSerializer):

    class Meta:
        model = News
        fields = ('author', 'title', 'text')


class CommentsSerializer (serializers.ModelSerializer):

    class Meta:
        model = News
        fields = ('news', 'author', 'text')