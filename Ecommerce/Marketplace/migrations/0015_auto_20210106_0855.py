# Generated by Django 3.1.4 on 2021-01-06 06:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Marketplace', '0014_auto_20210106_0855'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='date',
        ),
        migrations.RemoveField(
            model_name='seller',
            name='date',
        ),
    ]
