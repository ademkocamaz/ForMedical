from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from genotip._model.service import ServiceDefinition
from genotip._model.bed import Bed
from form._form.pain import Pain
from form._model.observation import Observation
from django.contrib import messages

# Create your views here.
from app._view.pain import pain, pain_print, pain_update
from app._view.observation import Observation_CreateView


@login_required(login_url="/login/")
def index(request):
    messages.add_message(request, messages.WARNING, 'Hoşgeldiniz.')

    if request.session.has_key("service"):
        service_definition = ServiceDefinition.objects.get(
            id=request.session["service"])
    else:
        service_definition = None
    context = {
        "service_definition": service_definition if service_definition != None else "--Servis Seçilmedi--",
        "beds": Bed.objects.filter(service_definition=service_definition).order_by("oda")
    }

    return render(request=request, template_name='app/index.html', context=context)


@login_required(login_url="/login/")
def bed_detail(request, bed_id):
    bed = get_object_or_404(Bed, pk=bed_id)
    service_definition = ServiceDefinition.objects.get(
        id=request.session["service"]
    )

    pain_forms = Pain.objects.filter(bed=bed, service=bed.service)
    observation_forms = Observation.objects.filter(
        bed=bed, service=bed.service)

    context = {
        "service_definition": service_definition,
        "bed": bed,
        "pain_forms": pain_forms,
        "observation_forms": observation_forms,
    }

    return render(request=request, template_name='app/bed_detail.html', context=context)
