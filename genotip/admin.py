from django.contrib import admin

# Register your models here.
from genotip._admin.patient import PatientAdmin
from genotip._admin.visit import VisitAdmin
from genotip._admin.service import ServiceAdmin, ServiceDefinitionAdmin
from genotip._admin.user import UserAdmin
from genotip._admin.bed import BedAdmin

# admin.site.site_title='ForMedical Yönetim Paneli'
# admin.site.site_header='ForMedical'
# admin.site.index_title='ForMedical - Hemşire Formları Yönetimine, Hoşgeldiniz.'
