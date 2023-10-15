from typing import Any
from django.contrib import admin
from django.http.request import HttpRequest

from django_object_actions import DjangoObjectActions, action

from form.model.pain import *


class PainScaleInline(admin.StackedInline):
    model = PainScale
    extra = 0
    max_num = 3
    classes = ("collapse-entry",)
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


class PainPlaceInline(admin.StackedInline):
    model = PainPlace
    extra = 0
    max_num = 3
    classes = ("collapse-entry",)
    # fieldsets = [
    #     (
    #         "Bilgiler",
    #         {
    #             "classes": ["collapse"],
    #             "fields": [field.name for field in model._meta.concrete_fields if field.name not in ('id', 'edited', 'created')],
    #         },
    #     ),
    # ]


class PainSeverityInline(admin.StackedInline):
    model = PainSeverity
    extra = 0
    max_num = 3
    classes = ("collapse-entry",)
    # fieldsets = [
    #     (
    #         "Bilgiler",
    #         {
    #             "classes": ["collapse"],
    #             "fields": [field.name for field in model._meta.concrete_fields if field.name not in ('id', 'edited', 'created')],
    #         },
    #     ),
    # ]


class PainFrequencyInline(admin.StackedInline):
    model = PainFrequency
    extra = 0
    max_num = 3
    classes = ("collapse-entry",)
    # fieldsets = [
    #     (
    #         "Bilgiler",
    #         {
    #             "classes": ["collapse"],
    #             "fields": [field.name for field in model._meta.concrete_fields if field.name not in ('id', 'edited', 'created')],
    #         },
    #     ),
    # ]


class PainNatureInline(admin.StackedInline):
    model = PainNature
    extra = 0
    max_num = 3
    classes = ("collapse-entry",)
    # fieldsets = [
    #     (
    #         "Bilgiler",
    #         {
    #             "classes": ["collapse"],
    #             "fields": [field.name for field in model._meta.concrete_fields if field.name not in ('id', 'edited', 'created')],
    #         },
    #     ),
    # ]


class PainFactorAffectingInline(admin.StackedInline):
    model = PainFactorAffecting
    extra = 0
    max_num = 3
    classes = ("collapse-entry",)
    # fieldsets = [
    #     (
    #         "Bilgiler",
    #         {
    #             "classes": ["collapse"],
    #             "fields": [field.name for field in model._meta.concrete_fields if field.name not in ('id', 'edited', 'created')],
    #         },
    #     ),
    # ]


class PainTargetedLevelInline(admin.StackedInline):
    model = PainTargetedLevel
    extra = 0
    max_num = 3
    classes = ("collapse-entry",)
    # fieldsets = [
    #     (
    #         "Bilgiler",
    #         {
    #             "classes": ["collapse"],
    #             "fields": [field.name for field in model._meta.concrete_fields if field.name not in ('id', 'edited', 'created')],
    #         },
    #     ),
    # ]


class PainInline(admin.StackedInline):
    model = Pain
    extra = 0
    max_num = 0
    can_delete = False
    classes = ("collapse-entry",)
    fields = [
        field.name
        for field in Pain._meta.fields
        if field.name not in ("id", "edited", "created", "user")
    ]
    # classes=('collapse','collapse-entry') çalışmadı
    # readonly_fields=[field.name for field in Pain._meta.fields]
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
        from django.shortcuts import render
        from django.db.models import Prefetch
        
        painScales=PainScale.objects.filter(pain=obj)
        painPlaces=PainPlace.objects.filter(pain=obj)
        painSeverities=PainSeverity.objects.filter(pain=obj)
        painFrequencies=PainFrequency.objects.filter(pain=obj)
        painNatures=PainNature.objects.filter(pain=obj)
        painFactorAffectings=PainFactorAffecting.objects.filter(pain=obj)
        painTargetedLevels=PainTargetedLevel.objects.filter(pain=obj)

        context = {
            "pain": obj,
            "painScales":painScales,
            "painPlaces":painPlaces,
            "painSeverities":painSeverities,
            "painFrequencies":painFrequencies,
            "painNatures":painNatures,
            "painFactorAffectings":painFactorAffectings,
            "painTargetedLevels":painTargetedLevels,
        }

        return render(
            request=request, template_name="form/admin/pain_print.html", context=context
        )
        # from django.http import HttpResponseRedirect
        # return HttpResponseRedirect(f'https://google.com')

    def save_model(self, request, obj, form, change):
        """
        Given a model instance save it to the database.
        """
        obj.user = request.user
        obj.save()

    # def has_add_permission(self, request: HttpRequest) -> bool:
    #     return False

    # def has_change_permission(self, request: HttpRequest, obj: Any | None = ...) -> bool:
    #     return False

    change_actions = ("print",)
    # changelist_actions=("print",)

    fields = [
        field.name
        for field in Pain._meta.fields
        if field.name not in ("id", "edited", "created", "user")
    ]
    list_display = [
        field.name
        for field in Pain._meta.fields
        if field.name in ("service", "edited", "created", "user")
    ]
    list_display_links = ("service",)
    search_fields = ("service",)

    save_on_top = True

    # change_form_template = "override/change_form.html"
    # change_list_template = "override/change_list.html"

    # readonly_fields=("patient",)
    # list_editable = ('fileNumber',)

    search_fields = ("service",)

    autocomplete_fields = ("service",)

    inlines = [
        PainScaleInline,
        PainPlaceInline,
        PainSeverityInline,
        PainFrequencyInline,
        PainNatureInline,
        PainFactorAffectingInline,
        PainTargetedLevelInline,
    ]
