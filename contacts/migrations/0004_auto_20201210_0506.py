# Generated by Django 3.1.4 on 2020-12-09 23:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_auto_20201210_0445'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='onecar',
            new_name='car_name',
        ),
    ]
