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
            path('<int:id>/', include(
                [
                    path('data', ParserProductView.as_view()),
                    path('', ProductView.as_view()),
                ]
            )),
            path('', ProductsView.as_view()),
        ]
    )),
    path('categories/', include(
        [
            path('<int:id>', CategoryView.as_view()),
            path('', CategoriesView.as_view()),
        ]
    )),
    path('<str:job_id>', ScrapyView.as_view()),
]
