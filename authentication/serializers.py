from rest_framework import serializers
from django.contrib.auth.hashers import make_password


from .models import User


class UserSerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(read_only=True)
    is_staff = serializers.BooleanField(read_only=True)
    is_superuser = serializers.BooleanField(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name',
                  'last_name', 'gender', 'phone', 'birthday', 'is_active', 'is_staff', 'is_superuser')

    def create(self, validated_data):
        validated_data['password'] = make_password(
            validated_data.get('password'))
        return super(UserSerializer, self).create(validated_data)
    
    def update(self, instance, validated_data):
        validated_data['password'] = make_password(
            validated_data.get('password'))
        return super().update(instance, validated_data)


class ChangePasswordSerializer(serializers.Serializer):
    model = User
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)