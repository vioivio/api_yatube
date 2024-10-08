from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, GroupViewSet, PostViewSet

VERSION = 'v1'
app_name = 'api'

v1_router = DefaultRouter()

v1_router.register('groups', GroupViewSet, basename='groups')
v1_router.register('posts', PostViewSet, basename='posts')
v1_router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments')

urlpatterns = [
    path(f'{VERSION}/', include(v1_router.urls)),
    path(f'{VERSION}/api-token-auth/', views.obtain_auth_token),
]
