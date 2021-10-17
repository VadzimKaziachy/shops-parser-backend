from django.db import models

from .managers import HomeManager


class HomeModel(models.Model):
    """
    Model for home page.

    Fields:
        1. title - field for saving title for home page;
        2. image - field for loading and saving images for the home page;
        3. text_button - field for saving text button save;
        4. description - field for saving description for home page.
    """

    title = models.CharField(verbose_name="Title", max_length=100)
    image = models.ImageField(verbose_name="Background image")
    text_button = models.CharField(verbose_name="Text button", max_length=50)
    description = models.CharField(verbose_name="Description", max_length=200)

    objects = HomeManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Home page"
