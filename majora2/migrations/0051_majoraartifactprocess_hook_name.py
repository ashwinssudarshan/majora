# Generated by Django 2.2.10 on 2020-04-09 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('majora2', '0050_auto_20200406_0855'),
    ]

    operations = [
        migrations.AddField(
            model_name='majoraartifactprocess',
            name='hook_name',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]