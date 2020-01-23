from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

from rest_app.models import FancyCat

class ListApiTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('fancy-cats-list')
    
        FancyCat.objects.create(name="Alex", age=2)
        FancyCat.objects.create(name="Oscar", age=1)
    
    # def test_get_method(self):
    #     response = self.client.get(self.url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(response.data, [
    #         {'id': 1, 'name': 'Alex'},
    #         {'id': 2, 'name': 'Oscar'}
    #     ])
    
    def test_post_method(self):
        data = {'name': 'Mary'}
        user = User.objects.create_superuser(username="admin", password="adminadmin", email="admin@example.com")
        self.client.force_login(user)
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['id'], 3)
        self.assertEqual(response.data['name'], 'Mary')
        self.assertEqual(FancyCat.objects.count(), 3)
    
    def test_not_authenticated(self):
        data = {'name': 'Mary'}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_bad_request(self):
        data = {}
        user = User.objects.create_superuser(username="admin", password="adminadmin", email="admin@example.com")
        self.client.force_login(user)
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
class DetailApiTest(APITestCase):
    
    def setUp(self):
        self.cat = FancyCat.objects.create(name="Alex", age=2)
        self.client = Client()
        self.url = reverse('fancy-cats-detail', args=(self.cat.id, ))
       
    def test_get_auth(self):
        user = User.objects.create_superuser(username="admin", password="adminadmin", email="admin@example.com")
        self.client.force_login(user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], 1)
        self.assertEqual(response.data['name'], "Alex")
    
    def test_get_not_auth(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_put_auth(self):
        data = self.cat.name
        print(type(data))
        user = User.objects.create_superuser(username="admin", password="adminadmin", email="admin@example.com")
        self.client.force_login(user)
        response = self.client.put(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_put_not_auth(self):
        data = {'name': 'Hi'}
        response = self.client.put(self.url, data=data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_del_auth(self):
        user = User.objects.create_superuser(username="admin", password="adminadmin", email="admin@example.com")
        self.client.force_login(user)
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    def test_del_not_auth(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)



    


    


