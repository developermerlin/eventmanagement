# Generated by Django 5.1 on 2024-11-07 08:06

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_creditcard'),
    ]

    operations = [
        migrations.AddField(
            model_name='creditcard',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]