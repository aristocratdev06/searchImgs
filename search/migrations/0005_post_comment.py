# Generated by Django 4.1 on 2022-08-06 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0004_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='comment',
            field=models.TextField(default=1, max_length=700),
            preserve_default=False,
        ),
    ]
