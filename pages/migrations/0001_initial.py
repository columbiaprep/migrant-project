# Generated by Django 4.2.11 on 2024-05-20 22:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('vicinity', models.CharField(max_length=255)),
                ('latitude', models.CharField(max_length=255)),
                ('longitude', models.CharField(max_length=255)),
                ('number', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('photo_url', models.URLField(blank=True, max_length=255, null=True)),
                ('hours_array', models.JSONField(blank=True, null=True)),
                ('business_status', models.CharField(blank=True, max_length=255, null=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='MatchShelters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donate_link', models.URLField()),
                ('shelter_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.location')),
            ],
        ),
    ]
