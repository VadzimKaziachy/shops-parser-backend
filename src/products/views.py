from core.exceptions import NotFoundSerializer
from core.exceptions import PermissionDeniedSerializer
from core.utils import ProductsPagination
from drf_spectacular.utils import extend_schema
from drf_spectacular.utils import OpenApiParameter
from products.models import ProductModel
from products.serializers import DetailProductSerializer
from products.serializers import ProductSerializer
from rest_framework import generics
from rest_framework import permissions
from rest_framework import status


@extend_schema(
    summary="Call to get all products",
    responses={
        status.HTTP_200_OK: ProductSerializer,
        status.HTTP_401_UNAUTHORIZED: PermissionDeniedSerializer,
    },
)
class ProductsView(generics.ListAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductsPagination
    permission_classes = (permissions.IsAuthenticated,)


@extend_schema(
    summary="Call to get product",
    parameters=[
        OpenApiParameter(
            name="id", required=True, type=int, location=OpenApiParameter.PATH
        ),
    ],
    responses={
        status.HTTP_200_OK: DetailProductSerializer,
        status.HTTP_401_UNAUTHORIZED: PermissionDeniedSerializer,
        status.HTTP_404_NOT_FOUND: NotFoundSerializer,
    },
)
class ProductView(generics.RetrieveAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = DetailProductSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "id"
