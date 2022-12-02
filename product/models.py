from django.db import models
from core.models import BaseModel


class ProductCategory(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class Discount(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    percent = models.DecimalField(max_digits=6, decimal_places=2)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Product(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    category = models.ForeignKey(ProductCategory, to_field="key", on_delete=models.CASCADE)
    discount = models.ForeignKey(Discount, to_field="key", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ProductInventory(BaseModel):
    quantity = models.IntegerField(default=0)
    product = models.OneToOneField(Product, to_field="key", on_delete=models.CASCADE)
