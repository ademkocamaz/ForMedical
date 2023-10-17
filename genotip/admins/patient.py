from typing import Any
from django.contrib import admin
from django.http.request import HttpRequest

from genotip.model.patient import *
from genotip.model.visit import *

from genotip.admins.visit import VisitInline

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    fields=[field.name for field in Patient._meta.fields if field.name not in 'id']
    list_display=[field.name for field in Patient._meta.fields if field.name not in 'id']
    readonly_fields=[field.name for field in Patient._meta.fields if field.name not in 'id']
    search_fields=('dosyano',)
    ordering=('-dosyano',)
    
    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False

    inlines=[
        VisitInline,
    ]