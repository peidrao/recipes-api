from rest_framework import viewsets, generics
from rest_framework.response import Response 

from .serializers import CategorySerializer, TagSerializer
from .models import Tag


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.filter(is_active=True)
    serializer_class = TagSerializer


class CategoryListView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = CategorySerializer

    # def list(self, request, *args, **kwargs):
    #     queryset = self.filter_queryset(self.get_queryset())

    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)