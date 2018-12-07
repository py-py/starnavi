from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

from backend_rest.views import *

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('posts', PostViewSet)


urlpatterns = [
    path('token', obtain_jwt_token),
    path('like', LikeView.as_view())
] + router.urls
