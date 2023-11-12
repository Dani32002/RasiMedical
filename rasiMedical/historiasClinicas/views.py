import json
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from .logic import entradaClinica_logic as pl

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