from rest_framework.routers import DefaultRouter
from app.api.views import RuleViewSet

urlpatterns = []
router = DefaultRouter()
router.register(r'rules', RuleViewSet, basename="rule")
urlpatterns += router.urls
