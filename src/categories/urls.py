from categories.views import CategoriesView
from categories.views import CategoryView
from django.urls import path


urlpatterns = [
    path("<int:id>", CategoryView.as_view()),
    path("", CategoriesView.as_view()),
]
