
from model_bakery import baker
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from authentication.models import User
from .models import Tag

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
        response = self.client.post(reverse('recipes:tags-list'), payload, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['slug'], Tag.objects.last().slug)
