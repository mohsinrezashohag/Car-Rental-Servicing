# Generated by Django 3.1.2 on 2020-12-18 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0008_auto_20201219_0049'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service_request',
            old_name='message',
            new_name='problem_shortly',
        ),
    ]
