from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from product.models import Discount, ProductCategory, Product


class TestCategoryView(TestCase):

    base_url = "http://127.0.0.1:8000/api"
    end_points = {
        "login": "token/",
        "discount": "discounts/",
        "product": "products/"
    }
    api_client = APIClient()

    def setUp(self):
        get_user_model().objects.create_superuser("admin", "123456a@", "admin@gmail.com")
        self.discount = Discount.objects.create(name="category v1", description="category description", percent=10.04)
        self.category = ProductCategory.objects.create(name="category v1", description="category description")
        Product.objects.create(name="Product Test", description="description of product", price="10.04",
                               category=self.category, discount=self.discount)

    def test_get_list_product(self):
        url = "{0}/{1}".format(self.base_url, self.end_points["product"])
        response = self.api_client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(response.data["count"], 0)

    def test_create_product(self):
        login_data = {
            "email": "admin@gmail.com",
            "password": "123456a@"
        }
        user_response = self.api_client.post("{0}/{1}".format(self.base_url, self.end_points["login"]),
                                             data=login_data)
        self.api_client.credentials(HTTP_AUTHORIZATION="Bearer " + user_response.data["access"])
        product = {
            "name": "product v2",
            "description": "lorem abc japan china",
            "price": "20.05",
            "category": self.category.key,
            "discount": self.discount.key
        }
        url = "{0}/{1}".format(self.base_url, self.end_points["product"])
        response = self.api_client.post(url, data=product)
        self.assertEqual(response.status_code, 201)
        self.assertNotEqual(response.data["key"], "")
        self.assertEqual(response.data["name"], product["name"])
        self.assertEqual(response.data["description"], product["description"])
        self.assertEqual(response.data["price"], product["price"])

    def test_update_product(self):
        login_data = {
            "email": "admin@gmail.com",
            "password": "123456a@"
        }
        user_response = self.api_client.post("{0}/{1}".format(self.base_url, self.end_points["login"]),
                                             data=login_data)
        self.api_client.credentials(HTTP_AUTHORIZATION="Bearer " + user_response.data["access"])
        product = Product.objects.all().first()
        new_product = {
            "name": "product updated v2",
            "description": "lorem abc japan china",
            "price": "21.05",
            "category": self.category.key,
            "discount": self.discount.key
        }
        url = "{0}/{1}{2}/".format(self.base_url, self.end_points["product"], product.key)
        response = self.api_client.put(url, data=new_product)
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.data["key"], "")
        self.assertEqual(response.data["name"], new_product["name"])
        self.assertEqual(response.data["description"], new_product["description"])
        self.assertEqual(response.data["price"], new_product["price"])

    def test_update_fail_product_without_description(self):
        login_data = {
            "email": "admin@gmail.com",
            "password": "123456a@"
        }
        user_response = self.api_client.post("{0}/{1}".format(self.base_url, self.end_points["login"]),
                                             data=login_data)
        self.api_client.credentials(HTTP_AUTHORIZATION="Bearer " + user_response.data["access"])
        product = Product.objects.all().first()
        new_product = {
            "description": "lorem abc japan china"
        }
        url = "{0}/{1}{2}/".format(self.base_url, self.end_points["product"], product.key)
        response = self.api_client.put(url, data=new_product)
        self.assertEqual(response.status_code, 400)

    def test_update_success_product_without_required_field(self):
        login_data = {
            "email": "admin@gmail.com",
            "password": "123456a@"
        }
        user_response = self.api_client.post("{0}/{1}".format(self.base_url, self.end_points["login"]),
                                             data=login_data)
        self.api_client.credentials(HTTP_AUTHORIZATION="Bearer " + user_response.data["access"])
        product = Product.objects.all().first()
        new_product = {
            "description": "lorem abc japan china"
        }
        url = "{0}/{1}{2}/".format(self.base_url, self.end_points["product"], product.key)
        response = self.api_client.patch(url, data=new_product)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["description"], new_product["description"])

    def test_delete_product(self):
        login_data = {
            "email": "admin@gmail.com",
            "password": "123456a@"
        }
        user_response = self.api_client.post("{0}/{1}".format(self.base_url, self.end_points["login"]),
                                             data=login_data)
        self.api_client.credentials(HTTP_AUTHORIZATION="Bearer " + user_response.data["access"])
        new_product = {
            "name": "product updated v2",
            "description": "lorem abc japan china",
            "price": "21.05",
            "category": self.category.key,
            "discount": self.discount.key
        }
        url = "{0}/{1}".format(self.base_url, self.end_points["product"])
        self.api_client.post(url, data=new_product)
        last_product = Product.objects.all().last()
        delete_url = "{0}/{1}{2}/".format(self.base_url, self.end_points["product"], last_product.key)
        response = self.api_client.delete(delete_url)
        self.assertEqual(response.status_code, 204)
        self.assertGreaterEqual(Product.objects.all().count(), 0)
        self.api_client.logout()
