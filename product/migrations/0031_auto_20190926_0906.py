# Generated by Django 2.2.5 on 2019-09-26 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0030_auto_20190926_0906'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Hình loại'),
        ),
        migrations.AddField(
            model_name='category',
            name='Image_URL',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Link Hình'),
        ),
    ]
