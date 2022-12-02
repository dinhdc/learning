from rest_framework.routers import DefaultRouter
from user.api.api_views import UserLoginView, UserRefreshView, UserViewSet, UserAddressUpdate
from django.urls import path

urlpatterns = [
    path('token/', UserLoginView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', UserRefreshView.as_view(), name='token_refresh'), ]
router = DefaultRouter()
router.register(r'users', UserViewSet, basename="User Controller")
router.register(r'user-address', UserAddressUpdate, basename="User Address")
urlpatterns += router.urls
