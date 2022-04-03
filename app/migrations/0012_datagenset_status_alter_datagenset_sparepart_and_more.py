# Generated by Django 4.0.3 on 2022-04-02 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_datagenset_jam_penggunaan_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='datagenset',
            name='status',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='datagenset',
            name='sparepart',
            field=models.ManyToManyField(blank=True, to='app.sparepart'),
        ),
        migrations.CreateModel(
            name='SparepartUtility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.CharField(blank=True, max_length=255, null=True)),
                ('sparepart', models.JSONField(blank=True, null=True)),
                ('genset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.datagenset')),
            ],
        ),
        migrations.CreateModel(
            name='GensetUtility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.CharField(blank=True, max_length=255, null=True)),
                ('lama_penggunaan', models.IntegerField()),
                ('alasan_pemakaian', models.CharField(blank=True, max_length=255, null=True)),
                ('lokasi', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('genset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.datagenset')),
            ],
        ),
    ]
