# Generated by Django 2.2.10 on 2020-03-18 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('majora2', '0007_auto_20200318_1535'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='api_key',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
