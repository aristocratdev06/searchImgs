# Generated by Django 4.0.6 on 2022-08-02 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0027_alter_myuser_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='website',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
