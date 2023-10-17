from django.contrib import admin
from genotip.model.user import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=[field.name for field in User._meta.fields if field.name not in 'id']
    search_fields=('username', 'user')
    list_display_links=('username',)
    # list_filter=('is_inactive', 'is_superuser','group')
    # readonly_fields=[field.name for field in User._meta.fields if field.name not in 'id']
    
    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False
