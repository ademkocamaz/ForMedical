from django import forms


from django.contrib.auth.forms import AuthenticationForm
from genotip._model.service import ServiceDefinition


class LoginForm(AuthenticationForm):
    servis = forms.ModelChoiceField(ServiceDefinition.objects.all())
