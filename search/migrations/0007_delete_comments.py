# Generated by Django 4.1 on 2022-08-13 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0006_followerslen'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comments',
        ),
    ]