from categories.models import CategoryModel
from categories.serializers import CategorySerializer
from categories.serializers import DetailCategorySerializer
from core.exceptions import NotFoundSerializer
from core.exceptions import PermissionDeniedSerializer
from core.utils import ProductsPagination
from drf_spectacular.utils import extend_schema
from drf_spectacular.utils import OpenApiParameter
from rest_framework import generics
from rest_framework import permissions
from rest_framework import status


@extend_schema(
    summary="Call to get a list of available categories",
    responses={
        status.HTTP_200_OK: CategorySerializer,
        status.HTTP_401_UNAUTHORIZED: PermissionDeniedSerializer,
    },
)
class CategoriesView(generics.ListAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer
    pagination_class = ProductsPagination
    permission_classes = (permissions.IsAuthenticated,)


@extend_schema(
    summary="Call to get category",
    parameters=[
        OpenApiParameter(
            name="id", required=True, type=int, location=OpenApiParameter.PATH
        ),
    ],
    responses={
        status.HTTP_200_OK: DetailCategorySerializer,
        status.HTTP_401_UNAUTHORIZED: PermissionDeniedSerializer,
        status.HTTP_404_NOT_FOUND: NotFoundSerializer,
    },
)
class CategoryView(generics.RetrieveAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = DetailCategorySerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "id"
