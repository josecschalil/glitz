# Generated by Django 3.1.7 on 2021-04-03 02:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20210402_0323'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activities',
            name='Dates',
        ),
    ]
