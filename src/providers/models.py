from django.db import models


class ProviderModel(models.Model):
    name = models.CharField(max_length=100, unique=True)

    created = models.DateTimeField(editable=False, auto_now_add=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ("created",)
        verbose_name = "Provider"
        verbose_name_plural = "Providers"
