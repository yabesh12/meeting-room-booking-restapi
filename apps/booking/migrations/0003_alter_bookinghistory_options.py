# Generated by Django 4.2 on 2023-12-10 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinghistory',
            options={'verbose_name_plural': 'Booking Histories'},
        ),
    ]