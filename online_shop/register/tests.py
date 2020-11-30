from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import *
from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate

class AccountTestCase(APITestCase):

    def setUp(self):
        self.create_url = reverse('create')
        Account.objects.create(name='era',
                               last_name='Erjan',
                               username='Erjan',
                               email='zumc4847@gmail.com',
                               password='qwertij')

    def test_account_create(self):
        data = {
            "name":"Erjan",
            "last_name":"Karimov",
            "email":"zuwmc4847@gmail.com",
            "username":"Erjanqwe",
            "password":"qwertij",
            "password2":"qwertij"
        }
        self.response = self.client.post(self.create_url,data)
        self.assertEqual(self.response.status_code,status.HTTP_201_CREATED)

    def test_account_create_empty_username(self):
        data = {
            "name": "Erjan",
            "last_name": "Karimov",
            "email": "zumc4847@gail.com",
            "username": "",
            "password": "qwertij",
            "password2": "qwertij"
        }
        self.response = self.client.post(self.create_url, data)
        self.assertEqual(self.response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_account_empty_email(self):
        data = {
            "name": "Erjan",
            "last_name": "Karimov",
            "email": "",
            "username": "Erjan",
            "password": "qwertij",
            "password2": "qwertij"
        }
        self.response = self.client.post(self.create_url, data)
        self.assertEqual(self.response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_account_empty_password(self):
        data = {
            "name": "Erjan",
            "last_name": "Karimov",
            "email": "zumc4847@gail.com",
            "username": "Erjan",
            "password": "qwertij",
            "password2": "qwertijsdv"
        }
        self.response = self.client.post(self.create_url, data)
        self.assertEqual(self.response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_account_empty_name_and_lastname(self):
        data = {
            "name": "",
            "last_name": "",
            "email": "zumc4847@gail.com",
            "username": "Erjan",
            "password": "qwertij",
            "password2": "qwertijsdv"
        }
        self.response = self.client.post(self.create_url, data)
        self.assertEqual(self.response.status_code, status.HTTP_400_BAD_REQUEST)
        print(self.response.data)

    def test_account_create_username_duplicate(self):
        data = {
            "name": "Erjan",
            "last_name": "Karimov",
            "email": "zumc4847@gail.com",
            "username": "Erjan",
            "password": "qwertij",
            "password2": "qwertij"
        }
        self.response = self.client.post(self.create_url, data)
        self.assertEqual(self.response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_account_create_email_duplicate(self):
        data = {
            "name": "Erjan",
            "last_name": "Karimov",
            "email": "zumc4847@gmail.com",
            "username": "Erjan",
            "password": "qwertij",
            "password2": "qwertij"
        }
        self.response = self.client.post(self.create_url, data)
        self.assertEqual(self.response.status_code, status.HTTP_400_BAD_REQUEST)

class loginTestCase(APITestCase):
    def setUp(self):
        self.login_url = reverse('login')
        Account.objects.create(
                               username='Erjan',
                               password='qwertij')
        self.factory = APIRequestFactory()
        self.request = self.factory.get(self.login_url)

    def test_sign_in(self):
      user = Account.objects.get(username='Erjan')
      force_authenticate(request=self.request,user=user)
      print(self.request.body)