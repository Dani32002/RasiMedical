from django.http import HttpResponse
from .logic import usuario_logic as pl
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def medicos_view(request):
    if request.method == 'GET':
        meds = pl.get_medicos()
        medsDTO = serializers.serialize('json', meds)
        return HttpResponse(meds, content_type = 'application/json')


@csrf_exempt
def medico_view(request, pk):
    if request.method == 'GET':
        med = pl.get_medico(pk)
        medDTO = serializers.serialize('json', [med])
        return HttpResponse(medDTO, content_type = 'application/json')


