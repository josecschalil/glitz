# Generated by Django 3.1.7 on 2021-04-03 03:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_activities_dates'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activities',
            name='Dates',
        ),
    ]
