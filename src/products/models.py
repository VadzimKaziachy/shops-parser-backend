from django.db import models
from django.core.validators import MinValueValidator


class ProductModel(models.Model):
    name = models.CharField(max_length=1000)
    category = models.ForeignKey("categories.CategoryModel", on_delete=models.CASCADE)
    created = models.DateTimeField(editable=False, auto_now_add=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ('id', )
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class ProviderProductModel(models.Model):
    name = models.CharField(max_length=1000)
    price = models.FloatField(validators=[MinValueValidator(0)])
    code = models.IntegerField(validators=[MinValueValidator(0)])

    product = models.ForeignKey("products.ProductModel", on_delete=models.CASCADE)
    provide = models.ForeignKey("providers.ProviderModel", on_delete=models.CASCADE)

    created = models.DateTimeField(editable=False, auto_now_add=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ('id',)
        verbose_name = 'Provider product'
        verbose_name_plural = 'Provider products'


# Create your models here.
