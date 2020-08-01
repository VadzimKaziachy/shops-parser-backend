from rest_framework.permissions import (
    IsAuthenticated,
)
from rest_framework.generics import (
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView
)
from core.utils import (
    ProductsPagination,
)
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
    Call for saving data from the parser container. Accept PATCH method.

    Parameter
        1) **job_id** - query parameter, to search for on ScrapyModel by job_id.

    **PATCH** - request for change ScrapyModel.
    """
    queryset = ScrapyModel.objects.all()
    serializer_class = ScrapySerializer
    lookup_field = 'job_id'
    http_method_names = [u'patch']


class CategoriesView(ListAPIView):
    """
    Call for read list CategoryModel. Accept GET method.

    **GET** - request for return a list CategoryModel. Available to authorized users only.
    """
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer
    pagination_class = ProductsPagination
    permission_classes = [IsAuthenticated]


class CategoryView(RetrieveAPIView):
    """
    Call for read CategoryModel. Accept GET method.

    Parameter
        1) **id** - query parameter, to search for an CategoryModel by id.

    **GET** - request for return CategoryModel. Available to authorized users only.
    """
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'


class ProductsView(ListAPIView):
    """
    Call for read list ProductModel. Accept GET method.

    **GET** - request for return a list ProductModel. Available to authorized users only.
    """
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductsPagination
    permission_classes = [IsAuthenticated]


class ProductView(RetrieveAPIView):
    """
    Call for read ProductModel. Accept GET method.

    Parameter
        1) **id** - query parameter, to search for an ProductModel by id.

    **GET** - request for return ProductModel. Available to authorized users only.
    """
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'


class ParserProductView(ListAPIView):
    """
    Call for read list ParserProductModel. Accept GET method.

    Parameter
        1) **id** - query parameter, to search for an ParserProductModel by id.

    **GET** - request for return a list of ParserProductModel.
    """
    queryset = ParserProductModel.objects.all()
    serializer_class = ParserProductSerializer
    pagination_class = ProductsPagination
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
