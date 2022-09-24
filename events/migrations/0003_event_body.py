# Generated by Django 2.2.9 on 2020-01-05 07:02

import cms.models.fields
from django.db import migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        ('events', '0002_auto_20200105_0650'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='body',
            field=cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, slotname='body', to='cms.Placeholder'),
        ),
    ]