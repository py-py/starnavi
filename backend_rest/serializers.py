from django.contrib.auth.models import User
from rest_framework import serializers

from backend.models import *

__all__ = ('UserSerializer', 'PostSerializer', 'LikeSerializer', )


class PostSerializer(serializers.ModelSerializer):
    # user # TODO: fix
    class Meta:
        model = Post
        fields = ('id', 'text', 'count_likes', 'count_dislikes', 'user')


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    posts = PostSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'full_name', 'posts')

    def get_full_name(self, obj):
        return obj.get_full_name()


class LikeSerializer(serializers.Serializer):
    post_id = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())
    status = serializers.ChoiceField(choices=STATUS)
