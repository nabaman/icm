# Generated by Django 4.0.3 on 2022-04-02 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_merek_merek'),
    ]

    operations = [
        migrations.DeleteModel(
            name='EngineGenset',
        ),
        migrations.DeleteModel(
            name='Generator',
        ),
        migrations.RemoveField(
            model_name='kebutuhansparepart',
            name='sparepart',
        ),
        migrations.RemoveField(
            model_name='servis',
            name='genset',
        ),
        migrations.RemoveField(
            model_name='servis',
            name='sparepart',
        ),
        migrations.RemoveField(
            model_name='utilitas',
            name='genset',
        ),
        migrations.DeleteModel(
            name='Genset',
        ),
        migrations.DeleteModel(
            name='KebutuhanSparepart',
        ),
        migrations.DeleteModel(
            name='Merek',
        ),
        migrations.DeleteModel(
            name='Servis',
        ),
        migrations.DeleteModel(
            name='Sparepart',
        ),
        migrations.DeleteModel(
            name='TipeGenset',
        ),
        migrations.DeleteModel(
            name='Utilitas',
        ),
    ]
