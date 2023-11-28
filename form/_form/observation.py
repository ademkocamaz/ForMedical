from django import forms
from django.forms import inlineformset_factory

from form._model.observation import (
    Observation,
    ObservationPageOneDetails,
    ObservationPageTwoDetails,
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
from crispy_forms.layout import Field, Row, Column, Layout, Fieldset, Div, Submit
from crispy_forms.helper import FormHelper

from crispy_formset_modal.helper import ModalEditFormHelper
from crispy_formset_modal.layout import ModalEditLayout, ModalEditFormsetLayout

from extra_views import InlineFormSetFactory


class Observation_Form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.layout = Layout(
            Field("bed"),
            Field("service"),
            Field("user"),

            # Row(
            #     Column(
            #         Field("date"),
            #     ),
            #     Column(
            #         Field("doctor"),
            #     ),
            #     Column(
            #         Field("section"),
            #     ),
            # ),

            Row(
                Column(
                    Field("kilogram"),
                ),
                Column(
                    Field("height"),
                ),
                Column(
                    Field("preliminary_diagnosis"),
                ),
            ),

            Fieldset(
                ObservationPageOneDetails._meta.verbose_name_plural,
                ModalEditFormsetLayout(
                    "ObservationPageOneDetails_Inline",
                    # list_display=[
                    #     field.name
                    #     for field in ObservationPageOneDetails._meta.fields
                    #     if field.name not in ("id", "edited", "created")
                    # ]
                ),
            ),

            Fieldset(
                ObservationPageTwoDetails._meta.verbose_name_plural,
                ModalEditFormsetLayout(
                    "ObservationPageTwoDetails_Inline",
                ),
            ),

            Fieldset(
                ObservationTracking_PTaPTT._meta.verbose_name_plural,
                ModalEditFormsetLayout(
                    "ObservationTracking_PTaPTT_Inline",
                ),
            ),

            Fieldset(
                ObservationTracking_Hemogram._meta.verbose_name_plural,
                ModalEditFormsetLayout(
                    "ObservationTracking_Hemogram_Inline",
                ),
            ),

            Fieldset(
                ObservationTracking_BreathingExercise._meta.verbose_name_plural,
                ModalEditFormsetLayout(
                    "ObservationTracking_BreathingExercise_Inline",
                ),
            ),

            Fieldset(
                ObservationTracking_CVP._meta.verbose_name_plural,
                ModalEditFormsetLayout(
                    "ObservationTracking_CVP_Inline",
                ),
            ),

            Fieldset(
                ObservationTracking_SteamTreatment._meta.verbose_name_plural,
                ModalEditFormsetLayout(
                    "ObservationTracking_SteamTreatment_Inline",
                ),
            ),

            Fieldset(
                ObservationTracking_Aspiration._meta.verbose_name_plural,
                ModalEditFormsetLayout(
                    "ObservationTracking_Aspiration_Inline",
                ),
            ),

            Fieldset(
                ObservationTracking_EKG._meta.verbose_name_plural,
                ModalEditFormsetLayout(
                    "ObservationTracking_EKG_Inline",
                ),
            ),

            Fieldset(
                ObservationTracking_SandBagApplication._meta.verbose_name_plural,
                ModalEditFormsetLayout(
                    "ObservationTracking_SandBagApplication_Inline",
                ),
            ),

            Fieldset(
                ObservationTracking_IceBagApplication._meta.verbose_name_plural,
                ModalEditFormsetLayout(
                    "ObservationTracking_IceBagApplication_Inline",
                ),
            ),

            Fieldset(
                ObservationTracking_ColdHotApplication._meta.verbose_name_plural,
                ModalEditFormsetLayout(
                    "ObservationTracking_ColdHotApplication_Inline",
                ),
            ),

            Fieldset(
                ObservationTracking_GodePlus._meta.verbose_name_plural,
                ModalEditFormsetLayout(
                    "ObservationTracking_GodePlus_Inline",
                ),
            ),

            Fieldset(
                ObservationTracking_GodePlusPlus._meta.verbose_name_plural,
                ModalEditFormsetLayout(
                    "ObservationTracking_GodePlusPlus_Inline",
                ),
            ),

            Fieldset(
                ObservationTracking_GodePlusPlusPlus._meta.verbose_name_plural,
                ModalEditFormsetLayout(
                    "ObservationTracking_GodePlusPlusPlus_Inline",
                ),
            ),

            Fieldset(
                ObservationTracking_RadiologicalExamination._meta.verbose_name_plural,
                ModalEditFormsetLayout(
                    "ObservationTracking_RadiologicalExamination_Inline",
                ),
            ),

            Fieldset(
                ObservationInsertionOpening._meta.verbose_name_plural,
                ModalEditFormsetLayout(
                    "ObservationInsertionOpening_Inline",
                ),
            ),

            Fieldset(
                ObservationNote._meta.verbose_name_plural,
                ModalEditFormsetLayout(
                    "ObservationNote_Inline",
                ),
            ),

            Div(
                Submit("submit", "Kaydet", css_class="btn btn-lg btn-warning"),
                css_class="d-flex justify-content-center mb-3",
            ),
        )

    class Meta:
        model = Observation
        fields = "__all__"
        widgets = {
            "bed": forms.HiddenInput,
            "service": forms.HiddenInput,
            "user": forms.HiddenInput,
        }


class ObservationPageOneDetails_Form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = ModalEditFormHelper()
        self.helper.layout = ModalEditLayout(
            Row(
                Column(
                    Field("date"),
                ),
                Column(
                    Field("body_temperature"),
                ),
            ),
            Row(
                Column(
                    Field("pulse"),
                ),
                Column(
                    Field("blood_pressure"),
                ),
            ),
            Row(
                Column(
                    Field("number_of_breaths"),
                ),
                Column(
                    Field("oxygen_saturation"),
                ),
            ),
        )

    class Meta:
        model = ObservationPageOneDetails
        fields = "__all__"
        widgets = {
            "date": forms.DateTimeInput(format=('%d.%m.%Y %H:%M:%S'), attrs={'type': 'datetime-local'}),
        }


class ObservationPageOneDetails_Inline(InlineFormSetFactory):
    model = ObservationPageOneDetails
    form_class = ObservationPageOneDetails_Form
    fields = "__all__"
    factory_kwargs = {"extra": 0, "max_num": 30}


class ObservationPageTwoDetails_Form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = ModalEditFormHelper()
        self.helper.layout = ModalEditLayout(
            Row(
                Column(
                    Field("oral_care"),
                ),
                Column(
                    Field("hand_facial_care"),
                ),
            ),
            Row(
                Column(
                    Field("body_bath"),
                ),
                Column(
                    Field("perineal_care"),
                ),
            ),
            Row(
                Column(
                    Field("toenail_care"),
                ),
                Column(
                    Field("dressing_change"),
                ),
            ),
        )

    class Meta:
        model = ObservationPageTwoDetails
        fields = "__all__"
        widgets = {
            "oral_care": forms.DateTimeInput(format=('%d.%m.%Y %H:%M:%S'), attrs={'type': 'datetime-local'}),
            "hand_facial_care": forms.DateTimeInput(format=('%d.%m.%Y %H:%M:%S'), attrs={'type': 'datetime-local'}),
            "body_bath": forms.DateTimeInput(format=('%d.%m.%Y %H:%M:%S'), attrs={'type': 'datetime-local'}),
            "perineal_care": forms.DateTimeInput(format=('%d.%m.%Y %H:%M:%S'), attrs={'type': 'datetime-local'}),
            "toenail_care": forms.DateTimeInput(format=('%d.%m.%Y %H:%M:%S'), attrs={'type': 'datetime-local'}),
            "dressing_change": forms.DateTimeInput(format=('%d.%m.%Y %H:%M:%S'), attrs={'type': 'datetime-local'}),
        }


class ObservationPageTwoDetails_Inline(InlineFormSetFactory):
    model = ObservationPageTwoDetails
    form_class = ObservationPageTwoDetails_Form
    fields = "__all__"
    factory_kwargs = {"extra": 0, "max_num": 1}

#region ObservationTracking

class ObservationTracking_BaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = ModalEditFormHelper()
        self.helper.layout = ModalEditLayout(
            Row(
                Column(
                    Field("planning"),
                ),
                Column(
                    Field("implementation"),
                ),
            ),
        )

    class Meta:
        model = None
        fields = "__all__"
        widgets = {
            "planning": forms.DateTimeInput(format=('%d.%m.%Y %H:%M:%S'), attrs={'type': 'datetime-local'}),
            "implementation": forms.DateTimeInput(format=('%d.%m.%Y %H:%M:%S'), attrs={'type': 'datetime-local'}),
        }


class ObservationTracking_BaseInline(InlineFormSetFactory):
    model = None
    form_class = None
    fields = "__all__"
    factory_kwargs = {"extra": 0, "max_num": 10}


class ObservationTracking_PTaPTT_Form(ObservationTracking_BaseForm):
    class Meta(ObservationTracking_BaseForm.Meta):
        model = ObservationTracking_PTaPTT


class ObservationTracking_PTaPTT_Inline(ObservationTracking_BaseInline):
    model = ObservationTracking_PTaPTT
    form_class = ObservationTracking_PTaPTT_Form


class ObservationTracking_Hemogram_Form(ObservationTracking_BaseForm):
    class Meta(ObservationTracking_BaseForm.Meta):
        model = ObservationTracking_Hemogram


class ObservationTracking_Hemogram_Inline(ObservationTracking_BaseInline):
    model = ObservationTracking_Hemogram
    form_class = ObservationTracking_Hemogram_Form


class ObservationTracking_BreathingExercise_Form(ObservationTracking_BaseForm):
    class Meta(ObservationTracking_BaseForm.Meta):
        model = ObservationTracking_BreathingExercise


class ObservationTracking_BreathingExercise_Inline(ObservationTracking_BaseInline):
    model = ObservationTracking_BreathingExercise
    form_class = ObservationTracking_BreathingExercise_Form


class ObservationTracking_CVP_Form(ObservationTracking_BaseForm):
    class Meta(ObservationTracking_BaseForm.Meta):
        model = ObservationTracking_CVP


class ObservationTracking_CVP_Inline(ObservationTracking_BaseInline):
    model = ObservationTracking_CVP
    form_class = ObservationTracking_CVP_Form


class ObservationTracking_SteamTreatment_Form(ObservationTracking_BaseForm):
    class Meta(ObservationTracking_BaseForm.Meta):
        model = ObservationTracking_SteamTreatment


class ObservationTracking_SteamTreatment_Inline(ObservationTracking_BaseInline):
    model = ObservationTracking_SteamTreatment
    form_class = ObservationTracking_SteamTreatment_Form


class ObservationTracking_Aspiration_Form(ObservationTracking_BaseForm):
    class Meta(ObservationTracking_BaseForm.Meta):
        model = ObservationTracking_Aspiration


class ObservationTracking_Aspiration_Inline(ObservationTracking_BaseInline):
    model = ObservationTracking_Aspiration
    form_class = ObservationTracking_Aspiration_Form


class ObservationTracking_EKG_Form(ObservationTracking_BaseForm):
    class Meta(ObservationTracking_BaseForm.Meta):
        model = ObservationTracking_EKG


class ObservationTracking_EKG_Inline(ObservationTracking_BaseInline):
    model = ObservationTracking_EKG
    form_class = ObservationTracking_EKG_Form


class ObservationTracking_SandBagApplication_Form(ObservationTracking_BaseForm):
    class Meta(ObservationTracking_BaseForm.Meta):
        model = ObservationTracking_SandBagApplication


class ObservationTracking_SandBagApplication_Inline(ObservationTracking_BaseInline):
    model = ObservationTracking_SandBagApplication
    form_class = ObservationTracking_SandBagApplication_Form


class ObservationTracking_IceBagApplication_Form(ObservationTracking_BaseForm):
    class Meta(ObservationTracking_BaseForm.Meta):
        model = ObservationTracking_IceBagApplication


class ObservationTracking_IceBagApplication_Inline(ObservationTracking_BaseInline):
    model = ObservationTracking_IceBagApplication
    form_class = ObservationTracking_IceBagApplication_Form


class ObservationTracking_ColdHotApplication_Form(ObservationTracking_BaseForm):
    class Meta(ObservationTracking_BaseForm.Meta):
        model = ObservationTracking_ColdHotApplication


class ObservationTracking_ColdHotApplication_Inline(ObservationTracking_BaseInline):
    model = ObservationTracking_ColdHotApplication
    form_class = ObservationTracking_ColdHotApplication_Form


class ObservationTracking_GodePlus_Form(ObservationTracking_BaseForm):
    class Meta(ObservationTracking_BaseForm.Meta):
        model = ObservationTracking_GodePlus


class ObservationTracking_GodePlus_Inline(ObservationTracking_BaseInline):
    model = ObservationTracking_GodePlus
    form_class = ObservationTracking_GodePlus_Form


class ObservationTracking_GodePlusPlus_Form(ObservationTracking_BaseForm):
    class Meta(ObservationTracking_BaseForm.Meta):
        model = ObservationTracking_GodePlusPlus


class ObservationTracking_GodePlusPlus_Inline(ObservationTracking_BaseInline):
    model = ObservationTracking_GodePlusPlus
    form_class = ObservationTracking_GodePlusPlus_Form


class ObservationTracking_GodePlusPlusPlus_Form(ObservationTracking_BaseForm):
    class Meta(ObservationTracking_BaseForm.Meta):
        model = ObservationTracking_GodePlusPlusPlus


class ObservationTracking_GodePlusPlusPlus_Inline(ObservationTracking_BaseInline):
    model = ObservationTracking_GodePlusPlusPlus
    form_class = ObservationTracking_GodePlusPlusPlus_Form


class ObservationTracking_RadiologicalExamination_Form(ObservationTracking_BaseForm):
    class Meta(ObservationTracking_BaseForm.Meta):
        model = ObservationTracking_RadiologicalExamination


class ObservationTracking_RadiologicalExamination_Inline(ObservationTracking_BaseInline):
    model = ObservationTracking_RadiologicalExamination
    form_class = ObservationTracking_RadiologicalExamination_Form

#endregion

class ObservationInsertionOpening_Form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = ModalEditFormHelper()
        self.helper.layout = ModalEditLayout(
            Row(
                Column(
                    Field("cvp_catheter"),
                ),
                Column(
                    Field("urinary_catheter"),
                ),
            ),
            Row(
                Column(
                    Field("peripheral_catheter"),
                ),
                Column(
                    Field("urinary_catheter"),
                ),
            ),
        )
    class Meta:
        model = ObservationInsertionOpening
        fields = "__all__"
        widgets = {
            "cvp_catheter": forms.DateTimeInput(format=('%d.%m.%Y %H:%M:%S'), attrs={'type': 'datetime-local'}),
            "urinary_catheter": forms.DateTimeInput(format=('%d.%m.%Y %H:%M:%S'), attrs={'type': 'datetime-local'}),
            "peripheral_catheter": forms.DateTimeInput(format=('%d.%m.%Y %H:%M:%S'), attrs={'type': 'datetime-local'}),
            "urinary_catheter": forms.DateTimeInput(format=('%d.%m.%Y %H:%M:%S'), attrs={'type': 'datetime-local'}),
        }

class ObservationInsertionOpening_Inline(InlineFormSetFactory):
    model = ObservationInsertionOpening
    form_class = ObservationInsertionOpening_Form
    fields = "__all__"
    factory_kwargs = {"extra": 0, "max_num": 3}

class ObservationNote_Form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = ModalEditFormHelper()
        self.helper.layout = ModalEditLayout(
            Field("note"),
        )
    class Meta:
        model = ObservationNote
        fields = "__all__"

class ObservationNote_Inline(InlineFormSetFactory):
    model = ObservationNote
    form_class = ObservationNote_Form
    fields = "__all__"
    factory_kwargs = {"extra": 0, "max_num": 20}

