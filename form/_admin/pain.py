from typing import Any
from django.contrib import admin
from django.http.request import HttpRequest

from django_object_actions import DjangoObjectActions, action

from form._model.pain import *


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


class PainInterventionInline(admin.StackedInline):
    model = PainIntervention
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
        PainInterventionInline,
    ]


@admin.register(Pain)
class PainAdmin(DjangoObjectActions, admin.ModelAdmin):
    @action(
        label="Yazdır",
        # description="Geçerli Kaydı Yazdırmak için Yeni Pencere açılır."
    )
    def print(self, request, obj):
        from django.shortcuts import render
        
        pain = obj
        pain_scales = PainScale.objects.filter(pain=pain)
        pain_places = PainPlace.objects.filter(pain=pain)
        pain_severities = PainSeverity.objects.filter(pain=pain)
        pain_frequencies = PainFrequency.objects.filter(pain=pain)
        pain_natures = PainNature.objects.filter(pain=pain)
        pain_factor_affectings = PainFactorAffecting.objects.filter(pain=pain)
        pain_targeted_levels = PainTargetedLevel.objects.filter(pain=pain)
        pain_interventions = PainIntervention.objects.filter(pain=pain)

        context = {
            "pain": pain,
            "pain_scales": pain_scales,
            "pain_places": pain_places,
            "pain_severities": pain_severities,
            "pain_frequencies": pain_frequencies,
            "pain_natures": pain_natures,
            "pain_factor_affectings": pain_factor_affectings,
            "pain_targeted_levels": pain_targeted_levels,
            "pain_interventions": pain_interventions,
        }

        return render(request=request, template_name='form/pain/pain_print.html', context=context)
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
        if field.name not in ("id", "edited", "created")
    ]
    list_display = [
        field.name
        for field in Pain._meta.fields
        if field.name in ("bed", "service", "edited", "created", "user")
    ]
    list_display_links = ("service", "bed")
    search_fields = ("service", "bed")

    readonly_fields = ("bed", "service", "user")

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
        PainInterventionInline,
    ]
