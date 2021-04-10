from django.contrib import admin

from categories.models import (
    CategoryModel,
    ProviderCategoryModel,
)


class ProviderCategoryAdmin(admin.StackedInline):
    model = ProviderCategoryModel
    extra = 0
    min_num = 1
    fieldsets = (
        (None, {
            'fields': (
                'provider',
                'link',
            )
        }),
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = (ProviderCategoryAdmin,)


admin.site.register(CategoryModel, CategoryAdmin)
