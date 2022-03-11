from rest_framework import viewsets, status, generics
from rest_framework.response import Response

from authentication.permissions import IsSuperUser
from .permissions import HasUserPermission
from .serializers import TagSerializer, IngredientSerializer, RecipeSerializer
from .models import Tag, Ingredient, Recipe


class TagListCreateView(generics.ListCreateAPIView):
    queryset = Tag.objects.filter(is_active=True)
    serializer_class = TagSerializer
    permission_classes = (IsSuperUser,)

    def get_queryset(self):
        queryset = self.queryset.filter(user=self.request.user)
        return queryset
        

class TagDetailView(generics.RetrieveUpdateAPIView):
    queryset = Tag.objects.filter(is_active=True)
    serializer_class = TagSerializer
    permission_classes = (HasUserPermission,)

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
        


class IngredientListCreateView(generics.ListCreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = (IsSuperUser,)

    def get_queryset(self):
        queryset = self.queryset.filter(user=self.request.user)
        return queryset
        

class IngredientDetailView(generics.RetrieveUpdateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = (HasUserPermission,)


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

