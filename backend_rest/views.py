from django.contrib.auth.models import User
from rest_framework import viewsets, views, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from backend.models import *
from backend_rest.permissions import IsOwnerOrReadOnly, IsSuperUserOrIsOwnerOrReadOnly
from backend_rest.serializers import *

__all__ = ('UserViewSet', 'PostViewSet', 'LikeView')


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.exclude(is_superuser=True).all()
    serializer_class = UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsOwnerOrReadOnly,)  # TODO: change?
    permission_classes = (IsSuperUserOrIsOwnerOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class LikeView(views.APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        serializer = LikeSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            post = serializer.validated_data['post_id']
            like, is_created = Like.objects.get_or_create(user=user, post=post)
            like.status = serializer.validated_data['status']
            like.save()
            # TODO: empty data ?
            return Response(status=status.HTTP_200_OK)
        raise Exception(serializer.errors)
