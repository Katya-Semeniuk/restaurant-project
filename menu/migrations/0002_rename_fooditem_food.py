# Generated by Django 4.2.14 on 2024-07-25 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FoodItem',
            new_name='Food',
        ),
    ]