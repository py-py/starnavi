from rest_framework import viewsets

from backend.models import *
from backend_rest.serializers import *

__all__ = ('PostViewSet', )


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.order_by('-date').all()
    serializer_class = PostSerializer

