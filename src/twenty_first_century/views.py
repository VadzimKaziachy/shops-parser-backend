from rest_framework.generics import (
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView
)

from core.utils import ProductsPagination
from .models import (
    ScrapyModel,
    ProductModel,
    CategoryModel,
    ParserProductModel
)
from .serializers import (
    ScrapySerializer,
    ProductSerializer,
    CategorySerializer,
    ParserProductSerializer
)


class ScrapyView(UpdateAPIView):
    queryset = ScrapyModel.objects.all()
    serializer_class = ScrapySerializer
    lookup_field = 'job_id'
    http_method_names = [u'patch']


class CategoriesView(ListAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer
    pagination_class = ProductsPagination


class CategoryView(RetrieveAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer


class ProductsView(ListAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductsPagination


class ProductView(RetrieveAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer


class ParserProductView(ListAPIView):
    queryset = ParserProductModel.objects.all()
    serializer_class = ParserProductSerializer
    pagination_class = ProductsPagination
