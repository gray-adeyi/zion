# Generated by Django 3.1.1 on 2020-11-09 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrayerRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Anonymous', max_length=20, null=True)),
                ('prayer_request', models.TextField()),
                ('timestamp', models.DateTimeField()),
            ],
        ),
    ]