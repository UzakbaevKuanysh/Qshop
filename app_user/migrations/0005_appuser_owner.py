# Generated by Django 4.0.4 on 2022-05-03 13:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_user', '0004_alter_appuser_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='appuser', to=settings.AUTH_USER_MODEL),
        ),
    ]
