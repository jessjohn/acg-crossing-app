# Generated by Django 2.2.6 on 2019-10-26 20:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Locations',
            new_name='Location',
        ),
    ]