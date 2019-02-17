# Generated by Django 2.1.3 on 2018-11-23 13:12

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('life', '0004_auto_20181123_1424'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('address', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='PersonEducation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('finish_date', models.DateTimeField(default=None)),
                ('education', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='membership', to='life.Education')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='membership', to='life.Person')),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='educations',
            field=models.ManyToManyField(related_name='pupils', through='life.PersonEducation', to='life.Education'),
        ),
    ]
