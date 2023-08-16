from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.decorators import api_view, action, permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework import (
    filters,
    permissions,
    status,
    viewsets,
)

from .permissions import (
    IsAdmin,
    IsAdminOrAuthor,
    IsOwnerOrReadOnly
)

from news.models import News
from user.models import User
from comments.models import Comment, Like
from .pagination import PageNumberPagination
from .serializers import (
    NewsSerializer,
    UserRegistrSerializer,
    CommentsSerializer,
    CreatNewsSerializer,
    LikeSerializer
)
from .utils import add_or_del_like

#TODO сделать delete коментариев
#TODO При получении списка новостей и одной конкретной новости нужно показать
#TODO количество лайков и комментариев. 
#TODO сделать ручку PUT News 


class NewsViewSet(viewsets.ModelViewSet):
    http_method_names = ('get', 'post', 'put', 'delete')
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def get_serializer_class(self):
        if self.request.method in ('POST', 'PUT'):
            return CreatNewsSerializer
        return NewsSerializer

    def get_permissions(self):
        if self.action in ('destroy', 'update',):
            return (IsAdminOrAuthor(),)
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def destroy(self, request, *args, **kwargs):
        news = self.get_object()
        news.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @permission_classes(IsAdminOrAuthor)
    def perform_update(self, serializer):
        serializer.save()

    @action(
        methods=['get'],
        detail=True,
        url_path='like',
    )
    def like(self, request, pk):
        return add_or_del_like(
            self,
            id=pk,
            request=request,
            serializer=LikeSerializer,
            model=Like
        )


class CommentsViewSet(viewsets.ModelViewSet):
    http_method_names = ('get', 'post', 'delete')
    serializer_class = CommentsSerializer

    def get_queryset(self):
        news = get_object_or_404(News, pk=self.kwargs.get('news_id'))
        return news.comments.all()

    def perform_create(self, serializer):
        news_id = self.kwargs.get('news_id')
        news = get_object_or_404(News, id=news_id)
        serializer.save(author=self.request.user, news=news)

    def get_permissions(self):
        if self.action == 'destroy':
            return (IsAdminOrAuthor(),)
        return super().get_permissions()

    def destroy(self, request, *args, **kwargs):
        news = self.get_object()
        news.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
