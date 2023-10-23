from django.contrib import admin

from genotip._model.bed import Bed

@admin.register(Bed)
class BedAdmin(admin.ModelAdmin):
    fields=[field.name for field in Bed._meta.fields if field.name not in 'id']
    list_display=[field.name for field in Bed._meta.fields if field.name not in 'id']
    search_fields=('oda',)
    list_display_links=('oda',)
    ordering=('oda',)

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False