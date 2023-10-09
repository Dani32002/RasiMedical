import json
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
    
    if request.method == 'POST':
        med_dto = pl.create_medico(json.loads(request.body))
        medico = serializers.serialize('json', [med_dto,])
        return HttpResponse(medico, 'application/json')    


@csrf_exempt
def medico_view(request, pk):
    if request.method == 'GET':
        med = pl.get_medico(pk)
        medDTO = serializers.serialize('json', [med])
        return HttpResponse(medDTO, content_type = 'application/json')
    
    if request.method == 'PUT':
        med_dto = pl.update_medico(pk, json.loads(request.body))
        med = serializers.serialize('json', [med_dto,])
        return HttpResponse(med, 'application/json')
    
    if request.method == 'DELETE':
        pl.delete_medico(pk)
        return HttpResponse("Borrado exitoso con id: " + str(pk))


@csrf_exempt
def pacientes_view(request):
    if request.method == 'GET':
        pacientes = pl.get_pacientes()
        pacientesDTO = serializers.serialize('json', pacientes)
        return HttpResponse(pacientesDTO, content_type='application/json')
    
    if request.method == 'POST':
        pac_dto = pl.create_paciente(json.loads(request.body))
        paciente = serializers.serialize('json', [pac_dto,])
        return HttpResponse(paciente, content_type='application/json')    

@csrf_exempt
def paciente_view(request, pk):
    if request.method == 'GET':
        paciente = pl.get_paciente(pk)
        pacienteDTO = serializers.serialize('json', [paciente])
        return HttpResponse(pacienteDTO, content_type='application/json')
    
    if request.method == 'PUT':
        pac_dto = pl.update_paciente(pk, json.loads(request.body))
        paciente = serializers.serialize('json', [pac_dto,])
        return HttpResponse(paciente, content_type='application/json')
    
    if request.method == 'DELETE':
        pl.delete_paciente(pk)
        return HttpResponse("Borrado exitoso con id: " + str(pk))