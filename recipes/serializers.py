from rest_framework import serializers
from .models import Tag

class TagSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    is_active = serializers.BooleanField(read_only=True)

    class Meta:
        model = Tag
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('name', 'slug')

