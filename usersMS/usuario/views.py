from django.views.decorators.csrf import csrf_exempt
from .logic import usuario_logic as ul
from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
import json

@csrf_exempt
def medicos_view(request):
    if request.method == 'GET':
        meds = ul.get_medicos()
        medsDTO = serializers.serialize('json', meds)
        return HttpResponse(medsDTO, content_type = 'application/json')
    
    if request.method == 'POST':
        med_dto = ul.create_medico(json.loads(request.body))
        medico = serializers.serialize('json', [med_dto,])
        return HttpResponse(medico, 'application/json')    

@csrf_exempt
def medico_view(request, pk):
    if request.method == 'GET':
        med = ul.get_medico(pk)
        medDTO = serializers.serialize('json', [med])
        return HttpResponse(medDTO, content_type = 'application/json')
    
    if request.method == 'PUT':
        med_dto = ul.update_medico(pk, json.loads(request.body))
        med = serializers.serialize('json', [med_dto,])
        return HttpResponse(med, 'application/json')
    
    if request.method == 'DELETE':
        ul.delete_medico(pk)
        return HttpResponse("Borrado exitoso con id: " + str(pk))