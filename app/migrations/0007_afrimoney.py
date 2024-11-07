# Generated by Django 5.1 on 2024-11-05 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_book_event_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Afrimoney',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.IntegerField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pin', models.IntegerField()),
            ],
        ),
    ]
