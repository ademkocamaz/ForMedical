from django.shortcuts import render
from form.form.pain import PainForm
# Create your views here.
def print_pain(request):
    painForm = PainForm()
    
    context = {
        'pain_form': painForm,
    }
    return render(request=request, template_name='form/pain_print.html', context=context)