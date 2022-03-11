from django.urls import path

from .views import (TagListCreateView, TagDetailView, RecipeCreateView,
                    RecipeDetailView, IngredientListCreateView, IngredientDetailView)

app_name = 'recipes'

urlpatterns = [
    path('api/v1/recipes/', RecipeCreateView.as_view()),
    path('api/v1/recipes/<int:id>', RecipeDetailView.as_view()),
    path('api/v1/tags/', TagListCreateView.as_view(), name='tags-list'),
    path('api/v1/tags/<int:pk>', TagDetailView.as_view(), name='tags-detail'),
    path('api/v1/ingredients/', IngredientListCreateView.as_view()),
    path('api/v1/ingredients/<int:pk>', IngredientDetailView.as_view()),
]
