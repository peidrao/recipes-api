from rest_framework import viewsets, status, generics
from rest_framework.response import Response

from authentication.permissions import IsSuperUser
from .permissions import HasUserPermission
from .serializers import TagSerializer, IngredientSerializer, RecipeSerializer
from .models import Tag, Ingredient, Recipe


class TagListCreateView(generics.ListCreateAPIView):
    queryset = Tag.objects.filter(is_active=True)
    serializer_class = TagSerializer
    permission_classes = (IsSuperUser, HasUserPermission)

class TagDetailView(generics.RetrieveUpdateAPIView):
    queryset = Tag.objects.filter(is_active=True)
    serializer_class = TagSerializer
    permission_classes = (IsSuperUser, HasUserPermission)

    def put(self, request, id):
        try:
            tag = self.queryset.get(id=id)
        except Tag.DoesNotExist:
            return Response("tag not found", status=404)
        serializer = self.serializer_class(tag, many=False)
        return Response(serializer.data, status=200)


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class RecipeCreateView(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class RecipeDetailView(generics.RetrieveUpdateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def get(self, request, id):
        try:
            recipe = self.queryset.get(id=id)
        except Recipe.DoesNotExist:
            return Response("Recipe not found", status=404)

        serializer = self.serializer_class(recipe, many=False)
        return Response(serializer.data, status=200)

# class CategoryListView(generics.ListAPIView):
#     queryset = Tag.objects.all()
#     serializer_class = CategorySerializer
