from django.contrib import admin
from products.models import ProductModel
from products.models import ProviderProductModel


class ProviderProductAdmin(admin.StackedInline):
    model = ProviderProductModel
    extra = 0
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    "code",
                    "price",
                    "provide",
                )
            },
        ),
    )


class ProductAdmin(admin.ModelAdmin):
    list_filter = ("category",)
    list_display = (
        "name",
        "category",
    )
    inlines = (ProviderProductAdmin,)


admin.site.register(ProductModel, ProductAdmin)
