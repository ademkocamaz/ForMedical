from django.contrib import admin

# Register your models here.
from .admins.pain import PainAdmin
from .admins.patient import PatientAdmin
from .admins.visit import VisitAdmin
from .admins.service import ServiceAdmin

admin.site.site_title='ForMedical Yönetim Paneli'
admin.site.site_header='ForMedical'
admin.site.index_title='ForMedical - Hemşire Formları Yönetimine, Hoşgeldiniz.'
