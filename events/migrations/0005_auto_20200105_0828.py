# Generated by Django 2.2.9 on 2020-01-05 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20200105_0822'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='listed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='event',
            name='published',
            field=models.BooleanField(default=False),
        ),
    ]
