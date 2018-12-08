from django.contrib.auth.models import User
from rest_framework import mixins
from rest_framework import viewsets

from backend_rest.serializers import *

__all__ = ('UserViewSet', 'SignUpViewSet', )


class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    queryset = User.objects.exclude(is_superuser=True).all()
    serializer_class = UserSerializer


class SignUpViewSet(mixins.CreateModelMixin,
                    viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = SignUpSerializer
    permission_classes = ()
    authentication_classes = ()

    def perform_create(self, serializer):
        user = User.objects.create_user(**serializer.validated_data)
        user.set_password(serializer.validated_data['password'])
        user.save()

