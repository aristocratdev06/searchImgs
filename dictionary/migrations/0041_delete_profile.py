# Generated by Django 4.0.6 on 2022-08-03 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0040_remove_profile_email_remove_profile_last_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
