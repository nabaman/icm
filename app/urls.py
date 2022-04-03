from django.urls import path
from app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('genset/<str:id>', views.detailgenset, name='detailgenset'),
    path('hx-dropdown/<str:id>',views.hxdropdownstatus,name='dropdownstatus'),
    path('pemakaiangenset/<str:id>',views.penggunaangenset,name='pemakaian'),

]
