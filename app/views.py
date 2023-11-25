from django.forms.models import BaseModelForm
from django.http import HttpResponse
from extra_views import CreateWithInlinesView, UpdateWithInlinesView
from django.views.generic.edit import CreateView
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from genotip._model.service import ServiceDefinition
from genotip._model.bed import Bed
from form._form.pain import *
from django.contrib import messages
from django.urls import reverse_lazy
# Create your views here.


@login_required(login_url="/login/")
def index(request):
    messages.add_message(request, messages.WARNING, 'Hoşgeldiniz.')
    service_definition = ServiceDefinition.objects.get(
        id=request.session["service"])
    context = {
        "service_definition": service_definition,
        "beds": Bed.objects.filter(service_definition=service_definition).order_by("oda")
    }

    return render(request=request, template_name='app/index.html', context=context)


@login_required(login_url="/login/")
def bed_detail(request, bed_id):
    bed = get_object_or_404(Bed, pk=bed_id)
    service_definition = ServiceDefinition.objects.get(
        id=request.session["service"])

    pain_forms = Pain.objects.filter(bed=bed, service=bed.service)

    context = {
        "service_definition": service_definition,
        "bed": bed,
        "pain_forms": pain_forms,
    }

    return render(request=request, template_name='app/bed_detail.html', context=context)


@login_required(login_url="/login/")
def pain(request, bed_id):
    bed = get_object_or_404(Bed, pk=bed_id)

    if request.method == 'POST':
        pain_form = PainForm(request.POST)
        if pain_form.is_valid():
            pain_form.save()
            messages.add_message(request, messages.WARNING,
                                 'Ağrı Formu eklendi.')
        else:
            messages.add_message(request, messages.ERROR,
                                 pain_form.Meta.model._meta.verbose_name)
            for error in list(pain_form.errors.values()):
                messages.add_message(request, messages.ERROR, error)

        return redirect('bed_detail', bed.id)

    pain_form = PainForm(
        initial={"bed": bed, "service": bed.service, "user": request.user}
    )

    # pain_scale_formset = PainScaleFormSet()

    context = {
        'bed': bed,
        'pain_form': pain_form,
        # 'pain_scale_formset': pain_scale_formset
    }

    return render(request=request, template_name='form/pain/pain.html', context=context)


@login_required(login_url="/login/")
def pain_update(request, bed_id, pain_id):
    bed = get_object_or_404(Bed, pk=bed_id)
    pain = get_object_or_404(Pain, pk=pain_id)

    if request.method == 'POST':

        pain_form_updated = PainForm(request.POST, instance=pain)
        if pain_form_updated.is_valid():
            pain_form_updated.save()
        # else:
        #     messages.add_message(request, messages.ERROR,
        #                          pain_form_updated._meta.model._meta.verbose_name)
        #     for error in pain_form_updated.errors:
        #         messages.add_message(request, messages.ERROR, error)

        pain_scale_formset = PainScaleFormSet(request.POST, instance=pain)

        if pain_scale_formset.is_valid():
            pain_scale_formset.save()
        # else:
        #     messages.add_message(request, messages.ERROR,
        #                          pain_scale_formset.model._meta.verbose_name)
        #     for error in pain_scale_formset.errors:
        #         messages.add_message(request, messages.ERROR, error)

        pain_place_formset = PainPlaceFormSet(request.POST, instance=pain)
        if pain_place_formset.is_valid():
            pain_place_formset.save()
        # else:
        #     messages.add_message(request, messages.ERROR,
        #                          pain_place_formset.model._meta.verbose_name)
        #     for error in pain_place_formset.errors:
        #         messages.add_message(request, messages.ERROR, error)

        pain_severity_formset = PainSeverityFormSet(
            request.POST, instance=pain)
        if pain_severity_formset.is_valid():
            pain_severity_formset.save()
        # else:
        #     messages.add_message(request, messages.ERROR,
        #                          pain_severity_formset.model._meta.verbose_name)
        #     for error in pain_severity_formset.errors:
        #         messages.add_message(request, messages.ERROR, error)

        pain_frequency_formset = PainFrequencyFormSet(
            request.POST, instance=pain)
        if pain_frequency_formset.is_valid():
            pain_frequency_formset.save()
        # else:
        #     messages.add_message(request, messages.ERROR,
        #                          pain_frequency_formset.model._meta.verbose_name)
        #     for error in pain_frequency_formset.errors:
        #         messages.add_message(request, messages.ERROR, error)

        pain_nature_formset = PainNatureFormSet(request.POST, instance=pain)
        if pain_nature_formset.is_valid():
            pain_nature_formset.save()
        # else:
        #     messages.add_message(request, messages.ERROR,
        #                          pain_nature_formset.model._meta.verbose_name)
        #     for error in pain_nature_formset.errors:
        #         messages.add_message(request, messages.ERROR, error)

        pain_factor_affecting_formset = PainFactorAffectingFormSet(
            request.POST, instance=pain)
        if pain_factor_affecting_formset.is_valid():
            pain_factor_affecting_formset.save()
        # else:
        #     messages.add_message(
        #         request, messages.ERROR, pain_factor_affecting_formset.model._meta.verbose_name)
        #     for error in pain_factor_affecting_formset.errors:
        #         messages.add_message(request, messages.ERROR, error)

        pain_targeted_level_formset = PainTargetedLevelFormSet(
            request.POST, instance=pain)
        if pain_targeted_level_formset.is_valid():
            pain_targeted_level_formset.save()
        # else:
        #     messages.add_message(
        #         request, messages.ERROR, pain_targeted_level_formset.model._meta.verbose_name)
        #     for error in pain_targeted_level_formset.errors:
        #         messages.add_message(request, messages.ERROR, error)

        pain_intervention_formset = PainInterventionFormSet(
            request.POST, instance=pain)
        if pain_intervention_formset.is_valid():
            pain_intervention_formset.save()
        # else:
        #     messages.add_message(
        #         request, messages.ERROR, pain_intervention_formset.model._meta.verbose_name)
        #     for error in pain_intervention_formset.errors:
        #         messages.add_message(request, messages.ERROR, error)

        # messages.add_message(request, messages.WARNING, 'Ağrı Formu eklendi.')

        # return redirect('bed_detail', bed.id)

    pain_form = PainForm(instance=pain)

    pain_scale_formset = PainScaleFormSet(instance=pain)
    pain_scale_formset_helper = PainScaleFormSetHelper()

    pain_place_formset = PainPlaceFormSet(instance=pain)
    pain_place_formset_helper = PainPlaceFormSetHelper()

    pain_severity_formset = PainSeverityFormSet(instance=pain)
    pain_severity_formset_helper = PainSeverityFormSetHelper()

    pain_frequency_formset = PainFrequencyFormSet(instance=pain)
    pain_frequency_formset_helper = PainFrequencyFormSetHelper()

    pain_nature_formset = PainNatureFormSet(instance=pain)
    pain_nature_formset_helper = PainNatureFormSetHelper()

    pain_factor_affecting_formset = PainFactorAffectingFormSet(
        instance=pain)
    pain_factor_affecting_formset_helper = PainFactorAffectingFormSetHelper()

    pain_targeted_level_formset = PainTargetedLevelFormSet(instance=pain)
    pain_targeted_level_formset_helper = PainTargetedLevelFormSetHelper()

    pain_intervention_formset = PainInterventionFormSet(instance=pain)
    pain_intervention_formset_helper = PainInterventionFormSetHelper()

    context = {
        'bed': bed,
        'pain': pain,
        'pain_form': pain_form,

        'pain_scale_formset': pain_scale_formset,
        'pain_scale_formset_helper': pain_scale_formset_helper,

        'pain_place_formset': pain_place_formset,
        'pain_place_formset_helper': pain_place_formset_helper,

        'pain_severity_formset': pain_severity_formset,
        'pain_severity_formset_helper': pain_severity_formset_helper,

        'pain_frequency_formset': pain_frequency_formset,
        'pain_frequency_formset_helper': pain_frequency_formset_helper,

        'pain_nature_formset': pain_nature_formset,
        'pain_nature_formset_helper': pain_nature_formset_helper,

        'pain_factor_affecting_formset': pain_factor_affecting_formset,
        'pain_factor_affecting_formset_helper': pain_factor_affecting_formset_helper,

        'pain_targeted_level_formset': pain_targeted_level_formset,
        'pain_targeted_level_formset_helper': pain_targeted_level_formset_helper,

        'pain_intervention_formset': pain_intervention_formset,
        'pain_intervention_formset_helper': pain_intervention_formset_helper,
    }

    return render(request=request, template_name='form/pain/pain_update.html', context=context)


@login_required(login_url="/login/")
def pain_print(request, bed_id, pain_id):
    pain = get_object_or_404(Pain, pk=pain_id)

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


class PainCreateView(CreateView):

    model = Pain
    form_class = PainForm
    template_name = "form/pain/pain.html"

    def get_context_data(self, **kwargs):
        print(self.kwargs)
        data = super(PainCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            # data['pain_scale'] = PainScaleFormSet(self.request.POST)
            data['bed'] = get_object_or_404(Bed, pk=self.kwargs["bed_id"])
        else:
            # data['pain_scale'] = PainScaleFormSet()
            data['bed'] = get_object_or_404(Bed, pk=self.kwargs["bed_id"])
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        # pain_scale = context['pain_scale']
        # with transaction.atomic():
        form.instance.bed = context["bed"]
        form.instance.service = form.instance.bed.service
        form.instance.user = self.request.user
        if form.is_valid():
            form.save()
            messages.add_message(self.request, messages.WARNING,
                                 'Ağrı Formu eklendi.')
        else:
            messages.add_message(self.request, messages.ERROR,
                                 form.Meta.model._meta.verbose_name)
            for error in list(form.errors.values()):
                messages.add_message(self.request, messages.ERROR, error)
            # self.object = form.save()

            # if pain_scale.is_valid():
            #     pain_scale.instance = self.object
            #     pain_scale.save()
        return super(PainCreateView, self).form_valid(form)


# class PainScaleInline(InlineFormSetFactory):
#     model = PainScale
#     # form_class = PainScaleForm
#     fields="__all__"
#     factory_kwargs = {
#         'extra': 1,
#         'max_num': 3,
#         'can_delete': True
#     }


class PainCreateTestView(CreateWithInlinesView):
    model = Pain
    form_class = PainForm
    inlines = [PainScaleInline, PainPlaceInline]
    template_name = "form/pain/pain_test.html"
    index_url = reverse_lazy("index")
    success_url = reverse_lazy("bed_detail")

    def get_context_data(self, **kwargs):
        print(self.kwargs)
        data = super().get_context_data(**kwargs)
        data['bed'] = get_object_or_404(Bed, pk=self.kwargs["bed_id"])
        return data

    # def get_success_url(self):
    #     return self.object.get_absolute_url()

    def form_valid(self, form):
        context = self.get_context_data()

        form.instance.bed = context["bed"]
        form.instance.service = form.instance.bed.service
        form.instance.user = self.request.user

        if form.is_valid():
            form.save()
            messages.add_message(self.request, messages.WARNING,
                                 'Ağrı Formu eklendi.')
        else:
            messages.add_message(self.request, messages.ERROR,
                                 form.Meta.model._meta.verbose_name)
            for error in list(form.errors.values()):
                messages.add_message(self.request, messages.ERROR, error)

        return super().form_valid(form)


class PainUpdateTestView(UpdateWithInlinesView):
    model = Pain
    form_class = PainForm
    inlines = [PainScaleInline, PainPlaceInline]
    template_name = "form/pain/pain_test.html"

    def get_context_data(self, **kwargs):
        print(self.kwargs)
        data = super().get_context_data(**kwargs)
        data['bed'] = get_object_or_404(Bed, pk=self.kwargs["bed_id"])
        data['pain'] = get_object_or_404(Pain, pk=self.kwargs["pain_id"])
        return data

    def get_success_url(self):
        return self.object.get_absolute_url()
