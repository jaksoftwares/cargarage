# Generated by Django 5.1.4 on 2024-12-13 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_booking_status_alter_booking_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='preferred_date',
            field=models.DateField(default='2024-01-01'),
        ),
    ]
