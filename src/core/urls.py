from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from allauth.account.views import ConfirmEmailView

from rest_framework_swagger.views import get_swagger_view

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

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # Swagger
    urlpatterns += [path('swagger-ui/', get_swagger_view(title='Shops-parser-backend API'))]
