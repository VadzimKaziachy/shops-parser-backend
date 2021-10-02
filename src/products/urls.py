from django.urls import path
from products.views import ProductsView
from products.views import ProductView


urlpatterns = [
    path("<int:id>", ProductView.as_view()),
    path("", ProductsView.as_view()),
]
