from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response


def add_or_del_like(self, **kwargs):
    """Поставить или удалить лайк."""
    request = kwargs['request']
    model = kwargs['model']
    serializer_type = kwargs['serializer']
    user_id = self.request.user.id
    news_id = kwargs['id']
    like = model.objects.filter(user_id=user_id, news_id=news_id)
    if like:
        like.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        model.objects.create(user_id=user_id, news_id=news_id)
        serializer = serializer_type(
            news_id,
            context={'request': request},
        )
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )
