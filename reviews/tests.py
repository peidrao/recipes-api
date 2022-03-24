from random import randint
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

    def test_reviewrecipe_create(self):
        user = baker.make(User, is_superuser=True)
        recipe = baker.make(Recipe)
        payload = dict(user=user.id, recipe=recipe.id, rate=5, comment='Best')
        self.client.force_authenticate(user)
        response = self.client.post(reverse('reviews:review_recipes-list'), payload, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['rate'], ReviewRecipe.objects.last().rate)
        self.assertEqual(response.data['comment'], ReviewRecipe.objects.last().comment)
    
    def test_reviewrecipe_dont_rate_same_recipe(self):
        user = baker.make(User, is_superuser=True)
        recipe = baker.make(Recipe)
        baker.make(ReviewRecipe, recipe_id=recipe.id, user_id=user.id)
        payload = dict(user=user.id, recipe=recipe.id, rate=5, comment='Best')
        self.client.force_authenticate(user)
        response = self.client.post(reverse('reviews:review_recipes-list'), payload, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data['detail'].title(), 'You Can Only Rate A Recipe Once')
        

class ReviewRecipeDetailTest(APITestCase):
    def test_reviewrecipe_get_by_id(self):
        user = baker.make(User, is_superuser=True)
        review = baker.make(ReviewRecipe, is_active=True)
        self.client.force_authenticate(user)
        response = self.client.get(
            reverse('reviews:review_recipes-detail', args=[review.id]), format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_reviewrecipe_get_by_id_not_found(self):
        user = baker.make(User, is_superuser=True)
        self.client.force_authenticate(user)
        response = self.client.get(
            reverse('reviews:review_recipes-detail', args=[randint(500, 1000)]), format='json')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_reviewrecipe_delete(self):
        user = baker.make(User, is_superuser=True)
        review = baker.make(ReviewRecipe, is_active=True)
        self.client.force_authenticate(user)
        response = self.client.delete(
            reverse('reviews:review_recipes-detail', args=[review.id]), format='json')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
    def test_reviewrecipe_delete_not_found(self):
        user = baker.make(User, is_superuser=True)
        
        self.client.force_authenticate(user)
        response = self.client.delete(
            reverse('reviews:review_recipes-detail', args=[randint(500, 1000)]), format='json')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)