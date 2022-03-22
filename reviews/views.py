from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated

from reviews.permissions import HasOnlyReview

from .serializers import ReviewRecipeSerializer
from .models import ReviewRecipe




# Validações
# O usuário só pode fazer uma avaliação para cada receita


class ReviewRecipeList(generics.ListCreateAPIView):
    queryset = ReviewRecipe.objects.filter(is_active=True)
    serializer_class = ReviewRecipeSerializer
    permission_classes = (IsAuthenticated, HasOnlyReview )
