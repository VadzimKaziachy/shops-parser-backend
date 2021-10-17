# Generated by Django 3.2.7 on 2021-10-03 09:39
from django.db import migrations
from providers.constants import ProviderEnum


def create_providers(app, schema_editor):
    ProviderModel = app.get_model(app_label="providers", model_name="ProviderModel")

    ProviderModel.objects.bulk_create(
        [
            ProviderModel(name=ProviderEnum.vek.value),
            ProviderModel(name=ProviderEnum.sila.value),
        ]
    )


def delete_providers(app, schema_editor):
    ProviderModel = app.get_model(app_label="providers", model_name="ProviderModel")
    ProviderModel.objects.filter(
        name__in=[ProviderEnum.vek.value, ProviderEnum.sila.value]
    ).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("providers", "0001_initial"),
    ]

    operations = [migrations.RunPython(create_providers, delete_providers)]
