# Generated by Django 2.2.4 on 2019-08-10 01:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20190810_0833'),
    ]

    operations = [
        migrations.RenameField(
            model_name='brand',
            old_name='Slug_Brand',
            new_name='slug',
        ),
        migrations.RenameField(
            model_name='brand',
            old_name='Name_Brand',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='Slug_Category',
            new_name='slug',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='Name_Category',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Slug',
            new_name='slug',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Name_Product',
            new_name='title',
        ),
    ]
