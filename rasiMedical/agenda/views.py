from django.shortcuts import render
from .logic import agenda_logic as al
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt
from datetime import date
from django.core.mail import send_mail
from usuario.logic import usuario_logic as ul
from rasiMedical.settings import EMAIL_HOST_USER

# Create your views here.
@csrf_exempt
def citas_view(request):
    if request.method == 'GET':
        citas = al.get_citas()
        citasDTO = serializers.serialize('json', citas)
        return HttpResponse(citasDTO, content_type = 'application/json')
    
    if request.method == 'POST':
        citaDTO = al.create_cita(json.loads(request.body))
        cita = serializers.serialize('json', [citaDTO,])
        return HttpResponse(cita, 'application/json')
    

@csrf_exempt
def cita_view(request, pk):
    if request.method == 'GET':
        cita = al.get_cita(pk)
        citasDTO = serializers.serialize('json', [cita])
        return HttpResponse(citasDTO, content_type = 'application/json')
    
    if request.method == 'PUT':
        citaDTO = al.update_cita(pk, json.loads(request.body))
        cita = serializers.serialize('json', [citaDTO,])
        return HttpResponse(cita, 'application/json')
    
    if request.method == 'DELETE':
        al.delete_cita(pk)
        return HttpResponse("Borrado exitoso con id: " + str(pk))