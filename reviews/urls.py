from django.urls import path

from .views import ReviewRecipeList

app_name = 'reviews'

urlpatterns = [
    path('api/v1/review/recipes/', ReviewRecipeList.as_view(), name='review_recipes-list')
]
