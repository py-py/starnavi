from rest_framework import viewsets

from backend.models import *
from backend_rest.permissions import IsSuperUserOrIsOwnerOrReadOnly
from backend_rest.serializers import *

__all__ = ('PostViewSet', )


class PostViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsOwnerOrReadOnly,)  # TODO: change?
    permission_classes = (IsSuperUserOrIsOwnerOrReadOnly,)
    queryset = Post.objects.order_by('-date').all()
    serializer_class = PostSerializer

