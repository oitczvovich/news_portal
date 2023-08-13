from django.urls import include, path
from rest_framework.routers import DefaultRouter

# from .views import CommentsViewSet, UserViewSet
from django.conf import settings

router = DefaultRouter()
# router.register('users', UserViewSet, basename='users')  
# router.register('comments', CommentsViewSet, basename='comments')  

app_name = 'api'

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls.authtoken')),
]
