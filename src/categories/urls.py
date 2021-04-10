from django.urls import path

from categories.views import (
    CategoryView,
    CategoriesView
)


urlpatterns = [
    path('<int:id>', CategoryView.as_view()),
    path('', CategoriesView.as_view()),
]
