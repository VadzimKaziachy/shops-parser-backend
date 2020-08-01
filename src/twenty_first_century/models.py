from django.db import models
from django.core.validators import MinValueValidator

from django.contrib.postgres.fields import JSONField


class CategoryModel(models.Model):
    """
    Category model.

    Fields:
        1) name - field for saving shop category;
        2) link - field for saving link to shop category.
    """
    name = models.CharField(max_length=255)
    link = models.URLField()
    created = models.DateTimeField(editable=False, auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('id',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class ProductModel(models.Model):
    """
    Product model, which has category.

    Fields:
        1) name - field for saving product name;
        2) code - field for saving unique product code;
        3) category - field for saving link to CategoryModel.
    """
    name = models.CharField(max_length=1000)
    code = models.IntegerField(validators=[MinValueValidator(0)])
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    created = models.DateTimeField(editable=False, auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('id', )
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class ParserProductModel(models.Model):
    """
    Parser product model, product parser saved here.

    Fields:
        1) price - field for saving parser product price;
        2) product - field for saving link to ProductModel;
        3) date - field for saving parser product creation date.
    """
    price = models.FloatField(validators=[MinValueValidator(0)])
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name

    class Meta:
        ordering = ('id',)
        verbose_name = 'Parser product'
        verbose_name_plural = 'Parser products'


class ScrapyModel(models.Model):
    """
    This is the model for saving data obtained from the application 'shops-parser'.

    Fields:
        1) data - field for saving json data received from 'shops-parser';
        2) job_id - field for saving unique id, which has session in 'shops-parser';
        3) category - field for saving link to CategoryModel.
    """
    data = JSONField(blank=True, null=True)
    job_id = models.CharField(max_length=1000)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    created = models.DateTimeField(editable=False, auto_now_add=True)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Scrapy model'
        verbose_name_plural = 'Scrapy models'
