# Generated by Django 2.2.5 on 2019-09-28 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0036_image_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='Image',
            field=models.CharField(max_length=1000, verbose_name='Banner'),
        ),
    ]
