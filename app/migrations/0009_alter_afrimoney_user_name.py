# Generated by Django 5.1 on 2024-11-05 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_afrimoney_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='afrimoney',
            name='user_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
