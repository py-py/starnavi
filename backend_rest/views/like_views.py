from rest_framework import views, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from backend.models import *
from backend_rest.serializers import *

__all__ = ('LikeView', )


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
            return Response(status=status.HTTP_200_OK)
        raise Exception(serializer.errors)

