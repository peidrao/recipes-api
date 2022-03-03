from rest_framework import serializers
from .models import Tag

class TagSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Tag
        fields = "__all__"