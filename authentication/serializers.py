from rest_framework import serializers
from django.contrib.auth.hashers import make_password


from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name',
                  'last_name', 'gender', 'phone', 'birthday')
    
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UserSerializer, self).create(validated_data)
