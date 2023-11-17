import json
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .logic import historiasClinicas_logic as pl
from usuario.logic import usuario_logic as ul
from agenda.logic import agenda_logic as al
from rasiMedical.auth0backend import getEmail, getRole
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader


@csrf_exempt
def entradasClinicas_view(request):
    if request.method == 'GET':
        entradasClinicas = pl.get_entradasClinicas()
        entradasClinicasDTO = serializers.serialize('json', entradasClinicas)
        return HttpResponse(entradasClinicasDTO, content_type = 'application/json')
    
    if request.method == 'POST':
        ent_dto = pl.create_entradaClinica(json.loads(request.body))
        ent = serializers.serialize('json', [ent_dto,])
        return HttpResponse(ent, 'application/json')

@csrf_exempt
def entradaClinica_view(request, pk):
    if request.method == 'GET':
        ent = pl.get_entradaClinica(pk)
        entDTO = serializers.serialize('json', [ent])
        return HttpResponse(entDTO, content_type = 'application/json')
    
    if request.method == 'PUT':
        ent_dto = pl.update_entradaClinica(pk, json.loads(request.body))
        ent = serializers.serialize('json', [ent_dto,])
        return HttpResponse(ent, 'application/json')
    
    if request.method == 'DELETE':
        pl.delete_entradaClinica(pk)
        return HttpResponse("Borrado exitoso con id: " + str(pk))
    
@csrf_exempt
def anadirMedico(request, pk, pkEntidad):
    if request.method == 'POST':
        medico = ul.get_medico(pkEntidad)
        hc = pl.get_entradaClinica(pk)
        hc.permitidosMedico.add(medico)
        return HttpResponse("Se añadio el medico: " + str(pkEntidad) + ", a la historia clinica: " + str(pk))

@csrf_exempt
def anadirFarmaceutico(request, pk, pkEntidad):
    if request.method == 'POST':
        far = ul.get_farmaceutico(pkEntidad)
        hc = pl.get_entradaClinica(pk)
        hc.permitidosFarmaceutico.add(far)
        return HttpResponse("Se añadio el farmaceutico: " + str(pkEntidad) + ", a la historia clinica: " + str(pk))
    

@csrf_exempt
def anadirEnfermera(request, pk, pkEntidad):
    if request.method == 'POST':    
        enf = ul.get_Enfermera(pkEntidad)
        hc = pl.get_entradaClinica(pk)
        hc.permitidosEnfermera.add(enf)
        return HttpResponse("Se añadio la enfermera: " + str(pkEntidad) + ", a la historia clinica: " + str(pk))
        

@csrf_exempt
def usuarioEmail(request, email):
    return ul.get_medicoEmail(email)

@csrf_exempt
def enfermeraEmail(request, email):
    return ul.get_enfemeraEmail(email)
     
@csrf_exempt
def farmaceuticoEmail(request, email):
    return ul.get_farmaceuticaEmail(email)
    
@csrf_exempt
@login_required
def nueva_historia(request, pk):
    role = getRole(request)
    if request.method == 'POST' and role == "Medico":
        email = getEmail(request)
        usuario = usuarioEmail(request, email)
        ent = request.POST
        entidad = {
            "diagnostico": ent["diagnostico"],
            "tratamiento": ent["tratamiento"],
            "paciente": pk,
            "autor": usuario.id, # type: ignore
            "fecha": ent["fecha"],
            "cita": ent["cita"]
        } 
        entrada = pl.create_entradaClinica(entidad)
        vh.anadirMedico(request, entrada.id, usuario.id) # type: ignore
        return HttpResponseRedirect("/")
    return HttpResponse("Error")


@csrf_exempt
@login_required
def crear(request, pk):
    role = getRole(request)
    if request.method == 'GET' and role == "Medico":
        email = getEmail(request)
        usuario = usuarioEmail(request, email)
        citas = al.get_citasPacienteMedico(pk, usuario.id) # type: ignore
        template = loader.get_template('nuevaHistoria.html')
        context = {
            "citas": citas
        }
        return HttpResponse(template.render(context, request)) 
    return HttpResponse("Error")

@login_required
def pacientes_historias(request, pk):
    role = getRole(request)
    if request.method == 'GET' and (role == "Medico" or role == "Farmaceutico" or role == "Enfermera"):
        usuario = None
        paciente = ul.get_paciente(pk)
        historias = paciente.entradaclinica_set.all()  # type: ignore
        historias2 = []
        email = getEmail(request)
        if role == "Medico":
            usuario = usuarioEmail(request, email)
            print(usuario)
            for historia in historias:
                if usuario in historia.permitidosMedico.all():
                    historias2.append(historia)
        elif role == "Farmaceutico":
            usuario = farmaceuticoEmail(request, email)
            for historia in historias:
                if usuario in historia.permitidosFarmaceutico.all():
                    historias2.append(historia)
        else:
            usuario = enfermeraEmail(request, email)
            for historia in historias:
                if usuario in historia.permitidosEnfermera.all():
                    historias2.append(historia)
        
        template = loader.get_template('entradasClinicas.html')
        context = {
            "paciente": paciente,
            "entradas": historias2
        }
        return HttpResponse(template.render(context, request))
    return HttpResponse("Error")