from rest_framework import status
from rest_framework import generics
from rest_framework import permissions

from drf_spectacular.utils import (
    extend_schema,
)

from core.utils import (
    ProductsPagination,
)
from core.exceptions import (
    PermissionDeniedSerializer,
)

from providers.models import (
    ProviderModel,
)
from providers.serializers import (
    ProviderSerializer,
)


@extend_schema(
    summary='Call to get all providers',
    responses={
        status.HTTP_200_OK: ProviderSerializer,
        status.HTTP_401_UNAUTHORIZED: PermissionDeniedSerializer,
    }
)
class ProviderView(generics.ListAPIView):
    queryset = ProviderModel.objects.all()
    serializer_class = ProviderSerializer
    pagination_class = ProductsPagination
    permission_classes = (permissions.IsAuthenticated,)
