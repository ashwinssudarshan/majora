# Generated by Django 2.2.10 on 2020-03-27 10:00

from django.db import migrations

def copy_dna_id(apps, schema_editor):
    DNASequencingProcess = apps.get_model("majora2", "DNASequencingProcess")
    for d in DNASequencingProcess.objects.all():
        d.run_name = str(d.id)
        d.save()

class Migration(migrations.Migration):

    dependencies = [
        ('majora2', '0035_dnasequencingprocess_run_name'),
    ]

    operations = [
        migrations.RunPython(copy_dna_id),
    ]