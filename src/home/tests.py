from django.urls import reverse
from django.test import TestCase


class HomeViewTests(TestCase):
    """
    Class which testing HomeView.
    """

    def test_get_queryset(self):
        """
        Test for check work HomeView.
        """
        response = self.client.get(reverse('home:home'))

        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.template_name, ["'home/home_page.html'"])
