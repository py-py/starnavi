from rest_framework import serializers

from backend.models import *

__all__ = ('LikeSerializer', )


class LikeSerializer(serializers.Serializer):
    post_id = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())
    status = serializers.ChoiceField(choices=STATUS)
