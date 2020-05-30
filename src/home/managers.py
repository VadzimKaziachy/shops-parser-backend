from django.db import models

from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404


class HomeManager(models.Manager):
    """
    Manager for HomeModel.
    """
    def get_first_object_to_dict(self):
        return model_to_dict(get_object_or_404(self.get_queryset()))
