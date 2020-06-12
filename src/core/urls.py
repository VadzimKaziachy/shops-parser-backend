from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from allauth.account.views import ConfirmEmailView

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(
        [
            path('century/', include('twenty_first_century.urls')),
            path('rest-auth/', include(
                [
                    path('registration/', include(
                        [
                            path('account-confirm-email/<str:key>/', ConfirmEmailView.as_view()),
                            path('', include('rest_auth.registration.urls')),
                        ]
                    )),
                    path('', include('rest_auth.urls')),
                ]
            )),
        ]
    )),
    path('', include('home.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static

    schema_view = get_schema_view(
        openapi.Info(
            title="Shops parser API",
            default_version='v1',
            description="API for Shops parser app",
        ),
        public=True,
        permission_classes=(permissions.AllowAny,),
    )

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    urlpatterns += [
        path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    ]

