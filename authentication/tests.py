
from model_bakery import baker
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from authentication.models import User


class UserViewTest(APITestCase):
    def test_list_users(self):
        user = baker.make(User, is_superuser=True)
        for _ in range(0, 5):
            baker.make(User)
        
        self.client.force_authenticate(user)
        response = self.client.get(reverse('authentication:users-list'), format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 6)

