# Generated by Django 4.0.3 on 2022-04-02 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_remove_datagenset_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sparepartutility',
            name='jenis_servis',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
