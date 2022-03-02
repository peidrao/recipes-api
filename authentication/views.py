from datetime import datetime

from rest_framework import viewsets, status
from rest_framework.response import Response

from authentication.models import User
from authentication.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer

    def destroy(self, request, *args, **kwargs):
        try:
            user = self.queryset.get(id=kwargs['pk'])
            user.is_active = False
            user.deleted_at = datetime.now()
            user.save()
        except User.DoesNotExist:
            return Response(data='User does not exists', status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)

    
