from django.contrib import admin
from providers.models import ProviderModel


class ProviderAdmin(admin.ModelAdmin):
    list_display = ("name",)


admin.site.register(ProviderModel, ProviderAdmin)
