from django.db import models


class CategoryModel(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(editable=False, auto_now_add=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ('created',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class ProviderCategoryModel(models.Model):
    link = models.URLField()
    provider = models.ForeignKey("providers.ProviderModel", on_delete=models.CASCADE)
    category = models.ForeignKey("categories.CategoryModel", on_delete=models.CASCADE)

    created = models.DateTimeField(editable=False, auto_now_add=True)

    def __str__(self) -> str:
        return self.provider.name

    class Meta:
        ordering = ('created',)
        verbose_name = "Provider category"
        verbose_name_plural = "Provider categories"
