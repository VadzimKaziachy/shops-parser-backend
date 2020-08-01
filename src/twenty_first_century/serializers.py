from rest_framework import serializers

from .models import (
    ScrapyModel,
    ProductModel,
    CategoryModel,
    ParserProductModel
)


class ScrapyObjectSerializer(serializers.Serializer):
    """
    Serializer which check object in list `data`. Use only in ScrapySerializer.
    """
    code = serializers.CharField(required=True)
    price = serializers.CharField(required=True)
    name = serializers.CharField(required=True)


class ScrapySerializer(serializers.ModelSerializer):
    """
    Serializer for check `data` from ScrapyMode, after save started celery task. Use only in ScrapyView.
    """
    data = ScrapyObjectSerializer(required=True, many=True)

    class Meta:
        model = ScrapyModel
        fields = ('data',)


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for CategoryModel. Use in CategoriesView and CategoryView.
    """

    class Meta:
        model = CategoryModel
        fields = ('id', 'name', 'link')


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for ProductModel. Use in ProductsView and ProductView.
    """

    class Meta:
        model = ProductModel
        fields = ('id', 'name', 'code')


class ParserProductSerializer(serializers.ModelSerializer):
    """
    Serializer for ParserProductModel. Use only in ParserProductView.
    """

    class Meta:
        model = ParserProductModel
        fields = ('id', 'created', 'price')
