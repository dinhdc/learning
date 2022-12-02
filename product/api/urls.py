from rest_framework.routers import DefaultRouter
from product.api.views import (
    ProductCategoryView, ProductView, DiscountView,
    ProductInventoryView
)

urlpatterns = []

router = DefaultRouter()
router.register(r'categories', ProductCategoryView, basename="Product Category Controller")
router.register(r'products', ProductView, basename="Product Controller")
router.register(r'discounts', DiscountView, basename="Discount Controller")
router.register(r'inventories', ProductInventoryView, basename="Inventory Controller")


urlpatterns += router.urls
