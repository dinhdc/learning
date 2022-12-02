from django.test import TestCase
from rest_framework.test import APIClient
from user.models import User


class TestUserAction(TestCase):

    base_url = "http://127.0.0.1:8000/api"
    end_points = {
        "register": "users/",
        "login": "token/",
        "refresh": "token/refresh/"
    }
    api_client = APIClient()
    access = ""
    refresh = ""

    def setUp(self):
        self.refresh = ""
        User.objects.create_superuser("admin", "123456a@", "admin@gmail.com")

    def test_create_normal_user(self):
        data = {
            "username": "congdinh2k",
            "password": "congdinh2k",
            "email": "congdinh2k@gmail.com",
            "first_name": "cong",
            "last_name": "dinh"
        }
        response = self.api_client.post("{0}/{1}".format(self.base_url, self.end_points["register"]),
                                        data=data)
        self.assertEqual(response.status_code, 201)

    def test_create_normal_user_without_name(self):  # create user fail
        data = {
            "username": "congdinh2kv2",
            "password": "congdinh2kv2",
            "email": "congdinh2kv2@gmail.com"
        }
        response = self.api_client.post("{0}/{1}".format(self.base_url, self.end_points["register"]),
                                        data=data)
        self.assertEqual(response.status_code, 400)

    def test_login_with_correct_email_password(self):
        user = User.objects.first()
        data = {
            "password": "123456a@",
            "email": user.email,
        }
        response = self.api_client.post("{0}/{1}".format(self.base_url, self.end_points["login"]),
                                        data=data)
        self.assertEqual(response.status_code, 200)
        self.access = response.data["access"]
        self.refresh = response.data["refresh"]
        self.assertNotEqual(response.data["access"], "")

    def test_login_with_incorrect_email_password(self):
        user = User.objects.first()
        data = {
            "password": "123456a@111",
            "email": user.email,
        }
        response = self.api_client.post("{0}/{1}".format(self.base_url, self.end_points["login"]),
                                        data=data)
        self.assertEqual(response.status_code, 401)

    def test_refresh_token(self):
        user = User.objects.first()
        data = {
            "password": "123456a@",
            "email": user.email,
        }
        response = self.api_client.post("{0}/{1}".format(self.base_url, self.end_points["login"]),
                                        data=data)
        refresh = response.data["refresh"]
        response = self.api_client.post("{0}/{1}".format(self.base_url, self.end_points["refresh"]),
                                        data={"refresh": refresh})
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.data["access"], "")
