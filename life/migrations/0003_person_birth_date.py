# Generated by Django 2.1.3 on 2018-11-23 08:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('life', '0002_auto_20181119_1625'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='birth_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
