import json
from django.http import HttpResponse
from .logic import usuario_logic as pl
from administrativo.logic import administrativo_logic as al
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
def paciente_view(request, id):
    if request.method == 'GET':
        paciente = pl.get_paciente(id)
        pacienteDTO = serializers.serialize('json', [paciente])
        return HttpResponse(pacienteDTO, content_type='application/json')
    
    if request.method == 'PUT':
        pac_dto = pl.update_paciente(id, json.loads(request.body))
        paciente = serializers.serialize('json', [pac_dto,])
        return HttpResponse(paciente, content_type='application/json')
    
    if request.method == 'DELETE':
        pl.delete_paciente(id)
        return HttpResponse("Borrado exitoso con id: " + str(id))
    
@csrf_exempt
def anadirEpsPaciente(request, id, id2):
    if request.method == 'POST':
        paciente = pl.get_paciente(id)
        eps = al.get_EPS(id2)
        paciente.eps = eps
        pl.update_pacienteEps(paciente)
        elementoDto = serializers.serialize('json',[paciente])
        return HttpResponse(elementoDto, 'application/json')
    
@csrf_exempt
def admins_view(request):
    if request.method == 'GET':
        admins = pl.get_admins()
        adminsDTO = serializers.serialize('json', admins)
        return HttpResponse(adminsDTO, content_type='application/json')
    if request.method == 'POST':
        admin_dto = pl.create_admin(json.loads(request.body))
        admin = serializers.serialize('json', [admin_dto,])
        return HttpResponse(admin, 'application/json')

@csrf_exempt
def admin_view(request, pk):
    if request.method == 'GET':
        admin = pl.get_admin(pk)
        adminDTO = serializers.serialize('json', [admin])
        return HttpResponse(adminDTO, content_type='application/json')
    if request.method == 'PUT':
        admin_dto = pl.update_admin(pk, json.loads(request.body))
        admin = serializers.serialize('json', [admin_dto,])
        return HttpResponse(admin, 'application/json')
    if request.method == 'DELETE':
        pl.delete_admin(pk)
        return HttpResponse("Borrado exitoso con id: " + str(pk))