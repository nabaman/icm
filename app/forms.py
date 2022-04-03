from django import forms
from .models import *



class DateInput(forms.DateInput):
    input_type = 'date'

class ServisForm(forms.Form):
    tanggal_servis = forms.DateField(widget=DateInput(attrs={'class':'form-control'}),required=True)
    jenis_servis = forms.ChoiceField(choices=SparepartUtility.servis_choice,widget=forms.Select(attrs={'class':'form-select'}))

class PemakaianForm(forms.Form):
    tanggal_pakai= forms.DateField(widget=DateInput(attrs={'class':'form-control'}),required=True)

