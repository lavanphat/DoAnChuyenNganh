# Generated by Django 2.2.5 on 2019-09-26 01:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0015_auto_20190926_0858'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bill',
            name='Address',
        ),
        migrations.RemoveField(
            model_name='bill',
            name='Phone',
        ),
    ]
