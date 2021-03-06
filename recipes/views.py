from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from authentication.permissions import IsSuperUser
from .permissions import HasUserPermission
from .serializers import TagSerializer, IngredientSerializer, RecipeSerializer
from .models import Tag, Ingredient, Recipe


class TagListCreateView(generics.ListCreateAPIView):
    queryset = Tag.objects.filter(is_active=True)
    serializer_class = TagSerializer
    permission_classes = (IsSuperUser,)


class TagDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.filter(is_active=True)
    serializer_class = TagSerializer
    permission_classes = (IsAuthenticated,)

    def put(self, request, pk):
        try:
            tag = self.queryset.get(id=pk)
        except Tag.DoesNotExist:
            return Response("tag not found", status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(tag, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            tag = self.queryset.get(id=pk)
        except Tag.DoesNotExist:
            return Response('tag not found', status=status.HTTP_404_NOT_FOUND)

        tag.is_active = False
        tag.save()

        return Response(status=status.HTTP_204_NO_CONTENT)


class IngredientListCreateView(generics.ListCreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = (IsSuperUser,)


class IngredientDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = (IsAuthenticated,)


class RecipeCreateView(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = (IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        queryset = list(self.queryset.filter(user=request.user))
        serializer = self.serializer_class(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class RecipeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def get(self, request, pk):
        try:
            recipe = self.queryset.get(pk=pk)
        except Recipe.DoesNotExist:
            return Response("Recipe not found", status=404)

        serializer = self.serializer_class(recipe, many=False)
        return Response(serializer.data, status=200)


class AllRecipeView(generics.ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
