from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from genotip._model.bed import Bed
from form._form.observation import (
    Observation_Form,
    ObservationPageOneDetail_Inline,
    ObservationPageTwoDetail_Inline,
    ObservationTracking_PTaPTT_Inline,
    ObservationTracking_Hemogram_Inline,
    ObservationTracking_BreathingExercise_Inline,
    ObservationTracking_CVP_Inline,
    ObservationTracking_SteamTreatment_Inline,
    ObservationTracking_Aspiration_Inline,
    ObservationTracking_EKG_Inline,
    ObservationTracking_SandBagApplication_Inline,
    ObservationTracking_IceBagApplication_Inline,
    ObservationTracking_ColdHotApplication_Inline,
    ObservationTracking_GodePlus_Inline,
    ObservationTracking_GodePlusPlus_Inline,
    ObservationTracking_GodePlusPlusPlus_Inline,
    ObservationTracking_RadiologicalExamination_Inline,
    ObservationInsertionOpening_Inline,
    ObservationNote_Inline,

)
from form._model.observation import (
    Observation,
    ObservationPageOneDetail,
    ObservationPageTwoDetail,
    ObservationTracking_PTaPTT,
    ObservationTracking_Hemogram,
    ObservationTracking_BreathingExercise,
    ObservationTracking_CVP,
    ObservationTracking_SteamTreatment,
    ObservationTracking_Aspiration,
    ObservationTracking_EKG,
    ObservationTracking_SandBagApplication,
    ObservationTracking_IceBagApplication,
    ObservationTracking_ColdHotApplication,
    ObservationTracking_GodePlus,
    ObservationTracking_GodePlusPlus,
    ObservationTracking_GodePlusPlusPlus,
    ObservationTracking_RadiologicalExamination,
    ObservationInsertionOpening,
    ObservationNote,
)
from django.contrib import messages

from extra_views import CreateWithInlinesView, UpdateWithInlinesView
from django.urls import reverse_lazy


class Observation_CreateView(CreateWithInlinesView):
    model = Observation
    form_class = Observation_Form
    inlines = [
        ObservationPageOneDetail_Inline,
        ObservationPageTwoDetail_Inline,
        ObservationTracking_PTaPTT_Inline,
        ObservationTracking_Hemogram_Inline,
        ObservationTracking_BreathingExercise_Inline,
        ObservationTracking_CVP_Inline,
        ObservationTracking_SteamTreatment_Inline,
        ObservationTracking_Aspiration_Inline,
        ObservationTracking_EKG_Inline,
        ObservationTracking_SandBagApplication_Inline,
        ObservationTracking_IceBagApplication_Inline,
        ObservationTracking_ColdHotApplication_Inline,
        ObservationTracking_GodePlus_Inline,
        ObservationTracking_GodePlusPlus_Inline,
        ObservationTracking_GodePlusPlusPlus_Inline,
        ObservationTracking_RadiologicalExamination_Inline,
        ObservationInsertionOpening_Inline,
        ObservationNote_Inline,
    ]
    template_name = "form/observation/observation.html"

    def get_context_data(self, **kwargs):
        # print(self.kwargs)
        data = super().get_context_data(**kwargs)
        data['bed'] = get_object_or_404(Bed, pk=self.kwargs["bed_id"])
        return data

    def get_initial(self):
        print(self.kwargs)
        initial = super().get_initial()
        bed = get_object_or_404(Bed, pk=self.kwargs["bed_id"])
        initial["bed"] = bed
        initial["service"] = bed.service
        initial["user"] = self.request.user
        return initial

    def get_success_url(self):
        bed = get_object_or_404(Bed, pk=self.kwargs["bed_id"])
        return reverse_lazy("bed_detail", kwargs={"bed_id": bed.id})


class Observation_UpdateView(UpdateWithInlinesView):
    model = Observation
    form_class = Observation_Form
    inlines = [
        ObservationPageOneDetail_Inline,
        ObservationPageTwoDetail_Inline,
        ObservationTracking_PTaPTT_Inline,
        ObservationTracking_Hemogram_Inline,
        ObservationTracking_BreathingExercise_Inline,
        ObservationTracking_CVP_Inline,
        ObservationTracking_SteamTreatment_Inline,
        ObservationTracking_Aspiration_Inline,
        ObservationTracking_EKG_Inline,
        ObservationTracking_SandBagApplication_Inline,
        ObservationTracking_IceBagApplication_Inline,
        ObservationTracking_ColdHotApplication_Inline,
        ObservationTracking_GodePlus_Inline,
        ObservationTracking_GodePlusPlus_Inline,
        ObservationTracking_GodePlusPlusPlus_Inline,
        ObservationTracking_RadiologicalExamination_Inline,
        ObservationInsertionOpening_Inline,
        ObservationNote_Inline,
    ]
    template_name = "form/observation/observation.html"
    pk_url_kwarg = "observation_id"

    def get_context_data(self, **kwargs):
        # print(self.kwargs)
        data = super().get_context_data(**kwargs)
        data['bed'] = get_object_or_404(Bed, pk=self.kwargs["bed_id"])
        return data

    def get_success_url(self):
        bed = get_object_or_404(Bed, pk=self.kwargs["bed_id"])
        return reverse_lazy("bed_detail", kwargs={"bed_id": bed.id})


@login_required(login_url="/login/")
def observation_print(request, bed_id, observation_id):
    observation = get_object_or_404(Observation, pk=observation_id)
    observation_pageonedetails = ObservationPageOneDetail.objects.filter(observation=observation)
    observation_pagetwodetails = ObservationPageTwoDetail.objects.filter(observation=observation)
    observation_tracking_ptaptts = ObservationTracking_PTaPTT.objects.filter(observation=observation)
    observation_tracking_hemograms = ObservationTracking_Hemogram.objects.filter(observation=observation)
    observation_tracking_breathingexercises = ObservationTracking_BreathingExercise.objects.filter(observation=observation)
    observation_tracking_cvps = ObservationTracking_CVP.objects.filter(observation=observation)
    observation_tracking_steamtreatments = ObservationTracking_SteamTreatment.objects.filter(observation=observation)
    observation_tracking_aspirations = ObservationTracking_Aspiration.objects.filter(observation=observation)
    observation_tracking_ekgs = ObservationTracking_EKG.objects.filter(observation=observation)
    observation_tracking_sandbagapplications = ObservationTracking_SandBagApplication.objects.filter(observation=observation)
    observation_tracking_icebagapplications = ObservationTracking_IceBagApplication.objects.filter(observation=observation)
    observation_tracking_coldhotapplications = ObservationTracking_ColdHotApplication.objects.filter(observation=observation)
    observation_tracking_godeplusses = ObservationTracking_GodePlus.objects.filter(observation=observation)
    observation_tracking_godeplusplusses = ObservationTracking_GodePlusPlus.objects.filter(observation=observation)
    observation_tracking_godeplusplusplusses = ObservationTracking_GodePlusPlusPlus.objects.filter(observation=observation)
    observation_tracking_radiologicalexaminations = ObservationTracking_RadiologicalExamination.objects.filter(observation=observation)
    observation_insertionopenings = ObservationInsertionOpening.objects.filter(observation=observation)
    observation_notes = ObservationNote.objects.filter(observation=observation)

    context = {
        "observation": observation,
        "observation_pageonedetails": observation_pageonedetails,
        "observation_pagetwodetails": observation_pagetwodetails,
        "observation_tracking_ptaptts": observation_tracking_ptaptts,
        "observation_tracking_hemograms": observation_tracking_hemograms,
        "observation_tracking_breathingexercises": observation_tracking_breathingexercises,
        "observation_tracking_cvps": observation_tracking_cvps,
        "observation_tracking_steamtreatments": observation_tracking_steamtreatments,
        "observation_tracking_aspirations": observation_tracking_aspirations,
        "observation_tracking_ekgs": observation_tracking_ekgs,
        "observation_tracking_sandbagapplications": observation_tracking_sandbagapplications,
        "observation_tracking_icebagapplications": observation_tracking_icebagapplications,
        "observation_tracking_coldhotapplications": observation_tracking_coldhotapplications,
        "observation_tracking_godeplusses": observation_tracking_godeplusses,
        "observation_tracking_godeplusplusses": observation_tracking_godeplusplusses,
        "observation_tracking_godeplusplusplusses": observation_tracking_godeplusplusplusses,
        "observation_tracking_radiologicalexaminations": observation_tracking_radiologicalexaminations,
        "observation_insertionopenings": observation_insertionopenings,
        "observation_notes": observation_notes,

    }

    return render(request=request, template_name="form/observation/observation_print.html", context=context)
