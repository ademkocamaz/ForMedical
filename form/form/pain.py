from django import forms
from django.forms import inlineformset_factory
from form.model.pain import *
# from crispy_forms.helper import FormHelper


class PainForm(forms.ModelForm):
    class Meta:
        model = Pain
        fields = [
            field.name
            for field in Pain._meta.fields
            if field.name not in ("id", "edited", "created", "service", "user")
        ]


class PainScaleForm(forms.ModelForm):
    class Meta:
        model = PainScale
        fields = "__all__"


class PainPlaceForm(forms.ModelForm):
    class Meta:
        model = PainPlace
        fields = "__all__"


PainScaleFormSet = inlineformset_factory(
    parent_model=Pain,
    model=PainScale,
    form=PainScaleForm,
    extra=0,
    max_num=0,
    can_delete=False,
)

PainPlaceFormSet = inlineformset_factory(
    parent_model=Pain,
    model=PainPlace,
    form=PainPlaceForm,
    extra=0,
    max_num=0,
    can_delete=False,
)
