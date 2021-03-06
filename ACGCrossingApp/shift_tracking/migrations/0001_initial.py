# Generated by Django 2.2.10 on 2020-02-09 18:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('zone', models.CharField(max_length=255)),
                ('latitude', models.IntegerField(help_text='Latitude should be between -90 and 90 degrees.', validators=[django.core.validators.MaxValueValidator(90), django.core.validators.MinValueValidator(-90)])),
                ('longitude', models.IntegerField(help_text='Longitude should be between -180 and 180 degrees.', validators=[django.core.validators.MaxValueValidator(180), django.core.validators.MinValueValidator(-180)])),
                ('description', models.TextField(blank=True)),
                ('location_number', models.IntegerField()),
            ],
        ),
    ]
