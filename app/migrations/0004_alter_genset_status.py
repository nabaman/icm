# Generated by Django 4.0.3 on 2022-03-28 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_servis_tanggal_servis_utilitas_tanggal_pakai'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genset',
            name='status',
            field=models.CharField(max_length=255),
        ),
    ]