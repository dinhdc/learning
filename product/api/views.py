from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.viewsets import ModelViewSet

from product.api.serializers import (
    ProductCategorySerializer, ProductSerializer, ProductGetSerializer,
    DiscountSerializer, ProductInventorySerializer
)
from product.models import ProductCategory, Product, Discount, ProductInventory


class ProductCategoryView(ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    module = ["Product Category"]
    lookup_field = "key"

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        else:
            return [IsAdminUser()]


class DiscountView(ModelViewSet):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer
    module = ["Product Discount"]
    lookup_field = "key"

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        else:
            return [IsAdminUser()]


class ProductView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    module = ["Product Module"]
    lookup_field = "key"
    permission_classes = [IsAdminUser]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ProductGetSerializer
        return self.serializer_class


class ProductInventoryView(ModelViewSet):
    queryset = ProductInventory.objects.all()
    serializer_class = ProductInventorySerializer
    module = ["Product Inventory"]
    lookup_field = "key"
    permission_classes = [IsAdminUser]

