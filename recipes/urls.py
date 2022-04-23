from django.urls import path

from .views import (AllRecipeView, TagListCreateView, TagDetailView, RecipeCreateView,
                    RecipeDetailView, IngredientListCreateView, IngredientDetailView)

app_name = 'recipes'

urlpatterns = [
    path('api/v1/recipes/', RecipeCreateView.as_view(), name='recipes-list'),
    path('api/v1/recipes/<int:pk>', RecipeDetailView.as_view(), name='recipes-detail'),
    path('api/v1/tags/', TagListCreateView.as_view(), name='tags-list'),
    path('api/v1/tags/<int:pk>', TagDetailView.as_view(), name='tags-detail'),
    path('api/v1/ingredients/', IngredientListCreateView.as_view(), name='ingredients-list'),
    path('api/v1/ingredients/<int:pk>', IngredientDetailView.as_view(), name='ingredients-detail'),
    path('api/v1/all_recipes/', AllRecipeView.as_view(), name='all-recipes'),
]
