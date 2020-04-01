# Generated by Django 2.2.10 on 2020-03-31 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('majora2', '0040_auto_20200329_1814'),
    ]

    operations = [
        migrations.AddField(
            model_name='majoraartifact',
            name='created',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='artifacts_created', to='majora2.MajoraArtifactProcess'),
        ),
    ]