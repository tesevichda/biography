# Generated by Django 2.1.3 on 2018-11-23 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('life', '0005_auto_20181123_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personeducation',
            name='finish_date',
            field=models.DateTimeField(null=True),
        ),
    ]