# Generated by Django 4.0.1 on 2022-01-30 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='milage',
            new_name='mileage',
        ),
    ]
