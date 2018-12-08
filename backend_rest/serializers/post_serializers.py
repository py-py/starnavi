from rest_framework import serializers

from backend.models import *

__all__ = ('PostSerializer', )


class PostSerializer(serializers.ModelSerializer):
    timestamp = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('id', 'text', 'count_likes', 'count_dislikes', 'timestamp', )

    def get_timestamp(self, obj):
        return int(obj.date.timestamp() * 1000)

    def to_internal_value(self, data):
        data = super(PostSerializer, self).to_internal_value(data)
        data['user'] = self.context['request'].user
        return data
