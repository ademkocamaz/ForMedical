from django.contrib import admin

# Register your models here.
from genotip.admins.patient import PatientAdmin
from genotip.admins.visit import VisitAdmin
from genotip.admins.service import ServiceAdmin, ServiceDefinitionAdmin
from genotip.admins.user import UserAdmin

# admin.site.site_title='ForMedical Yönetim Paneli'
# admin.site.site_header='ForMedical'
# admin.site.index_title='ForMedical - Hemşire Formları Yönetimine, Hoşgeldiniz.'
