from django.test import TestCase
from rest_framework.test import APIClient
from user.models import User, UserAddress
from address.models import District, Ward, City


class TestUserAction(TestCase):
    base_url = "http://127.0.0.1:8000/api"
    api_client = APIClient()
    end_points = {
        "list": "user-address/",
        "post": "user-address/",
        "login": "token/",
    }

    def setUp(self):
        self.user = User.objects.create_superuser("admin", "123456a@", "admin@gmail.com")
        city = City.objects.create(name="Vĩnh Phúc", slug="vinh-phuc", type="tinh",
                                   name_with_type="Tỉnh Vĩnh Phúc", code=26)
        district = District.objects.create(name="Tam Dương", slug="tam-duong", type="huyen",
                                           name_with_type="Huyện Tam Dương",
                                           path="Tam Dương, Vĩnh Phúc",
                                           path_with_type="Huyện Tam Dương, Tỉnh Vĩnh Phúc",
                                           code=247, parent_code=city)
        Ward.objects.create(name="Hợp Hòa", slug="hop-hoa", type="thi-tran", name_with_type="Thị trấn Hợp Hòa",
                            path="Hợp Hòa, Tam Dương, Vĩnh Phúc",
                            path_with_type="Thị trấn Hợp Hòa, Huyện Tam Dương, Tỉnh Vĩnh Phúc",
                            code=8869, parent_code=district)

    def test_create_address_without_token(self):
        data = {
            "addressLine": "demo",
            "phone": "021312312",
            "city": City.objects.first().key,
            "district": District.objects.first().key,
            "ward": Ward.objects.first().key
        }
        response = self.api_client.post("{0}/{1}".format(self.base_url, self.end_points["post"]), data=data)
        self.assertNotEqual(response.status_code, 201)

    def test_create_address_with_token(self):
        user = {
            "email": "admin@gmail.com",
            "password": "123456a@"
        }
        user_response = self.api_client.post("{0}/{1}".format(self.base_url, self.end_points["login"]), data=user)
        access = user_response.data["access"]
        self.api_client.credentials(HTTP_AUTHORIZATION="Bearer " + access)
        data = {
            "addressLine": "demo",
            "phone": "021312312",
            "city": City.objects.first().key,
            "district": District.objects.first().key,
            "ward": Ward.objects.first().key
        }
        response = self.api_client.post("{0}/{1}".format(self.base_url, self.end_points["post"]), data=data)
        self.assertEqual(response.status_code, 201)
        address = UserAddress.objects.all().filter(user=self.user).last()
        self.assertEqual(response.data['id'], address.id)
        self.assertEqual(response.data['city'], address.city.key)
        self.api_client.logout()
