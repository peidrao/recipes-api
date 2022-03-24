from django.urls import path

from .views import ReviewRecipeDetail, ReviewRecipeList

app_name = 'reviews'

urlpatterns = [
    path('api/v1/review/', ReviewRecipeList.as_view(), name='review_recipes-list'),
    path('api/v1/review/<int:pk>', ReviewRecipeDetail.as_view(), name='review_recipes-detail')
]
