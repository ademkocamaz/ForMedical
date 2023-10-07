from django.contrib import admin

from nested_inline.admin import NestedStackedInline, NestedModelAdmin
from django_object_actions import DjangoObjectActions, action

from ..model.pain import *

class PainScaleInline(NestedStackedInline):
    model = PainScale
    extra = 1
    # fields=('description',)
    # classes = ('collapse',)
    # fieldsets = [
    #     (
    #         "Bilgiler",
    #         {
    #             "classes": ["collapse"],
    #             "fields": [field.name for field in model._meta.concrete_fields if field.name not in ('id', 'edited', 'created')],
    #         },
    #     ),
    # ]

class PainPlaceInline(NestedStackedInline):
    model = PainPlace
    extra = 1
    # fieldsets = [
    #     (
    #         "Bilgiler",
    #         {
    #             "classes": ["collapse"],
    #             "fields": [field.name for field in model._meta.concrete_fields if field.name not in ('id', 'edited', 'created')],
    #         },
    #     ),
    # ]

class PainSeverityInline(NestedStackedInline):
    model = PainSeverity
    extra = 1
    # fieldsets = [
    #     (
    #         "Bilgiler",
    #         {
    #             "classes": ["collapse"],
    #             "fields": [field.name for field in model._meta.concrete_fields if field.name not in ('id', 'edited', 'created')],
    #         },
    #     ),
    # ]

class PainFrequencyInline(NestedStackedInline):
    model = PainFrequency
    extra = 1
    # fieldsets = [
    #     (
    #         "Bilgiler",
    #         {
    #             "classes": ["collapse"],
    #             "fields": [field.name for field in model._meta.concrete_fields if field.name not in ('id', 'edited', 'created')],
    #         },
    #     ),
    # ]

class PainNatureInline(NestedStackedInline):
    model = PainNature
    extra = 1
    # fieldsets = [
    #     (
    #         "Bilgiler",
    #         {
    #             "classes": ["collapse"],
    #             "fields": [field.name for field in model._meta.concrete_fields if field.name not in ('id', 'edited', 'created')],
    #         },
    #     ),
    # ]

class PainFactorAffectingInline(NestedStackedInline):
    model = PainFactorAffecting
    extra = 1
    # fieldsets = [
    #     (
    #         "Bilgiler",
    #         {
    #             "classes": ["collapse"],
    #             "fields": [field.name for field in model._meta.concrete_fields if field.name not in ('id', 'edited', 'created')],
    #         },
    #     ),
    # ]

class PainTargetedLevelInline(NestedStackedInline):
    model = PainTargetedLevel
    extra = 1
    # fieldsets = [
    #     (
    #         "Bilgiler",
    #         {
    #             "classes": ["collapse"],
    #             "fields": [field.name for field in model._meta.concrete_fields if field.name not in ('id', 'edited', 'created')],
    #         },
    #     ),
    # ]

class PainInline(NestedStackedInline):
    model = Pain
    extra = 1
    # classes = ('stacked_collapse', 'collapsed',) çalışmadı
    # fieldsets = [
    #     (
    #         "Bilgiler",
    #         {
    #             "classes": ["collapse"],
    #             "fields": [field.name for field in model._meta.concrete_fields if field.name not in ('id', 'edited', 'created')],
    #         },
    #     ),
    # ]
    # classes=('collapse','collapsed')

    inlines = [
        PainScaleInline,
        PainPlaceInline,
        PainSeverityInline,
        PainFrequencyInline,
        PainNatureInline,
        PainFactorAffectingInline,
        PainTargetedLevelInline,
    ]

@admin.register(Pain)
class PainAdmin(DjangoObjectActions, admin.ModelAdmin):
    @action(
        label="Yazdır",
        # description="Geçerli Kaydı Yazdırmak için Yeni Pencere açılır."
    )
    def print(self, request, obj):
        # from django.http import HttpResponseRedirect
        # return HttpResponseRedirect(f'https://google.com')
        pass

    change_actions = ("print",)
    
    list_display = ("id", "patient", "edited", "created")
    list_display_links = ("id", "patient")

    # readonly_fields=("patient",)
    # list_editable = ('fileNumber',)
    search_fields = ('patient',)
    
    autocomplete_fields = ('patient',)

    inlines = [
        PainScaleInline,
        PainPlaceInline,
        PainSeverityInline,
        PainFrequencyInline,
        PainNatureInline,
        PainFactorAffectingInline,
        PainTargetedLevelInline,
    ]
