from django.contrib import admin

from nested_inline.admin import NestedStackedInline, NestedModelAdmin

from ..model.service import Service

class ServiceInline(NestedStackedInline):
    model=Service
    readonly_fields=[field.name for field in Service._meta.get_fields()]
    extra=0
    max_num=0
    can_delete=False

@admin.register(Service)
class ServiceAdmin(NestedModelAdmin):
    fields = [field.name for field in Service._meta.get_fields() if field.name not in 'id']
    list_display=[field.name for field in Service._meta.get_fields() if field.name not in 'id']
    search_fields=('dosyano',)
    readonly_fields=[field.name for field in Service._meta.get_fields() if field.name not in 'id']
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
