from django.contrib import admin
from product.models import ProductCategory, ProductInventory, Product, Discount

admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(ProductInventory)
admin.site.register(Discount)
