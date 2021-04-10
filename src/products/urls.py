from django.urls import path

from products.views import (
    ProductView,
    ProductsView,
)


urlpatterns = [
    path('<int:id>', ProductView.as_view()),
    path('', ProductsView.as_view()),
]
