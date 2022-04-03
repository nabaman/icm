from django.db import transaction
from django.db.models import F
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import *
from .forms import ServisForm,PemakaianForm

# Create your views here.
def home(request):
    context = {
        'genset': DataGenset.objects.all().order_by('-jam_penggunaan','jenis_genset'),
        'servis': SparepartUtility.objects.all(),
        'ready':DataGenset.objects.filter(status_genset="READY").count(),
        'dipakai':DataGenset.objects.filter(status_genset="DIPAKAI").count(),
        'diservis':DataGenset.objects.filter(status_genset="SERVIS").count(),
        'sparepart': TipeSparepart.objects.all(),
        'nama_genset':[x.jenis_genset for x in DataGenset.objects.all()],
        'series': [x.jam_penggunaan for x in DataGenset.objects.all()]
    }
    return render(request, 'home.html', context)

@transaction.atomic
def detailgenset(request, id):
    data = DataGenset.objects.get(id=id)
    form = ServisForm()
    pemakaianform = PemakaianForm()
    if request.method == 'POST':
        keys = TipeSparepart.objects.all().values_list('jenis_sparepart', flat=True)
        data_sparepart = {your_key: request.POST.get(your_key) for your_key in keys if
                          request.POST.get(your_key) and request.POST.get(your_key) is not '0'}
        cp_data_sparepart = data_sparepart.copy()
        tanggal_servis = request.POST.get('tanggal_servis')
        jenis_servis = request.POST.get('jenis_servis')
        tz = timezone.get_current_timezone()

        for key, value in data_sparepart.items():
            data.sparepart.filter(tipe_sparepart__jenis_sparepart=key).update(qty=F('qty') - int(value))
            sparepart = data.sparepart.get(tipe_sparepart__jenis_sparepart=key)
            new_key = f"{key} {sparepart.merek} {sparepart.pn}"
            cp_data_sparepart[new_key] = cp_data_sparepart.pop(key)

        SparepartUtility.objects.create(
            genset=data,
            jenis_servis=jenis_servis,
            tanggal_servis=timezone.datetime.strptime(tanggal_servis, '%Y-%m-%d').replace(tzinfo=tz),
            pic=request.user.username,
            sparepart=cp_data_sparepart,
        )
        data.status_genset = "SERVIS"
        data.jumlah_servis+=1
        data.save()
        return redirect('detailgenset', id)
    context = {
        'data': data,
        'form': form,
        'pemakaian': GensetUtility.objects.order_by('-id'),
        'servis': data.sparepartutility_set.order_by('-id'),
        'pemakaianform':pemakaianform
    }
    return render(request, 'detail_genset.html', context)

@transaction.atomic
def penggunaangenset(request,id):
    if request.method == 'POST':
        data = DataGenset.objects.get(id=id)
        durasi_penggunaan = request.POST.get('durasi')
        tujuan_penggunaan = request.POST.get('tujuan')
        tanggal_penggunaan = request.POST.get('tanggal_pakai')
        lokasi_penggunaan = request.POST.get('lokasi')
        tz = timezone.get_current_timezone()
        GensetUtility.objects.create(
            genset=data,
            alasan_pemakaian=tujuan_penggunaan,
            lama_penggunaan=durasi_penggunaan,
            lokasi=lokasi_penggunaan,
            tanggal_pemakaian=timezone.datetime.strptime(tanggal_penggunaan, '%Y-%m-%d').replace(tzinfo=tz),
        )
        data.jam_penggunaan+=int(durasi_penggunaan)
        data.save()



    return redirect('detailgenset',id)


@transaction.atomic
def hxdropdownstatus(request,id):
    genset = DataGenset.objects.get(id=id)
    context = {
        'status': DataGenset.status,
        'data': genset
    }
    if request.method == 'POST':
        status_genset = request.POST.get('status_genset')
        genset.status_genset = status_genset
        genset.save()
        return render(request,'status-genset.html',context)
    return render(request, 'hx-form-dropdown-status.html', context)
