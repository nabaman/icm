from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Sparepart(models.Model):
    merek = models.CharField(max_length=255,null=True)
    pn = models.CharField(max_length=255,null=True)
    jenis_sparepart = models.CharField(max_length=255,null=True)

    def __str__(self):
        return self.nama_sparepart

class TipeGenset(models.Model):
    tipe = models.CharField(max_length=255,null=True)

    def __str__(self):
        return self.tipe

class Merek(models.Model):
    merek = models.CharField(max_length=255,null=True)

    def __str__(self):

        return self.merek

class EngineGenset(models.Model):
    merek = models.CharField(max_length=255,null=True)
    tipe = models.CharField(max_length=255,null=True)

    def __str__(self):
        return self.merek

class Generator(models.Model):
    merek = models.CharField(max_length=255,null=True)
    sn = models.CharField(max_length=255,null=True)
    model = models.CharField(max_length=255,null=True)

    def __str__(self):
        return self.merek

class Genset(models.Model):
    mpu = models.CharField(max_length=100)
    nopol = models.CharField(max_length=255,null=True)
    merek = models.ForeignKey(Merek,on_delete=models.SET_NULL,null=True)
    sn = models.CharField(max_length=100,null=True)
    kva = models.CharField(max_length=50,null=True)
    tipe = models.ForeignKey(TipeGenset,on_delete=models.SET_NULL,null=True)
    status = models.CharField(max_length=255,null=True)

    def __str__(self):
        return self.merek

class Utilitas(models.Model):
    genset = models.ForeignKey(Genset,on_delete=models.CASCADE)
    jam = models.CharField(max_length=10)
    alasan = models.TextField(null=True)
    pic = models.CharField(max_length=255,null=True)
    tanggal_pakai = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.genset

class KebutuhanSparepart(models.Model):
    sparepart = models.ForeignKey(Sparepart,on_delete=models.CASCADE,null=True)
    jumlah = models.CharField(max_length=255,null=True)

class Servis(models.Model):
    genset = models.ForeignKey(Genset,on_delete=models.CASCADE)
    jenis_servis = models.CharField(max_length=200)
    sparepart = models.ManyToManyField(KebutuhanSparepart)
    pic = models.CharField(max_length=255,null=True)
    tanggal_servis = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.jenis_servis

