from django.db import models
from django.contrib.auth.models import User

# min stock notification
# oli 50 liter
# coolant 40 liter
# aki 2
# filter oli 2
# filter solar 2
# filter udara 1
# van belt 1
# filter air 2



class TipeSparepart(models.Model):
    jenis_sparepart = models.CharField(max_length=255, null=True, blank=True)
    limit_notif = models.IntegerField(default=0)

    def __str__(self):
        return self.jenis_sparepart


class SparePart(models.Model):
    tipe_sparepart = models.ForeignKey(TipeSparepart, on_delete=models.CASCADE)
    qty = models.IntegerField(null=True, blank=True)
    merek = models.CharField(max_length=255, null=True, blank=True)
    pn = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        unique_together = ['merek', 'pn', 'tipe_sparepart']

    def __str__(self):
        return f'{self.tipe_sparepart.jenis_sparepart} {self.merek} {self.pn}'


class DataGenset(models.Model):
    status = (
        ("READY","READY"),
        ("SERVIS","SERVIS"),
        ("DIPAKAI","SERVIS"),
        ("GROUNDED","GROUNDED"),
    )
    jenis_genset = models.CharField(max_length=255, blank=True, null=True)
    sparepart = models.ManyToManyField(SparePart,blank=True)
    merek_genset = models.CharField(max_length=255, null=True, blank=True)
    type_genset = models.CharField(max_length=255, null=True, blank=True)
    sn_genset = models.CharField(max_length=255, null=True, blank=True)
    kva = models.CharField(max_length=255, null=True, blank=True)
    merek_engine = models.CharField(max_length=255, null=True, blank=True)
    type_engine = models.CharField(max_length=255, null=True, blank=True)
    merek_generator = models.CharField(max_length=255, null=True, blank=True)
    sn_generator = models.CharField(max_length=255, null=True, blank=True)
    model_generator = models.CharField(max_length=255, null=True, blank=True)
    nopol = models.CharField(max_length=255, null=True, blank=True)
    status_genset = models.CharField(max_length=255,choices=status, null=True, blank=True)
    jam_penggunaan = models.IntegerField(blank=True, null=True)
    jumlah_servis = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.jenis_genset} {self.merek_genset} {self.nopol} {self.type_genset} {self.sn_genset}'

class GensetUtility(models.Model):
    genset = models.ForeignKey(DataGenset,on_delete=models.CASCADE)
    pic = models.CharField(max_length=255, null=True, blank=True)
    lama_penggunaan = models.IntegerField()
    alasan_pemakaian = models.CharField(max_length=255, null=True, blank=True)
    lokasi = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    tanggal_pemakaian = models.DateTimeField(null=True,blank=True)

class SparepartUtility(models.Model):
    servis_choice = (
        ('250 JAM','250 JAM'),
        ('2500 JAM','2500 JAM'),
        ('10000 JAM','10000 JAM'),
    )
    genset = models.ForeignKey(DataGenset,on_delete=models.CASCADE)
    jenis_servis = models.CharField(max_length=255,blank=True,null=True,choices=servis_choice)
    pic = models.CharField(max_length=255, null=True, blank=True)
    sparepart = models.JSONField(null=True,blank=True)
    tanggal_servis = models.DateTimeField(null=True,blank=True)

