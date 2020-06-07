from rest_framework.permissions import IsAuthenticated
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
    """
    Class for saving data from the parser container.
    """
    queryset = ScrapyModel.objects.all()
    serializer_class = ScrapySerializer
    lookup_field = 'job_id'
    http_method_names = [u'patch']


class CategoriesView(ListAPIView):
    """
    Class that return a list of categories.
    """
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer
    pagination_class = ProductsPagination
    permission_classes = [IsAuthenticated]


class CategoryView(RetrieveAPIView):
    """
    Class that return categories by pk.
    """
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]


class ProductsView(ListAPIView):
    """
    Class that return a list of products.
    """
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductsPagination
    permission_classes = [IsAuthenticated]


class ProductView(RetrieveAPIView):
    """
    Class that return product by pk.
    """
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


class ParserProductView(ListAPIView):
    """
    Class that return a list parser product.
    """
    queryset = ParserProductModel.objects.all()
    serializer_class = ParserProductSerializer
    pagination_class = ProductsPagination
    permission_classes = [IsAuthenticated]
