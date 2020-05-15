from django.contrib import admin

from .models import CategoryModel, ProductModel, ParserProductModel


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'link')


class ProductAdmin(admin.ModelAdmin):
    list_filter = ('category',)
    list_display = ('name', 'category', 'code')


class ParserProductAdmin(admin.ModelAdmin):
    list_display = ('product', 'price', 'date')


admin.site.register(ProductModel, ProductAdmin)
admin.site.register(CategoryModel, CategoryAdmin)
admin.site.register(ParserProductModel, ParserProductAdmin)
