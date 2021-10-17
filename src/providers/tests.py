from django.test import TestCase
from rest_framework import status


class ProviderModelTests(TestCase):
    def test_providers_list_call_401(self) -> None:
        response = self.client.get("/api/products/")

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
