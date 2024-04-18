# Generated by Django 4.2.11 on 2024-04-18 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_location_photo_reference'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='photo_reference',
        ),
        migrations.AddField(
            model_name='location',
            name='photo_url',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
    ]