# Generated by Django 4.0.3 on 2022-04-01 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_rename_nama_sparepart_sparepart_jenis_sparepart_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merek',
            name='merek',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
    ]
