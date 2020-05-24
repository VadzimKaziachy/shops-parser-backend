from django.views import generic

from .models import HomeModel


class HomeView(generic.TemplateView):
    template_name = 'home/home_page.html'

    def get_context_data(self, **kwargs):
        return HomeModel.objects.get_first_model_to_dict()
