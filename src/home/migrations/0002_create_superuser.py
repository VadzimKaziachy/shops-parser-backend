from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.db import migrations


def create_user(apps, schema_editor):
    User = apps.get_model(app_label="auth", model_name="User")
    admin_user = User()
    admin_user.username = settings.ADMIN_USER_NAME
    admin_user.password = make_password(settings.ADMIN_USER_PASSWORD)
    admin_user.is_staff = True
    admin_user.is_superuser = True
    admin_user.save()


def delete_user(app, schema_editor):
    User = app.get_model(app_label="auth", model_name="User")
    admin_users = User.objects.filter(username=settings.ADMIN_USER_NAME)
    if admin_users.exists():
        admin_users.first().delete()


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [migrations.RunPython(create_user, delete_user)]
