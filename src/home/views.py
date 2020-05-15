from django.views import generic

from .services.home_service import HomeService


class HomeView(generic.ListView):
    template_name = 'home/home_page.html'
    context_object_name = 'context'

    def get_queryset(self):
        home_service = HomeService()
        return home_service.get_home_page()
