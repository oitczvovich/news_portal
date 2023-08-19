from django.urls import include, path
from rest_framework.routers import DefaultRouter
from djoser.views import UserViewSet

from .views import NewsViewSet, CommentsViewSet
from django.conf import settings


router_v1 = DefaultRouter()

router_v1.register('news', NewsViewSet, basename='news')
router_v1.register(
    r'news/(?P<news_id>\d+)/comments',
    CommentsViewSet,
    basename='comments',
)

urlpatterns = [
    path('', include(router_v1.urls)),
    path('auth/register/', UserViewSet.as_view({'post': 'create'}), name="register"),
    path('auth/users/me/', UserViewSet.as_view({'get': 'me'}), name='current_user'),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/', include('djoser.urls.authtoken')),
]
