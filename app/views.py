from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from genotip._model.service import ServiceDefinition
from genotip._model.bed import Bed
# Create your views here.


@login_required(login_url="/login/")
def index(request):

    service_definition = ServiceDefinition.objects.get(id=request.session["service"])
    context = {
        "service_definition": service_definition,
        "beds": Bed.objects.filter(service_definition=service_definition).order_by("-yatak")
    }

    return render(request=request, template_name='app/index.html', context=context)
