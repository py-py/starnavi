from django.conf import settings
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_swagger.views import get_swagger_view

from backend_rest.views import *

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('posts', PostViewSet)
router.register('signup', SignUpViewSet, base_name='signup')

urlpatterns = [
    path('token/', obtain_jwt_token, name='token'),
    path('likes/', LikeView.as_view(), name='likes'),
] + router.urls


if settings.DEBUG:
    schema_view = get_swagger_view(title='StarNavi API')
    internal_urlpatterns = [
        path('docs/', schema_view)
    ]
    urlpatterns += internal_urlpatterns