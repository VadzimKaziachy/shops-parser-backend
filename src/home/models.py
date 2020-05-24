from django.db import models
from .managers import HomeManager


class HomeModel(models.Model):
    title = models.CharField(verbose_name='Title', max_length=100)
    image = models.ImageField(verbose_name='Background image')
    text_button = models.CharField(verbose_name='Text button', max_length=50)
    description = models.CharField(verbose_name='Description', max_length=200)

    objects = HomeManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Home page'
