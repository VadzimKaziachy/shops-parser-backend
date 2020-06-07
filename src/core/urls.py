from django.conf import settings
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include

from allauth.account.views import ConfirmEmailView

from rest_framework_swagger.views import get_swagger_view

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/', include(
        [
            url(r'^century/', include('twenty_first_century.urls')),
            url(r'^rest-auth/', include(
                [
                    url(r'^registration/', include(
                        [
                            url(r'^account-confirm-email/(?P<key>[-:\w]+)/$', ConfirmEmailView.as_view()),
                            url(r'^', include('rest_auth.registration.urls')),
                        ]
                    )),
                    url(r'^', include('rest_auth.urls')),
                ]
            )),
        ]
    )),
    url(r'^', include('home.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # Swagger
    urlpatterns += [url(r'^swagger-ui/$', get_swagger_view(title='Shops-parser-backend API'))]
