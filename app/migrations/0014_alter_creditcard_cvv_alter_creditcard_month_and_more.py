# Generated by Django 5.1 on 2024-11-07 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_remove_creditcard_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditcard',
            name='cvv',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='month',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='year',
            field=models.IntegerField(null=True),
        ),
    ]
