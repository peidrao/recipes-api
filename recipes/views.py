from rest_framework import viewsets, status
from rest_framework.response import Response

from authentication.permissions import IsSuperUser
from .serializers import TagSerializer, IngredientSerializer, RecipeSerializer
from .models import Tag, Ingredient, Recipe


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.filter(is_active=True)
    serializer_class = TagSerializer
    permission_classes = (IsSuperUser,)


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


# class CategoryListView(generics.ListAPIView):
#     queryset = Tag.objects.all()
#     serializer_class = CategorySerializer
