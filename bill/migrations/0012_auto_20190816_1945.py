# Generated by Django 2.2.4 on 2019-08-16 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0011_auto_20190811_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='Total_Money',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10, verbose_name='Tổng Tiền'),
        ),
    ]
