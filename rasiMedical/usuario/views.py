import json
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader

from rasiMedical.auth0backend import getEmail, getRole
from .logic import usuario_logic as pl
from agenda.logic import agenda_logic as al2
from administrativo.logic import administrativo_logic as al
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from agenda.models import Cita
from historiasClinicas.logic import historiasClinicas_logic as hl
# Create your views here.
from django.contrib.auth.decorators import login_required
from historiasClinicas import views as vh

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
def estadisticas(request):
    if request.method == 'GET':
        pacientes = pl.get_pacientes()
        citas = al2.get_citas()
        i = 0
        for j in citas:
            if (j.completada):
                i += 1
        template = loader.get_template('estadisticas.html')
        context = {
            "pacientes": str(len(pacientes)),
            "completadas": str(i)
        }
        return context

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
    

@csrf_exempt
def farmaceuticos_view(request):
    if request.method == 'GET':
        fars = pl.get_farmaceuticos()
        farsDTO = serializers.serialize('json', fars)
        return HttpResponse(farsDTO, content_type = 'application/json')
    
    if request.method == 'POST':
        far_dto = pl.create_farmaceutico(json.loads(request.body))
        fars = serializers.serialize('json', [far_dto,])
        return HttpResponse(fars, 'application/json')    

@csrf_exempt
def farmaceutico_view(request, pk):
    if request.method == 'GET':
        far = pl.get_farmaceutico(pk)
        farDTO = serializers.serialize('json', [far])
        return HttpResponse(farDTO, content_type = 'application/json')
    
    if request.method == 'PUT':
        far_dto = pl.update_farmaceutico(pk, json.loads(request.body))
        far = serializers.serialize('json', [far_dto,])
        return HttpResponse(far, 'application/json')
    
    if request.method == 'DELETE':
        pl.delete_farmaceutico(pk)
        return HttpResponse("Borrado exitoso con id: " + str(pk))
    

@csrf_exempt
def enfermeras_view(request):
    if request.method == 'GET':
        enfs = pl.get_Enfermeras()
        enfsDTO = serializers.serialize('json', enfs)
        return HttpResponse(enfsDTO, content_type = 'application/json')
    
    if request.method == 'POST':
        enf_dto = pl.create_Enfermera(json.loads(request.body))
        enfs = serializers.serialize('json', [enf_dto,])
        return HttpResponse(enfs, 'application/json')    

@csrf_exempt
def enfermera_view(request, pk):
    if request.method == 'GET':
        enf = pl.get_Enfermera(pk)
        enfDTO = serializers.serialize('json', [enf])
        return HttpResponse(enfDTO, content_type = 'application/json')
    
    if request.method == 'PUT':
        enf_dto = pl.update_Enfermera(pk, json.loads(request.body))
        enf = serializers.serialize('json', [enf_dto,])
        return HttpResponse(enf, 'application/json')
    
    if request.method == 'DELETE':
        pl.delete_enfermera(pk)
        return HttpResponse("Borrado exitoso con id: " + str(pk))
    
@csrf_exempt
def usuarioEmail(request, email):
    return pl.get_medicoEmail(email)

@csrf_exempt
def enfermeraEmail(request, email):
    return pl.get_enfemeraEmail(email)
     
@csrf_exempt
def farmaceuticoEmail(request, email):
    return pl.get_farmaceuticaEmail(email)


@login_required
def pacientesHC_view(request):
    role = getRole(request)
    if request.method == 'GET' and (role == "Medico" or role == "Farmaceutico" or role == "Enfermera"):
        pacientes = pl.get_pacientes()
        template = loader.get_template('historiasClinicas.html')
        context = {
            "pacientes": pacientes
        }
        return HttpResponse(template.render(context, request))
    return HttpResponse("Error")