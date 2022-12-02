from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from product.models import Discount


class TestCategoryView(TestCase):

    base_url = "http://127.0.0.1:8000/api"
    end_points = {
        "login": "token/",
        "discount": "discounts/"
    }
    api_client = APIClient()

    def setUp(self):
        get_user_model().objects.create_superuser("admin", "123456a@", "admin@gmail.com")
        Discount.objects.create(name="category v1", description="category description", percent=10.04)

    def test_get_list_discount(self):
        url = "{0}/{1}".format(self.base_url, self.end_points["discount"])
        response = self.api_client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(response.data["count"], 0)

    def test_create_discount(self):
        login_data = {
            "email": "admin@gmail.com",
            "password": "123456a@"
        }
        user_response = self.api_client.post("{0}/{1}".format(self.base_url, self.end_points["login"]),
                                             data=login_data)
        self.api_client.credentials(HTTP_AUTHORIZATION="Bearer " + user_response.data["access"])
        discount = {
            "name": "category 1",
            "description": "lorem abc japan china",
            "percent": "20.05"
        }
        url = "{0}/{1}".format(self.base_url, self.end_points["discount"])
        response = self.api_client.post(url, data=discount)
        self.assertEqual(response.status_code, 201)
        self.assertNotEqual(response.data["key"], "")
        self.assertEqual(response.data["name"], discount["name"])
        self.assertEqual(response.data["description"], discount["description"])
        self.assertEqual(response.data["percent"], discount["percent"])

    def test_update_discount(self):
        login_data = {
            "email": "admin@gmail.com",
            "password": "123456a@"
        }
        user_response = self.api_client.post("{0}/{1}".format(self.base_url, self.end_points["login"]),
                                             data=login_data)
        self.api_client.credentials(HTTP_AUTHORIZATION="Bearer " + user_response.data["access"])
        discount = Discount.objects.all().first()
        new_discount = {
            "name": "category 1",
            "description": "lorem abc japan china",
            "percent": "15.43"
        }
        url = "{0}/{1}{2}/".format(self.base_url, self.end_points["discount"], discount.key)
        response = self.api_client.put(url, data=new_discount)
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.data["key"], "")
        self.assertEqual(response.data["name"], new_discount["name"])
        self.assertEqual(response.data["description"], new_discount["description"])
        self.assertEqual(response.data["percent"], new_discount["percent"])

    def test_update_fail_discount_without_description(self):
        login_data = {
            "email": "admin@gmail.com",
            "password": "123456a@"
        }
        user_response = self.api_client.post("{0}/{1}".format(self.base_url, self.end_points["login"]),
                                             data=login_data)
        self.api_client.credentials(HTTP_AUTHORIZATION="Bearer " + user_response.data["access"])
        discount = Discount.objects.all().first()
        new_discount = {
            "description": "lorem abc japan china"
        }
        url = "{0}/{1}{2}/".format(self.base_url, self.end_points["discount"], discount.key)
        response = self.api_client.put(url, data=new_discount)
        self.assertEqual(response.status_code, 400)

    def test_update_success_discount_without_required_field(self):
        login_data = {
            "email": "admin@gmail.com",
            "password": "123456a@"
        }
        user_response = self.api_client.post("{0}/{1}".format(self.base_url, self.end_points["login"]),
                                             data=login_data)
        self.api_client.credentials(HTTP_AUTHORIZATION="Bearer " + user_response.data["access"])
        discount = Discount.objects.all().first()
        new_discount = {
            "description": "lorem abc japan china"
        }
        url = "{0}/{1}{2}/".format(self.base_url, self.end_points["discount"], discount.key)
        response = self.api_client.patch(url, data=new_discount)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["description"], new_discount["description"])

    def test_delete_discount(self):
        login_data = {
            "email": "admin@gmail.com",
            "password": "123456a@"
        }
        user_response = self.api_client.post("{0}/{1}".format(self.base_url, self.end_points["login"]),
                                             data=login_data)
        self.api_client.credentials(HTTP_AUTHORIZATION="Bearer " + user_response.data["access"])
        new_discount = {
            "name": "category 1",
            "description": "lorem abc japan china"
        }
        url = "{0}/{1}".format(self.base_url, self.end_points["discount"])
        self.api_client.post(url, data=new_discount)
        last_discount = Discount.objects.all().last()
        delete_url = "{0}/{1}{2}/".format(self.base_url, self.end_points["discount"], last_discount.key)
        response = self.api_client.delete(delete_url)
        self.assertEqual(response.status_code, 204)
        self.assertGreaterEqual(Discount.objects.all().count(), 0)
        self.api_client.logout()
