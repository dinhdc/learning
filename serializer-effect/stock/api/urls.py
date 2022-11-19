from rest_framework.routers import DefaultRouter
from stock.api import views

router = DefaultRouter()
urlpatterns = []

router.register(r'stock-codes', views.StockCodeViewSet, basename="Stok Code")
router.register(r'stock-prices', views.StockPerDayViewSet, basename="Stok Price")
urlpatterns += router.urls
