# Generated by Django 4.0.6 on 2022-08-03 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0037_remove_myuser_bio_remove_myuser_img_profile_bio_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='img',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.AddField(
            model_name='myuser',
            name='bio',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='myuser',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]