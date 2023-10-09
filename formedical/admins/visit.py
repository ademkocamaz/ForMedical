from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from nested_inline.admin import NestedStackedInline

from ..model.visit import *

class VisitInline(NestedStackedInline):
    model = Visit
    readonly_fields=[field.name for field in Visit._meta.get_fields()]
    extra=0
    max_num=0
    can_delete=False

    # def get_queryset(self, request):
    #     qs = super().get_queryset(request)
    #     if request.user.is_superuser:
    #         return qs
    #     return qs.filter(author=request.user)
    
@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    fields = [field.name for field in Visit._meta.get_fields() if field.name not in 'id']
    list_display=[field.name for field in Visit._meta.get_fields() if field.name not in 'id']
    search_fields=('dosyano',)
    # autocomplete_fields = ('patient',)
    readonly_fields=[field.name for field in Visit._meta.get_fields() if field.name not in 'id']
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