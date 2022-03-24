from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated

from reviews.permissions import HasOnlyReview

from .serializers import ReviewRecipeSerializer
from .models import ReviewRecipe


class ReviewRecipeList(generics.ListCreateAPIView):
    queryset = ReviewRecipe.objects.filter(is_active=True)
    serializer_class = ReviewRecipeSerializer
    permission_classes = (IsAuthenticated, HasOnlyReview)


class ReviewRecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReviewRecipe.objects.filter(is_active=True)
    serializer_class = ReviewRecipeSerializer
    permission_classes = (IsAuthenticated,)