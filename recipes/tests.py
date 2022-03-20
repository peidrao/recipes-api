from random import randint

from model_bakery import baker
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from authentication.models import User
from .models import Ingredient, Recipe, Tag


class TagListCreateViewTest(APITestCase):
    def test_tags_list(self):
        user = baker.make(User, is_superuser=True)
        for _ in range(0, 5):
            baker.make(Tag, user=user)

        self.client.force_authenticate(user)
        response = self.client.get(reverse('recipes:tags-list'), format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 5)

    def test_tag_create(self):
        user = baker.make(User, is_superuser=True)
        payload = dict(name="new tag", user_id=user.id)

        self.client.force_authenticate(user)
        response = self.client.post(
            reverse('recipes:tags-list'), payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['slug'], Tag.objects.last().slug)

    def test_tag_get_by_id(self):
        user = baker.make(User, is_superuser=True)
        tag = baker.make(Tag, user=user, name='New Tag')
        self.client.force_authenticate(user)
        url = reverse('recipes:tags-detail', args=[tag.id])
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['slug'], tag.slug)
        self.assertEqual(response.data['name'], tag.name)

    def test_tag_put_not_found(self):
        user = baker.make(User, is_superuser=True)

        self.client.force_authenticate(user)
        url = reverse('recipes:tags-detail', args=[randint(500, 1000)])
        
        response = self.client.put(url, {}, format='json')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_tag_put(self):
        user = baker.make(User, is_superuser=True)
        tag = baker.make(Tag, name='New Tag', user=user)
        payload = dict(name='New Tag 2')
        self.client.force_authenticate(user)
        url = reverse('recipes:tags-detail', args=[tag.id])
        response = self.client.put(url, payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], Tag.objects.last().id)
        self.assertEqual(response.data['name'], Tag.objects.last().name)
        self.assertEqual(response.data['slug'], Tag.objects.last().slug)

    def test_tag_destroy(self):
        user = baker.make(User, is_superuser=True)
        tag = baker.make(Tag, name='New Tag Destroy',
                         user=user, is_active=True)
        self.client.force_authenticate(user)
        url = reverse('recipes:tags-detail', args=[tag.id])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_tag_destroy_not_found(self):
        user = baker.make(User, is_superuser=True)
        baker.make(Tag, name='New Tag Destroy', user=user)
        self.client.force_authenticate(user)
        url = reverse('recipes:tags-detail', args=[randint(500, 1000)])
        response = self.client.delete(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class IngredientListViewTest(APITestCase):
    def test_ingredient_list(self):
        user = baker.make(User, is_superuser=True)
        for _ in range(0, 10):
            baker.make(Ingredient, user=user, name=f'ingredient_{_}')

        self.client.force_authenticate(user)
        response = self.client.get(
            reverse('recipes:ingredients-list'), format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 10)

    def test_ingredient_list_empty(self):
        user = baker.make(User, is_superuser=True)

        self.client.force_authenticate(user)
        response = self.client.get(
            reverse('recipes:ingredients-list'), format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_ingredient_create(self):
        user = baker.make(User, is_superuser=True)

        payload = dict(user_id=user.id, name='Ingredient 1')

        self.client.force_authenticate(user)
        response = self.client.post(
            reverse('recipes:ingredients-list'), data=payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class IngredientDetailViewTest(APITestCase):
    def test_ingredient_get_by_id(self):
        user = baker.make(User, is_superuser=True)

        ingredient = baker.make(Ingredient, user=user, name='Potato')

        self.client.force_authenticate(user)
        response = self.client.get(
            reverse('recipes:ingredients-detail', args=[ingredient.id]), format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], ingredient.name)
        self.assertEqual(response.data['user'], ingredient.user.id)

    def test_ingredient_get_by_id_not_found(self):
        user = baker.make(User, is_superuser=True)

        self.client.force_authenticate(user)
        response = self.client.get(
            reverse('recipes:ingredients-detail', args=[randint(1000, 1500)]), format='json')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_ingredient_update(self):
        user = baker.make(User, is_superuser=True)
        ingredient = baker.make(Ingredient, user=user, name='Potato')
        payload = dict(name='Orange')
        self.client.force_authenticate(user)
        response = self.client.put(
            reverse('recipes:ingredients-detail', args=[ingredient.id]), payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Orange')
    
    def test_ingredient_update_user_different(self):
        user = baker.make(User, is_superuser=True)
        user2 = baker.make(User, is_superuser=True)

        ingredient = baker.make(Ingredient, user=user, name='Potato')
        payload = dict(name='Orange')
        self.client.force_authenticate(user2)
        response = self.client.put(
            reverse('recipes:ingredients-detail', args=[ingredient.id]), payload, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_ingredient_destroy(self):
        user = baker.make(User, is_superuser=True)

        ingredient = baker.make(Ingredient, user=user, name='Potato')
        
        self.client.force_authenticate(user)
        response = self.client.delete(
            reverse('recipes:ingredients-detail', args=[ingredient.id]), format='json')
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    def test_ingredient_destroy(self):
        user = baker.make(User, is_superuser=True)
        
        self.client.force_authenticate(user)
        response = self.client.delete(
            reverse('recipes:ingredients-detail', args=[randint(1000, 2000)]), format='json')
        
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    

class RecipeCreateViewTest(APITestCase):
    def test_recipe_list(self):
        user = baker.make(User, is_superuser=True)
        
        for _ in range(0, 10):
            baker.make(Recipe, title='Fries{_}', user=user, time_minutes=10)

        self.client.force_authenticate(user)
        response = self.client.get(
            reverse('recipes:recipes-list'), format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 10)

    def test_recipe_list_empty(self):
        user = baker.make(User, is_superuser=True)

        self.client.force_authenticate(user)
        response = self.client.get(
            reverse('recipes:ingredients-list'), format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_create_recipe(self):
        user = baker.make(User, is_superuser=True)
        tag1 = baker.make(Tag, name='juice', user=user)
        tag2 = baker.make(Tag, name='pizza', user=user)

        ingredient = baker.make(Ingredient, user=user, name='tomato')
        ingredient2 = baker.make(Ingredient, user=user, name='cheese')
        ingredient3 = baker.make(Ingredient, user=user, name='ham')
        ingredient4 = baker.make(Ingredient, user=user, name='chicken')
            
        payload = dict(user_id=user.id, title='Chicken Pizza', time_minutes=30, price=60.99, 
                        ingredients=[ingredient.id, ingredient2.id, ingredient3.id, ingredient4.id],
                        tags=[tag1.id, tag2.id])

        self.client.force_authenticate(user)
        response = self.client.post(
            reverse('recipes:recipes-list'), data=payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'Chicken Pizza')
        self.assertEqual(response.data['price'], '60.99')


class RecipeDetailViewTest(APITestCase):
    def test_recipe_get(self):
        user = baker.make(User, is_superuser=True)
        recipe = baker.make(Recipe, title='Recipe#1')

        self.client.force_authenticate(user)
        response = self.client.get(
            reverse('recipes:recipes-detail', args=[recipe.id]), format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], recipe.title)
    
    def test_recipe_get_not_found(self):
        user = baker.make(User, is_superuser=True)

        self.client.force_authenticate(user)
        response = self.client.get(
            reverse('recipes:recipes-detail', args=[randint(0, 0)]), format='json')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, 'Recipe not found')
    
    def test_recipe_destroy(self):
        user = baker.make(User, is_superuser=True)
        recipe = baker.make(Recipe, title='Recipe#2')

        self.client.force_authenticate(user)
        response = self.client.delete(
            reverse('recipes:recipes-detail', args=[recipe.id]), format='json')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    def test_recipe_destroy_not_found(self):
        user = baker.make(User, is_superuser=True)

        self.client.force_authenticate(user)
        response = self.client.delete(
            reverse('recipes:recipes-detail', args=[randint(0,0)]), format='json')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_recipe_update(self):
        user = baker.make(User, is_superuser=True)
        recipe = baker.make(Recipe, user=user, title='Recipe#3', time_minutes=50)
        payload = dict(title='Special Recipe', time_minutes=40, price=59.95)
        self.client.force_authenticate(user)
        response = self.client.put(
            reverse('recipes:recipes-detail', args=[recipe.id]), payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Special Recipe')
        self.assertEqual(response.data['time_minutes'], 40)
    
    def test_recipe_update_not_found(self):
        user = baker.make(User, is_superuser=True)
        
        payload = dict(title='Special Recipe', time_minutes=40, price=59.95)
        self.client.force_authenticate(user)
        response = self.client.put(
            reverse('recipes:recipes-detail', args=[randint(0,0)]), payload, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
