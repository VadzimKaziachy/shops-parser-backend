from django.views import generic

from .models import HomeModel


class HomeView(generic.TemplateView):
    """
    Render a template for home page.
    """
    template_name = 'home/home_page.html'

    def get_context_data(self, **kwargs):
        return HomeModel.objects.get_first_object_to_dict()
