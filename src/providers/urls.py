from django.urls import path
from providers.views import ProviderView

urlpatterns = [path("", ProviderView.as_view())]
