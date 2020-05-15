from django import forms
from django.contrib import admin
from django.forms.utils import ErrorList

from .models import HomeModel


class HomeModelForm(forms.ModelForm):
    def clean(self):
        if not self.instance.pk and HomeModel.objects.count() > 0:
            self._errors.setdefault('__all__', ErrorList()).append("You can only create one HomeModel object.")
        return self.cleaned_data


class HomeAdmin(admin.ModelAdmin):
    list_display = ('title',)
    form = HomeModelForm


admin.site.register(HomeModel, HomeAdmin)
