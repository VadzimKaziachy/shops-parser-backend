from providers.models import ProviderModel
from rest_framework import serializers


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProviderModel
        fields = "__all__"
