# Generated by Django 2.2.5 on 2019-09-26 02:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0029_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='Image',
        ),
        migrations.RemoveField(
            model_name='category',
            name='Image_URL',
        ),
    ]
