# Generated by Django 4.0.4 on 2022-04-23 06:32

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_productvariation_discountprice'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='product',
            managers=[
                ('onSale_objects', django.db.models.manager.Manager()),
            ],
        ),
    ]
