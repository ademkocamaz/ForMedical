from extra_views import InlineFormSetFactory
from django import forms
from django.forms import inlineformset_factory

from form._model.pain import *
from crispy_forms.layout import *
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import InlineRadios

from crispy_formset_modal.helper import ModalEditFormHelper
from crispy_formset_modal.layout import ModalEditLayout, ModalEditFormsetLayout

# region PainScaleForm


class PainScaleForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = ModalEditFormHelper()
    #     self.helper.layout = ModalEditLayout(
    #         "pain",
    #         "description",
    #         "date",
    #     )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # if self.instance.pk:
        #     self.fields['description'].widget.attrs['readonly'] = True
        #     self.fields['date'].widget.attrs['readonly'] = True

        if self.instance.pk:
            for field in self.fields:
                # print(field)
                self.fields[field].widget.attrs["readonly"] = True

    class Meta:
        model = PainScale
        fields = "__all__"
        widgets = {
            #     # "date": forms.DateTimeInput(format=('%d.%m.%Y %H:%M:%S'), attrs={'type': 'datetime-local'})
            "date": forms.DateTimeInput(format=('%Y-%m-%dT%H:%M:%S'), attrs={'type': 'datetime-local'}),
        }


class PainScaleFormSetHelper(FormHelper):

    template = "bootstrap4/table_inline_formset.html"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.layout = Layout(
            Field("pain"),
            Field("description",),
            Field("date"),
        )
        
        self.add_input(
            Submit("submit", "Kaydet")
        )
        self.render_required_fields = True


PainScaleFormSet = inlineformset_factory(
    parent_model=Pain,
    model=PainScale,
    form=PainScaleForm,
    extra=1,
    max_num=3,
    can_delete=True,
)


class PainScaleInline(InlineFormSetFactory):
    model = PainScale
    form_class = PainScaleForm
    fields = "__all__"
    factory_kwargs = {"extra": 0, "max_num": 3}
# endregion

# region PainPlaceForm


class PainPlaceForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = ModalEditFormHelper()
    #     self.helper.layout = ModalEditLayout(
    #         "pain",
    #         "description",
    #         "date",
    #     )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance.pk:
            for field in self.fields:
                # print(field)
                self.fields[field].widget.attrs["readonly"] = True
    class Meta:
        model = PainPlace
        fields = "__all__"
        widgets = {
            "date": forms.DateTimeInput(format=('%Y-%m-%dT%H:%M:%S'), attrs={'type': 'datetime-local'}),
        }


class PainPlaceFormSetHelper(FormHelper):

    template = "bootstrap4/table_inline_formset.html"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.layout = Layout(
            Field("pain"),
            Field("description"),
            Field("date"),
        )
        self.add_input(
            Submit("submit", "Kaydet")
        )
        self.render_required_fields = True


PainPlaceFormSet = inlineformset_factory(
    parent_model=Pain,
    model=PainPlace,
    form=PainPlaceForm,
    extra=1,
    max_num=3,
    can_delete=True,
)


class PainPlaceInline(InlineFormSetFactory):
    model = PainPlace
    form_class = PainPlaceForm
    fields = "__all__"
    factory_kwargs = {"extra": 0, "max_num": 3}

# endregion

# region PainSeverityForm


class PainSeverityForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance.pk:
            for field in self.fields:
                # print(field)
                self.fields[field].widget.attrs["readonly"] = True
    class Meta:
        model = PainSeverity
        fields = "__all__"
        widgets = {
            "date": forms.DateTimeInput(format=('%Y-%m-%dT%H:%M:%S'), attrs={'type': 'datetime-local'}),
        }


class PainSeverityFormSetHelper(FormHelper):

    template = "bootstrap4/table_inline_formset.html"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.layout = Layout(
            Field("pain"),
            Field("description"),
            Field("date"),
        )
        self.add_input(
            Submit("submit", "Kaydet")
        )
        self.render_required_fields = True


PainSeverityFormSet = inlineformset_factory(
    parent_model=Pain,
    model=PainSeverity,
    form=PainSeverityForm,
    extra=1,
    max_num=3,
    can_delete=False,
)
# endregion

# region PainFrequencyForm


class PainFrequencyForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance.pk:
            for field in self.fields:
                # print(field)
                self.fields[field].widget.attrs["readonly"] = True
    class Meta:
        model = PainFrequency
        fields = "__all__"
        widgets = {
            "date": forms.DateTimeInput(format=('%Y-%m-%dT%H:%M:%S'), attrs={'type': 'datetime-local'}),
        }


class PainFrequencyFormSetHelper(FormHelper):

    template = "bootstrap4/table_inline_formset.html"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.layout = Layout(
            Field("pain"),
            Field("description"),
            Field("date"),
        )
        self.add_input(
            Submit("submit", "Kaydet")
        )
        self.render_required_fields = True


PainFrequencyFormSet = inlineformset_factory(
    parent_model=Pain,
    model=PainFrequency,
    form=PainFrequencyForm,
    extra=1,
    max_num=3,
    can_delete=False,
)
# endregion

# region PainNatureForm


class PainNatureForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance.pk:
            for field in self.fields:
                # print(field)
                self.fields[field].widget.attrs["readonly"] = True
    class Meta:
        model = PainNature
        fields = "__all__"
        widgets = {
            "date": forms.DateTimeInput(format=('%Y-%m-%dT%H:%M:%S'), attrs={'type': 'datetime-local'}),
        }


class PainNatureFormSetHelper(FormHelper):

    template = "bootstrap4/table_inline_formset.html"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.layout = Layout(
            Field("pain"),
            Field("description"),
            Field("date"),
        )
        self.add_input(
            Submit("submit", "Kaydet")
        )
        self.render_required_fields = True


PainNatureFormSet = inlineformset_factory(
    parent_model=Pain,
    model=PainNature,
    form=PainNatureForm,
    extra=1,
    max_num=3,
    can_delete=False,
)
# endregion

# region PainFactorAffectingForm


class PainFactorAffectingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance.pk:
            for field in self.fields:
                # print(field)
                self.fields[field].widget.attrs["readonly"] = True
    class Meta:
        model = PainFactorAffecting
        fields = "__all__"
        widgets = {
            "date": forms.DateTimeInput(format=('%Y-%m-%dT%H:%M:%S'), attrs={'type': 'datetime-local'}),
        }


class PainFactorAffectingFormSetHelper(FormHelper):

    template = "bootstrap4/table_inline_formset.html"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.layout = Layout(
            Field("pain"),
            Field("description"),
            Field("date"),
        )
        self.add_input(
            Submit("submit", "Kaydet")
        )
        self.render_required_fields = True


PainFactorAffectingFormSet = inlineformset_factory(
    parent_model=Pain,
    model=PainFactorAffecting,
    form=PainFactorAffectingForm,
    extra=1,
    max_num=3,
    can_delete=False,
)
# endregion

# region PainTargetedLevelForm


class PainTargetedLevelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance.pk:
            for field in self.fields:
                # print(field)
                self.fields[field].widget.attrs["readonly"] = True
    class Meta:
        model = PainTargetedLevel
        fields = "__all__"
        widgets = {
            "date": forms.DateTimeInput(format=('%Y-%m-%dT%H:%M:%S'), attrs={'type': 'datetime-local'}),
        }


class PainTargetedLevelFormSetHelper(FormHelper):

    template = "bootstrap4/table_inline_formset.html"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.layout = Layout(
            Field("pain"),
            Field("description"),
            Field("date"),
        )
        self.add_input(
            Submit("submit", "Kaydet")
        )
        self.render_required_fields = True


PainTargetedLevelFormSet = inlineformset_factory(
    parent_model=Pain,
    model=PainTargetedLevel,
    form=PainTargetedLevelForm,
    extra=1,
    max_num=3,
    can_delete=False,
)
# endregion

# region PainInterventionForm


class PainInterventionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance.pk:
            for field in self.fields:
                # print(field)
                self.fields[field].widget.attrs["readonly"] = True
    class Meta:
        model = PainIntervention
        fields = "__all__"
        widgets = {
            "date": forms.DateTimeInput(format=('%Y-%m-%dT%H:%M:%S'), attrs={'type': 'datetime-local'}),
        }


class PainInterventionFormSetHelper(FormHelper):

    template = "bootstrap4/table_inline_formset.html"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.layout = Layout(
            Field("pain"),
            Field("pain_severity"),
            Field("medicine_detail"),
            Field("out_of_medicine"),
            Field("note"),
            Field("date"),
        )
        self.add_input(
            Submit("submit", "Kaydet")
        )
        self.render_required_fields = True


PainInterventionFormSet = inlineformset_factory(
    parent_model=Pain,
    model=PainIntervention,
    form=PainInterventionForm,
    extra=1,
    max_num=30,
    can_delete=False,
)
# endregion

# region PainForm


class FormSet(LayoutObject):

    template = "form/formset.html"

    def __init__(self, formset_name_in_context, template=None):
        self.formset_name_in_context = formset_name_in_context
        self.fields = []
        if template:
            self.template = template

    def render(self, form, context, template_pack=TEMPLATE_PACK, **kwargs):
        formset = context[self.formset_name_in_context]
        return render_to_string(self.template, {'formset': formset})


class PainForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        
        self.helper.layout = Layout(
            Field("bed"),
            Field("service"),
            Field("user"),

            HTML(
                """<img src="/static/img/numerik_agri_skalasi.png" class="img-fluid" >"""
            ),

            InlineRadios("numericalPainScale"),

            HTML(
                """<img src="/static/img/yuz_skalasi.png" class="img-fluid" >"""
            ),

            InlineRadios("wongBakerFacesPainScale"),


            InlineRadios("behavioralFaceExpressionPainScale"),


            InlineRadios("behavioralLegMovementsPainScale"),


            InlineRadios("behavioralActivityPainScale"),


            InlineRadios("behavioralCryPainScale"),


            InlineRadios("behavioralComfortedPainScale"),

            Div(
                Submit("submit", "Kaydet", css_class="btn btn-lg btn-warning"),
                css_class="d-flex justify-content-center mb-3",
            ),

            # Fieldset(
            #     PainScale._meta.verbose_name_plural,
            #     ModalEditFormsetLayout(
            #         "PainScaleInline",
            #         list_display=["description", "date"],
            #     ),
            # ),
            # Fieldset(
            #     PainPlace._meta.verbose_name_plural,
            #     ModalEditFormsetLayout(
            #         "PainPlaceInline",
            #         list_display=["description", "date"],
            #     ),
            # ),


            # Div(
            #     Submit("submit", "Kaydet", css_class="btn btn-lg btn-warning"),
            #     css_class="d-flex justify-content-center mb-3",
            # ),
        )

        if self.instance.pk:
            for field in self.fields:
                # print(field)
                self.fields[field].widget.attrs["readonly"]=True

    class Meta:
        model = Pain
        fields = "__all__"
        widgets = {
            "bed": forms.HiddenInput,
            "service": forms.HiddenInput,
            "user": forms.HiddenInput,
            "numericalPainScale": forms.RadioSelect,
            "wongBakerFacesPainScale": forms.RadioSelect,
            "behavioralFaceExpressionPainScale": forms.RadioSelect,
            "behavioralLegMovementsPainScale": forms.RadioSelect,
            "behavioralActivityPainScale": forms.RadioSelect,
            "behavioralCryPainScale": forms.RadioSelect,
            "behavioralComfortedPainScale": forms.RadioSelect,
        }

# endregion
