# Generated by Django 5.0.6 on 2024-10-03 15:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish_name', models.CharField(max_length=100)),
                ('dish_venue', models.CharField(max_length=100)),
                ('cost_of_dish', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=100)),
                ('event_description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('venue_name', models.CharField(max_length=100)),
                ('cost_per_day', models.DecimalField(decimal_places=2, max_digits=10)),
                ('facilities', models.TextField()),
                ('address', models.CharField(max_length=100)),
                ('contact', models.IntegerField()),
                ('profile', models.ImageField(blank=True, null=True, upload_to='venue/')),
                ('video', models.FileField(blank=True, null=True, upload_to='venue/')),
                ('venue_event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.event')),
            ],
        ),
    ]
