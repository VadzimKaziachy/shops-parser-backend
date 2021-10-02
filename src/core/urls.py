from django.conf import settings
from django.contrib import admin
from django.urls import include
from django.urls import path
from drf_spectacular.views import SpectacularAPIView
from drf_spectacular.views import SpectacularSwaggerView

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "api/",
        include(
            [
                path("products/", include("products.urls")),
                path("providers/", include("providers.urls")),
                path("categories/", include("categories.urls")),
                # path('rest-auth/', include(
                #     [
                #         path('registration/', include(
                #             [
                #                 path('account-confirm-email/<str:key>/', ConfirmEmailView.as_view()),
                #                 path('', include('rest_auth.registration.urls')),
                #             ]
                #         )),
                #         path('', include('rest_auth.urls')),
                #     ]
                # )),
                path(
                    "schema/",
                    include(
                        [
                            path(
                                "swagger-ui/",
                                SpectacularSwaggerView.as_view(url_name="schema"),
                                name="swagger-ui",
                            ),
                            path("", SpectacularAPIView.as_view(), name="schema"),
                        ]
                    ),
                ),
            ]
        ),
    ),
    path("", include("home.urls")),
]

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
