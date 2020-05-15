from django.db import models
from django.core.validators import MinValueValidator

from django.contrib.postgres.fields import JSONField


class CategoryModel(models.Model):
    name = models.CharField(max_length=255)
    link = models.URLField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('pk',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class ProductModel(models.Model):
    name = models.CharField(max_length=1000)
    code = models.IntegerField(validators=[MinValueValidator(0)])
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('pk', )
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class ParserProductModel(models.Model):
    price = models.FloatField(validators=[MinValueValidator(0)])
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name

    class Meta:
        ordering = ('pk',)
        verbose_name = 'Parser product'
        verbose_name_plural = 'Parser products'


class ScrapyModel(models.Model):
    data = JSONField(blank=True, null=True)
    job_id = models.CharField(max_length=1000)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)

    class Meta:
        ordering = ('pk',)
        verbose_name = 'Scrapy model'
        verbose_name_plural = 'Scrapy models'
