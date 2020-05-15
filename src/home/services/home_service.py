from django.forms.models import model_to_dict

from ..models import HomeModel


class HomeService:

    def get_home_page(self):
        home_pages = HomeModel.objects.all()
        return model_to_dict(home_pages.first()) if home_pages.exists() else {}
