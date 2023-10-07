from django.contrib import admin
from nested_inline.admin import NestedStackedInline, NestedModelAdmin

from ..model.patient import *

@admin.register(Patient)
class PatientAdmin(NestedModelAdmin):
    fields = ('dosyano','ad','soyad','vatandaslikno', 'cinsiyet', 'dogumtarih')
    list_display = ('dosyano','ad','soyad', 'vatandaslikno', 'cinsiyet', 'dogumtarih')
    readonly_fields = ('dosyano','ad','soyad', 'vatandaslikno', 'cinsiyet', 'dogumtarih')
    search_fields = ('dosyano','vatandaslikno')

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
    
    change_form_template = "override/patient_change_form.html"
    change_list_template = "override/patient_change_list.html"

    ordering = ('-dosyano',)
    # inlines=[
    #     PainInline,
    # ]