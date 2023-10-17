from django.contrib import admin

from genotip.model.service import Service, ServiceDefinition
from form.admins.pain import PainInline

@admin.register(ServiceDefinition)
class ServiceDefinitionAdmin(admin.ModelAdmin):
    fields=[field.name for field in ServiceDefinition._meta.fields if field.name not in 'id']
    list_display=[field.name for field in ServiceDefinition._meta.fields if field.name not in 'id']
    search_fields=('ad',)
    list_display_links=('ad',)
    ordering=('ad',)

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False

class ServiceInline(admin.StackedInline):
    model=Service
    extra=0
    max_num=0
    can_delete=False
    classes = ('collapse-entry', )
    inlines=[
        PainInline,
    ]
    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False
    

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    fields=[field.name for field in Service._meta.fields if field.name not in 'id']
    list_display=[field.name for field in Service._meta.fields if field.name not in 'id']
    search_fields=('dosyano', 'servis', 'oda')
    list_display_links=('visit',)
    # list_filter=('giristarih', 'servis')
    # readonly_fields=[field.name for field in Service._meta.fields if field.name not in 'id']
    ordering=('-giristarih', '-dosyano',)
    
    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False

    inlines=[
        PainInline,
    ]
