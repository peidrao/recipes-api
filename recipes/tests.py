from random import randint

from model_bakery import baker
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from authentication.models import User
from .models import Ingredient, Tag


class TagListCreateViewTest(APITestCase):
    def test_list_tags(self):
        user = baker.make(User, is_superuser=True)
        for _ in range(0, 5):
            baker.make(Tag, user=user)

        self.client.force_authenticate(user)
        response = self.client.get(reverse('recipes:tags-list'), format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 5)

    def test_create_tag(self):
        user = baker.make(User, is_superuser=True)
        payload = dict(name="new tag", user_id=user.id)

        self.client.force_authenticate(user)
        response = self.client.post(
            reverse('recipes:tags-list'), payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['slug'], Tag.objects.last().slug)

    def test_get_tag(self):
        user = baker.make(User, is_superuser=True)
        tag = baker.make(Tag, user=user, name='New Tag')
        self.client.force_authenticate(user)
        url = reverse('recipes:tags-detail', args=[tag.id])
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['slug'], tag.slug)
        self.assertEqual(response.data['name'], tag.name)

    def test_put_tag_not_found(self):
        user = baker.make(User, is_superuser=True)

        self.client.force_authenticate(user)
        url = reverse('recipes:tags-detail', args=[randint(500, 1000)])
        response = self.client.put(url, {}, format='json')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_put_tag(self):
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

    def test_destroy_tag(self):
        user = baker.make(User, is_superuser=True)
        tag = baker.make(Tag, name='New Tag Destroy',
                         user=user, is_active=True)
        self.client.force_authenticate(user)
        url = reverse('recipes:tags-detail', args=[tag.id])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_destroy_tag_not_found(self):
        user = baker.make(User, is_superuser=True)
        baker.make(Tag, name='New Tag Destroy', user=user)
        self.client.force_authenticate(user)
        url = reverse('recipes:tags-detail', args=[randint(500, 1000)])
        response = self.client.delete(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class IngredientListViewTest(APITestCase):
    def test_list_ingredients(self):
        user = baker.make(User, is_superuser=True)
        for _ in range(0, 10):
            baker.make(Ingredient, user=user, name=f'ingredient_{_}')

        self.client.force_authenticate(user)
        response = self.client.get(
            reverse('recipes:ingredients-list'), format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 10)

    def test_list_empty_ingredients(self):
        user = baker.make(User, is_superuser=True)

        self.client.force_authenticate(user)
        response = self.client.get(
            reverse('recipes:ingredients-list'), format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_create_ingredient(self):
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
