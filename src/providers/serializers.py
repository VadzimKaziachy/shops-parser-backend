from rest_framework import serializers

from providers.models import (
    ProviderModel,
)


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProviderModel
        fields = '__all__'
