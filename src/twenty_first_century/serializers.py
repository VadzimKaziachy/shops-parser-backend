from rest_framework import serializers

from .models import (
    ScrapyModel,
    ProductModel,
    CategoryModel,
    ParserProductModel
)


class ScrapyObjectSerializer(serializers.Serializer):
    code = serializers.CharField(required=True)
    price = serializers.CharField(required=True)
    name = serializers.CharField(required=True)


class ScrapySerializer(serializers.ModelSerializer):
    data = ScrapyObjectSerializer(required=True, many=True)

    class Meta:
        model = ScrapyModel
        fields = ('data',)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ('pk', 'name', 'link')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = ('pk', 'name', 'code')


class ParserProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParserProductModel
        fields = ('pk', 'date', 'price')
