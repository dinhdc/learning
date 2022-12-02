from rest_framework.viewsets import ModelViewSet
from user.api.serializers import (
    UserAddressCreateSerializer,
    UserAddressSerializer,
    UserSerializer
)
from user.models import User, UserAddress
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)
from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer,
    TokenRefreshSerializer
)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ["post", "retrieve"]
    lookup_field = "key"
    module = ["User"]


class UserLoginView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer
    permission_classes = [AllowAny]
    module = ["User"]


class UserRefreshView(TokenRefreshView):
    serializer_class = TokenRefreshSerializer
    module = ["User"]


class UserAddressUpdate(ModelViewSet):
    queryset = UserAddress.objects.all()
    serializer_class = UserAddressSerializer
    module = ["User Address"]
    permission_classes = [IsAuthenticated]
    lookup_field = "key"

    def get_serializer_class(self):
        if self.request.method == "GET":
            return UserAddressSerializer
        elif self.action == "create":
            return UserAddressCreateSerializer

    def get_serializer_context(self):
        return {'user': self.request.user}
