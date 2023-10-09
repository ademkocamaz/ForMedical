from django.contrib import admin

from nested_inline.admin import NestedStackedInline, NestedModelAdmin
from django_object_actions import DjangoObjectActions, action

from form.model.pain import *

class PainScaleInline(NestedStackedInline):
    model = PainScale
    extra = 0
    max_num = 3
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
    extra = 0
    max_num = 3
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
    extra = 0
    max_num = 3
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
    extra = 0
    max_num = 3
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
    extra = 0
    max_num = 3
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
    extra = 0
    max_num = 3
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
    extra = 0
    max_num = 3
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
    extra = 0
    max_num = 0
    can_delete = False
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
        from form.form.pain import PainForm
        painForm = PainForm()
    
        context = {
            'pain_form': painForm,
        }
        return render(request=request, template_name='form/pain_print.html', context=context)
        # from django.http import HttpResponseRedirect
        # return HttpResponseRedirect(f'https://google.com')
        

    change_actions = ("print",)
    # changelist_actions=("print",)
    
    fields=[field.name for field in Pain._meta.fields if field.name not in ('id', 'edited', 'created')]
    list_display = [field.name for field in Pain._meta.fields if field.name not in ('id', 'edited', 'created')]
    list_display_links = ('service',)
    search_fields=('service', )

    save_on_top=True
    
    # change_form_template = "override/change_form.html"
    # change_list_template = "override/change_list.html"
    
    # readonly_fields=("patient",)
    # list_editable = ('fileNumber',)
    
    search_fields = ('service',)
    
    autocomplete_fields = ('service',)

    inlines = [
        PainScaleInline,
        PainPlaceInline,
        PainSeverityInline,
        PainFrequencyInline,
        PainNatureInline,
        PainFactorAffectingInline,
        PainTargetedLevelInline,
    ]