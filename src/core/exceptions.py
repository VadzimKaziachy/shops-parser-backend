from rest_framework import serializers


class NotFoundSerializer(serializers.Serializer):
    detail = serializers.CharField()


class PermissionDeniedSerializer(serializers.Serializer):
    detail = serializers.CharField()
