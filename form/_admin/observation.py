from django.contrib import admin
from form._model.observation import Observation

@admin.register(Observation)
class Observation_Admin(admin.ModelAdmin):
    fields = [
        field.name
        for field in Observation._meta.fields
        if field.name not in ("id", "edited", "created")
    ]
    list_display = [
        field.name
        for field in Observation._meta.fields
        if field.name in ("bed", "service", "edited", "created", "user")
    ]
    list_display_links = ("service", "bed")
    search_fields = ("service", "bed")
    readonly_fields = ("bed", "service", "user")
    save_on_top = True


    def save_model(self, request, obj, form, change):
        """
        Given a model instance save it to the database.
        """
        obj.user = request.user
        obj.save()

