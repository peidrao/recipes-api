
from random import randint
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
        response = self.client.get(
            reverse('authentication:users-list'), format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 6)

    def test_create_user(self):
        payload = dict(username='profile', email='profile@teste.com', password='@profile',
                       first_name='Profile', last_name='Test', gender='MAN', phone='8499655648',
                       birthday='1999-06-06')

        response = self.client.post(reverse('authentication:users-list'), payload, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['username'], User.objects.last().username)
        self.assertEqual(response.data['email'], User.objects.last().email)
    
    def test_get_user_by_id(self):
        user = baker.make(User, is_superuser=True, username='profile')
        
        response = self.client.get(
            reverse('authentication:users-detail', args=[user.id]), format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], user.username)
        
    def test_delete_user(self):
        user2 = baker.make(User, is_superuser=True, username='profile2')
        response = self.client.delete(
            reverse('authentication:users-detail', args=[user2.id]), format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    def test_delete_user_not_pk(self):
        response = self.client.delete(
            reverse('authentication:users-detail', args=[randint(400, 500)]), format='json')
        
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_put(self):
        user = baker.make(User, is_superuser=True, username='profile', 
            first_name='Profile', last_name='Test')
        
        payload = dict(username='jose', first_name='Jose', last_name='Luis')

        response = self.client.put(
            reverse('authentication:users-detail', args=[user.id]), payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'jose')
        self.assertEqual(response.data['first_name'], 'Jose')
        self.assertEqual(response.data['last_name'], 'Luis')
    
    def test_user_put_not_found(self):
        baker.make(User, is_superuser=True, username='profile', 
            first_name='Profile', last_name='Test')
        
        payload = dict(username='jose', first_name='Jose', last_name='Luis')

        response = self.client.put(
            reverse('authentication:users-detail', args=[randint(100, 200)]), payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    