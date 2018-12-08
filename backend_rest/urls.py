from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

from backend_rest.views import *

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('posts', PostViewSet)
router.register('signup', SignUpViewSet, base_name='signup')

urlpatterns = [
    path('token/', obtain_jwt_token, name='token'),
    path('likes/', LikeView.as_view(), name='likes'),
] + router.urls
