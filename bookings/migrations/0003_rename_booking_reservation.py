# Generated by Django 4.2.14 on 2024-07-25 13:15

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookings', '0002_alter_booking_time'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Booking',
            new_name='Reservation',
        ),
    ]
