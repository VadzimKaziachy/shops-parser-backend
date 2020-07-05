from django.db import models
from django.core.validators import MinValueValidator

from django.contrib.postgres.fields import JSONField


class CategoryModel(models.Model):
    """
    Model category.

    Fields:
        1. name - field for saving name category shop;
        2. link - field for saving link category shop.
    """
    name = models.CharField(max_length=255)
    link = models.URLField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('pk',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class ProductModel(models.Model):
    """
    Model product, which have category.

    Fields:
        1. name - field for saving name product;
        2. code - field for saving unique code product;
        3. category - field for saving link on CategoryModel.
    """
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
    """
    Model parser product, product parser saved here.

    Fields:
        1. price - field for saving price parser product;
        2. product - field for saving link on ProductModel;
        3. date - field for saving date create this parser product.
    """
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
    """
    The model for saving data obtained from the application 'shops-parser'.

    Fields:
        1. data - field for saving json data received from 'shops-parser';
        2. job_id - field for saving unique id, which have session in 'shops-parser';
        3. category - field for saving link on CategoryModel.
    """
    data = JSONField(blank=True, null=True)
    job_id = models.CharField(max_length=1000)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)

    class Meta:
        ordering = ('pk',)
        verbose_name = 'Scrapy model'
        verbose_name_plural = 'Scrapy models'
