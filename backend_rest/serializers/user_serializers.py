from backend.models import *
from rest_framework import serializers

from backend_rest.serializers import PostSerializer

__all__ = ('UserSerializer', 'SignUpSerializer', )


class UserSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True)
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('username', 'full_name', 'posts', )

    def get_full_name(self, obj):
        return obj.get_full_name()


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name', 'clearbit', 'emailhunter', )
