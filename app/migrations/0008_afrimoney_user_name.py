# Generated by Django 5.1 on 2024-11-05 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_afrimoney'),
    ]

    operations = [
        migrations.AddField(
            model_name='afrimoney',
            name='user_name',
            field=models.CharField(default=3, max_length=50),
            preserve_default=False,
        ),
    ]
