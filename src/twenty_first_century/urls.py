from django.urls import path, include

from .views import (
    ScrapyView,
    ProductView,
    ProductsView,
    CategoryView,
    CategoriesView,
    ParserProductView,
)

app_name = 'century'
urlpatterns = [
    path('products/', include(
        [
            path('', ProductsView.as_view()),
            path('<int:pk>', ProductView.as_view()),
            path('<int:pk>/data', ParserProductView.as_view()),
        ]
    )),
    path('categories/', include(
        [
            path('', CategoriesView.as_view()),
            path('<int:pk>', CategoryView.as_view()),
        ]
    )),
    path('<str:job_id>', ScrapyView.as_view()),
]
