from core.exceptions import PermissionDeniedSerializer
from core.utils import ProductsPagination
from drf_spectacular.utils import extend_schema
from providers.models import ProviderModel
from providers.serializers import ProviderSerializer
from rest_framework import generics
from rest_framework import permissions
from rest_framework import status


@extend_schema(
    summary="Call to get all providers",
    responses={
        status.HTTP_200_OK: ProviderSerializer,
        status.HTTP_401_UNAUTHORIZED: PermissionDeniedSerializer,
    },
)
class ProviderView(generics.ListAPIView):
    queryset = ProviderModel.objects.all()
    serializer_class = ProviderSerializer
    pagination_class = ProductsPagination
    permission_classes = (permissions.IsAuthenticated,)
