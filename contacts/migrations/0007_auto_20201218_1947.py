# Generated by Django 3.1.2 on 2020-12-18 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0006_contact_car_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contact',
            new_name='Car_Request',
        ),
    ]
