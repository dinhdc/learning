from rest_framework import serializers
from product.models import ProductCategory, ProductInventory, Product, Discount


class ProductCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCategory
        fields = '__all__'
        extra_kwargs = {
            "created_at": {
                "read_only": True
            }
        }


class DiscountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Discount
        fields = '__all__'
        extra_kwargs = {
            "created_at": {
                "read_only": True
            }
        }


class CategoryRequiredFieldSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCategory
        fields = ('id', 'key', 'name', 'description', )


class DiscountRequiredFieldSerializer(serializers.ModelSerializer):

    class Meta:
        model = Discount
        fields = ('id', 'key', 'name', 'description', 'percent', 'active',)


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'
        extra_kwargs = {
            "created_at": {
                "read_only": True
            }
        }


class ProductGetSerializer(serializers.ModelSerializer):

    category = CategoryRequiredFieldSerializer()
    discount = DiscountRequiredFieldSerializer()

    class Meta:
        model = Product
        fields = '__all__'


class ProductInventorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductInventory
        fields = '__all__'
        extra_kwargs = {
            "created_at": {
                "read_only": True
            }
        }
