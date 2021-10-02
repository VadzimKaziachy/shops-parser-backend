from categories.models import CategoryModel
from categories.models import ProviderCategoryModel
from rest_framework import serializers


class ProviderCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProviderCategoryModel
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = "__all__"


class DetailCategorySerializer(serializers.ModelSerializer):
    categories = ProviderCategorySerializer(
        source="providercategorymodel_set", many=True
    )

    class Meta:
        model = CategoryModel
        fields = ("id", "name", "categories")
