# Generated by Django 4.0.3 on 2022-04-02 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0008_delete_enginegenset_delete_generator_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipeSparepart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jenis_sparepart', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SparePart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField(blank=True, null=True)),
                ('merek', models.CharField(blank=True, max_length=255, null=True)),
                ('pn', models.CharField(blank=True, max_length=255, null=True)),
                ('tipe_sparepart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.tipesparepart')),
            ],
            options={
                'unique_together': {('merek', 'pn')},
            },
        ),
        migrations.CreateModel(
            name='DataGenset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('merek_genset', models.CharField(blank=True, max_length=255, null=True)),
                ('type_genset', models.CharField(blank=True, max_length=255, null=True)),
                ('sn_genset', models.CharField(blank=True, max_length=255, null=True)),
                ('kva', models.CharField(blank=True, max_length=255, null=True)),
                ('merek_engine', models.CharField(blank=True, max_length=255, null=True)),
                ('type_engine', models.CharField(blank=True, max_length=255, null=True)),
                ('merek_generator', models.CharField(blank=True, max_length=255, null=True)),
                ('sn_generator', models.CharField(blank=True, max_length=255, null=True)),
                ('model_generator', models.CharField(blank=True, max_length=255, null=True)),
                ('nopol', models.CharField(blank=True, max_length=255, null=True)),
                ('status_genset', models.CharField(blank=True, max_length=255, null=True)),
                ('sparepart', models.ManyToManyField(to='app.sparepart')),
            ],
        ),
    ]