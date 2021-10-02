from products.models import ProductModel
from products.models import ProviderProductModel
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = "__all__"


class ProviderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProviderProductModel
        fields = "__all__"


class DetailProductSerializer(serializers.ModelSerializer):
    provider_products = ProviderProductSerializer(
        source="providerproductmodel_set", many=True
    )

    class Meta:
        model = ProductModel
        fields = ("id", "category", "created", "provider_products")
