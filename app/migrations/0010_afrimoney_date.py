# Generated by Django 5.1 on 2024-11-06 20:10

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_afrimoney_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='afrimoney',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
