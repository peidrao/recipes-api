import jwt

from django.utils import timezone
from django.conf import settings
from rest_framework import viewsets, status, exceptions, views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics


from authentication.models import User
from authentication.serializers import ChangePasswordSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer

    def destroy(self, request, *args, **kwargs):
        try:
            user = self.queryset.get(id=kwargs['pk'])
            user.is_active = False
            user.deleted_at = timezone.now()
            user.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            return Response(data='User does not exists', status=status.HTTP_404_NOT_FOUND)       
        

class ChangePasswordViewSet(generics.UpdateAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = ChangePasswordSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            check = user.check_password(
                serializer.data.get("old_password")
            )

            if not check:
                return Response(
                    {"old_password": "Senha errada."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            user.set_password(serializer.data.get("new_password"))
            user.save()

            return Response(None, status=status.HTTP_204_NO_CONTENT)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TokenIsValidViewSet(views.APIView):
    def get(self, request):
        return Response(request.data)

    def post(self, request, *args, **kwargs):
        try:
            token = request.data["access"]
            decode = jwt.decode(token, settings.SECRET_KEY,
                                algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('access_token expired')
        except jwt.InvalidSignatureError:
            raise exceptions.AuthenticationFailed('access_token invalid token')
        except KeyError:
            raise exceptions.AuthenticationFailed('access_token invalid key')

        user = User.objects.get(id=decode["user_id"])
        user = UserSerializer(user)

        decode.update(user.data)
        return Response(decode)
