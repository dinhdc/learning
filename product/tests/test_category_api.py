from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from product.models import ProductCategory


class TestCategoryView(TestCase):

    base_url = "http://127.0.0.1:8000/api"
    end_points = {
        "login": "token/",
        "category": "categories/"
    }
    api_client = APIClient()

    def setUp(self):
        get_user_model().objects.create_superuser("admin", "123456a@", "admin@gmail.com")
        ProductCategory.objects.create(name="category v1", description="category description")

    def test_get_list_category(self):
        url = "{0}/{1}".format(self.base_url, self.end_points["category"])
        response = self.api_client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(response.data["count"], 0)

    def test_create_category(self):
        login_data = {
            "email": "admin@gmail.com",
            "password": "123456a@"
        }
        user_response = self.api_client.post("{0}/{1}".format(self.base_url, self.end_points["login"]),
                                             data=login_data)
        self.api_client.credentials(HTTP_AUTHORIZATION="Bearer " + user_response.data["access"])
        new_category = {
            "name": "category 1",
            "description": "lorem abc japan china"
        }
        url = "{0}/{1}".format(self.base_url, self.end_points["category"])
        response = self.api_client.post(url, data=new_category)
        self.assertEqual(response.status_code, 201)
        self.assertNotEqual(response.data["key"], "")
        self.assertEqual(response.data["name"], new_category["name"])
        self.assertEqual(response.data["description"], new_category["description"])

    def test_update_category(self):
        login_data = {
            "email": "admin@gmail.com",
            "password": "123456a@"
        }
        user_response = self.api_client.post("{0}/{1}".format(self.base_url, self.end_points["login"]),
                                             data=login_data)
        self.api_client.credentials(HTTP_AUTHORIZATION="Bearer " + user_response.data["access"])
        category = ProductCategory.objects.all().first()
        new_category = {
            "name": "category 1",
            "description": "lorem abc japan china"
        }
        url = "{0}/{1}{2}/".format(self.base_url, self.end_points["category"], category.key)
        response = self.api_client.put(url, data=new_category)
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.data["key"], "")
        self.assertEqual(response.data["name"], new_category["name"])
        self.assertEqual(response.data["description"], new_category["description"])

    def test_update_fail_category_without_description(self):
        login_data = {
            "email": "admin@gmail.com",
            "password": "123456a@"
        }
        user_response = self.api_client.post("{0}/{1}".format(self.base_url, self.end_points["login"]),
                                             data=login_data)
        self.api_client.credentials(HTTP_AUTHORIZATION="Bearer " + user_response.data["access"])
        category = ProductCategory.objects.all().first()
        new_category = {
            "description": "lorem abc japan china"
        }
        url = "{0}/{1}{2}/".format(self.base_url, self.end_points["category"], category.key)
        response = self.api_client.put(url, data=new_category)
        self.assertEqual(response.status_code, 400)

    def test_update_success_category_without_description(self):
        login_data = {
            "email": "admin@gmail.com",
            "password": "123456a@"
        }
        user_response = self.api_client.post("{0}/{1}".format(self.base_url, self.end_points["login"]),
                                             data=login_data)
        self.api_client.credentials(HTTP_AUTHORIZATION="Bearer " + user_response.data["access"])
        category = ProductCategory.objects.all().first()
        new_category = {
            "description": "lorem abc japan china"
        }
        url = "{0}/{1}{2}/".format(self.base_url, self.end_points["category"], category.key)
        response = self.api_client.patch(url, data=new_category)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["description"], new_category["description"])

    def test_delete_category(self):
        login_data = {
            "email": "admin@gmail.com",
            "password": "123456a@"
        }
        user_response = self.api_client.post("{0}/{1}".format(self.base_url, self.end_points["login"]),
                                             data=login_data)
        self.api_client.credentials(HTTP_AUTHORIZATION="Bearer " + user_response.data["access"])
        new_category = {
            "name": "category 1",
            "description": "lorem abc japan china"
        }
        url = "{0}/{1}".format(self.base_url, self.end_points["category"])
        self.api_client.post(url, data=new_category)
        last_category = ProductCategory.objects.all().last()
        delete_url = "{0}/{1}{2}/".format(self.base_url, self.end_points["category"], last_category.key)
        response = self.api_client.delete(delete_url)
        self.assertEqual(response.status_code, 204)
        self.assertGreaterEqual(ProductCategory.objects.all().count(), 0)
        self.api_client.logout()
