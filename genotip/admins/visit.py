from typing import Any
from django.contrib import admin
from django.http.request import HttpRequest

from genotip.model.visit import *
from genotip.admins.service import ServiceInline

class VisitInline(admin.StackedInline):
    model = Visit
    readonly_fields=[field.name for field in Visit._meta.fields]
    extra=0
    max_num=0
    can_delete=False
    classes = ('collapse-entry', )
    inlines=[
        ServiceInline,
    ]

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False
    
@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    fields=[field.name for field in Visit._meta.fields if field.name not in 'id']
    list_display=[field.name for field in Visit._meta.fields if field.name not in 'id']
    search_fields=('dosyano',)
    # autocomplete_fields = ('patient',)
    readonly_fields=[field.name for field in Visit._meta.fields if field.name not in 'id']
    ordering=('-giristarih', '-dosyano',)
    
    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False

    inlines=[
        ServiceInline,
    ]