# Generated by Django 2.2.4 on 2019-08-23 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0012_auto_20190816_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='Date_Create',
            field=models.DateTimeField(verbose_name='Ngày Tạo'),
        ),
    ]
