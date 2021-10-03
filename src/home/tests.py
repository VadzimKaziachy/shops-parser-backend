from django.test import TestCase
from django.urls import reverse
from home.models import HomeModel


class HomeViewTests(TestCase):
    def test_get_queryset(self):
        # HomeModel.objects.create(title=)

        response = self.client.get(reverse("home:home"))

        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.template_name, ["'home/home_page.html'"])
