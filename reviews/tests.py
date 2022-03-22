from rest_framework import status
from django.urls import reverse
from rest_framework.test import APITestCase
from model_bakery import baker

from .models import Recipe, ReviewRecipe
from authentication.models import User


class ReviewRecipeListTest(APITestCase):
    def test_reviewrecipe_list(self):
        user = baker.make(User, is_superuser=True)
        [baker.make(ReviewRecipe, is_active=True) for _ in range(0,10)]
        self.client.force_authenticate(user)
        response = self.client.get(
            reverse('reviews:review_recipes-list'), format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 10)
