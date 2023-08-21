# Generated by Django 4.2.3 on 2023-07-20 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PrayerTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('fajr', models.TimeField()),
                ('dhuhr', models.TimeField()),
                ('asr', models.TimeField()),
                ('maghrib', models.TimeField()),
                ('isha', models.TimeField()),
            ],
        ),
    ]