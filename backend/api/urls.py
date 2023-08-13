from django.urls import include, path
from rest_framework.routers import DefaultRouter


from .views import NewsViewSet, CommentsViewSet
from django.conf import settings


router_v1 = DefaultRouter()

router_v1.register(
    r'news/(?P<news_id>\d+)/comments',
    CommentsViewSet,
    basename='comments',
)
# router.register('users', UserViewSet, basename='users')  
router_v1.register('news', NewsViewSet, basename='news')
# router_v1.register('comments', CommentsViewSet, basename='comments')


urlpatterns = [
    path('', include(router_v1.urls)),
    path('auth/', include('djoser.urls.authtoken')),
    path('v1/', include(router_v1.urls))
]
