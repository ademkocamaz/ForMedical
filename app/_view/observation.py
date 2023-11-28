from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from genotip._model.bed import Bed
from form._form.observation import (
    Observation_Form, 
    ObservationPageOneDetails_Inline, 
    ObservationPageTwoDetails_Inline,
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
from form._model.observation import Observation
from django.contrib import messages

from extra_views import CreateWithInlinesView, UpdateWithInlinesView
from django.urls import reverse_lazy


class Observation_CreateView(CreateWithInlinesView):
    model = Observation
    form_class = Observation_Form
    inlines = [
        ObservationPageOneDetails_Inline,
        ObservationPageTwoDetails_Inline,
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
