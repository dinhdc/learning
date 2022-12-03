from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from product.models import Discount, ProductCategory, Product, ProductInventory


class TestProductInventoryView(TestCase):
    base_url = "http://127.0.0.1:8000/api"
    end_points = {
        "login": "token/",
        "discount": "discounts/",
        "inventory": "inventories/"
    }
    api_client = APIClient()

    def setUp(self):
        get_user_model().objects.create_superuser("admin", "123456a@", "admin@gmail.com")
        self.discount = Discount.objects.create(name="category v1", description="category description", percent=10.04)
        self.category = ProductCategory.objects.create(name="category v1", description="category description")
        self.product = Product.objects.create(name="Product Test", description="description of product", price="10.04",
                                              category=self.category, discount=self.discount)
        self.inventory = ProductInventory.objects.create(product=self.product, quantity=20)

    def test_update_inventory_for_product(self):
        login_data = {
            "email": "admin@gmail.com",
            "password": "123456a@"
        }
        user_response = self.api_client.post("{0}/{1}".format(self.base_url, self.end_points["login"]),
                                             data=login_data)
        self.api_client.credentials(HTTP_AUTHORIZATION="Bearer " + user_response.data["access"])
        inventory = {
            "product": self.product.key,
            "quantity": 19
        }
        response = self.api_client.put("{0}/{1}{2}/".format(self.base_url, self.end_points["inventory"],
                                                            self.inventory.key), data=inventory)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["quantity"], inventory["quantity"])
        self.assertEqual(response.data["product"], inventory["product"])

    def test_delete_inventory_for_product(self):
        login_data = {
            "email": "admin@gmail.com",
            "password": "123456a@"
        }
        user_response = self.api_client.post("{0}/{1}".format(self.base_url, self.end_points["login"]),
                                             data=login_data)
        self.api_client.credentials(HTTP_AUTHORIZATION="Bearer " + user_response.data["access"])
        response = self.api_client.delete("{0}/{1}{2}/".format(self.base_url, self.end_points["inventory"],
                                                               self.inventory.key))
        self.assertEqual(response.status_code, 204)
