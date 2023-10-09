from typing import Any
from django.contrib import admin
from django.http.request import HttpRequest
from nested_inline.admin import NestedStackedInline, NestedModelAdmin

from formedical.model.patient import *
from formedical.model.visit import *

from formedical.admins.visit import VisitInline

@admin.register(Patient)
class PatientAdmin(NestedModelAdmin):
    fields=[field.name for field in Patient._meta.fields if field.name not in 'id']
    list_display=[field.name for field in Patient._meta.fields if field.name not in 'id']
    readonly_fields=[field.name for field in Patient._meta.fields if field.name not in 'id']
    search_fields=('dosyano',)
    ordering=('-dosyano',)
    
    def change_view(self, request, object_id, form_url="", extra_context=None):
        context = {}
        context.update(extra_context or {})
        context.update({"read_only": True})
        return super().change_view(request, object_id, form_url, extra_context=context)

    def changelist_view(self, request, extra_context=None):
        context = {}
        context.update(extra_context or {})
        context.update({"read_only": True})
        return super().changelist_view(request, extra_context=context)
    
    change_form_template = "override/change_form.html"
    change_list_template = "override/change_list.html"

    inlines=[
        VisitInline,
    ]