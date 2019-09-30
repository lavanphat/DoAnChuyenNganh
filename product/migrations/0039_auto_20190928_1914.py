# Generated by Django 2.2.5 on 2019-09-28 12:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0038_auto_20190928_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='Number',
            field=models.IntegerField(blank=True, null=True, unique=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(3)]),
        ),
    ]
