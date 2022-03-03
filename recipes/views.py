from rest_framework import viewsets

from .serializers import TagSerializer
from .models import Tag


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.filter(is_active=True)
    serializer_class = TagSerializer
