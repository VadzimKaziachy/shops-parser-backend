from django import forms
from django.contrib import admin
from django.forms.utils import ErrorList

from .models import HomeModel


class HomeModelForm(forms.ModelForm):
    def clean(self):
        """
        It can save only one object.
        :raise: If have more one object, will be return `None`.
        :return: Dict with object fields.
        """
        if not self.instance.pk and HomeModel.objects.count() > 0:
            self._errors.setdefault('__all__', ErrorList()).append("You can only create one HomeModel object.")
        return self.cleaned_data


class HomeAdmin(admin.ModelAdmin):
    """
    Class for filling the home page in the admin panel.
    """
    list_display = ('title',)
    form = HomeModelForm


admin.site.register(HomeModel, HomeAdmin)
