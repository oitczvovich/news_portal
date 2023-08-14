from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.validators import UniqueValidator


from user.models import User
from news.models import News
from comments.models import Comment, Like


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'role'
        ]


class UserRegistrSerializer(UserSerializer):
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


class NewsSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        default=serializers.CurrentUserDefault(),
        slug_field='username',
        read_only=True,
    )
    comments = serializers.StringRelatedField(many=True)

    class Meta:
        model = News
        fields = ('author', 'title', 'text', 'comments')


class CreatNewsSerializer(NewsSerializer):

    class Meta:
        model = News
        fields = ('author', 'title', 'text')


class CommentsSerializer (serializers.ModelSerializer):
    news = serializers.SlugRelatedField(
        slug_field='text',
        read_only=True,
    )
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
    )

    class Meta:
        model = Comment
        fields = ('news', 'author', 'text')