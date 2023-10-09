from django.contrib import admin

from formedical.model.service import Service
from form.admins.pain import PainInline

class ServiceInline(admin.StackedInline):
    model=Service
    readonly_fields=[field.name for field in Service._meta.fields]
    extra=0
    max_num=0
    can_delete=False
    classes = ('collapse','collapse-entry', )
    inlines=[
        PainInline,
    ]

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    fields=[field.name for field in Service._meta.fields if field.name not in 'id']
    list_display=[field.name for field in Service._meta.fields if field.name not in 'id']
    search_fields=('dosyano', 'servis', 'oda')
    list_display_links=('visit',)
    list_filter=('giristarih', 'servis')
    readonly_fields=[field.name for field in Service._meta.fields if field.name not in 'id']
    ordering=('-giristarih', '-dosyano',)

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
        PainInline,
    ]
