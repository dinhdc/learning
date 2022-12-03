from rest_framework import serializers
from user.models import User, UserAddress


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ('id', 'groups', 'user_permissions',)
        depth = 1
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            },
            'last_login': {
                'read_only': True
            },
            'is_superuser': {
                'read_only': True
            },
            'is_staff': {
                'read_only': True
            },
            'is_active': {
                'read_only': True
            },
            'date_joined': {
                'read_only': True
            },

        }

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        password = validated_data["password"]
        user.set_password(password)
        user.save()
        return user


class UserAddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserAddress
        depth = 1
        exclude = ("user",)


class UserAddressCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserAddress
        exclude = ("created_at", "user", )

    def create(self, validated_data):
        user = self.context["user"]
        validated_data["user"] = user
        user_address = UserAddress.objects.create(**validated_data)
        user_address.save()
        return user_address

    def update(self, instance, validated_data):
        instance = super(UserAddressCreateSerializer, self).update(instance, validated_data)
        user = self.context["user"]
        instance.user = user
        instance.save()
        return instance
