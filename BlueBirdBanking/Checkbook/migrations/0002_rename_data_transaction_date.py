# Generated by Django 5.0 on 2023-12-07 22:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Checkbook', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='data',
            new_name='date',
        ),
    ]
