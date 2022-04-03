# Generated by Django 4.0.3 on 2022-04-02 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_datagenset_jenis_genset'),
    ]

    operations = [
        migrations.AddField(
            model_name='datagenset',
            name='jam_penggunaan',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='sparepart',
            unique_together={('merek', 'pn', 'tipe_sparepart')},
        ),
    ]