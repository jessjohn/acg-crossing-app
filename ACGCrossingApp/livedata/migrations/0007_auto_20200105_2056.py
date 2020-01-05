# Generated by Django 2.2.9 on 2020-01-05 20:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('livedata', '0006_auto_20191027_0422'),
    ]

    operations = [
        migrations.AddField(
            model_name='usershift',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usershift',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
