from .logic import inventario_logic as el
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def dispositivos_view(request):
    if request.method == 'GET':
        elementos_dto = el.get_dipositivos()
        elementos = serializers.serialize('json', elementos_dto)
        return HttpResponse(elementos, 'application/json')

@csrf_exempt
def dispositivo_view(request, pk):
    if request.method == 'GET':
        elemento_dto = el.get_dispositivo(pk)
        elemento = serializers.serialize('json', [elemento_dto,])
        return HttpResponse(elemento, 'application/json')
    
@csrf_exempt
def medicamentos_view(request):
    if request.method == 'GET':
        elementos_dto = el.get_medicamentos()
        elementos = serializers.serialize('json', elementos_dto)    
        return HttpResponse(elementos, 'application/json')
    
    elif request.method == 'POST':
        elemento_dto = el.create_medicamento(json.loads(request.body))
        elemento = serializers.serialize('json', [elemento_dto,])
        return HttpResponse(elemento, 'application/json')

@csrf_exempt
def medicamento_view(request, id):
    if request.method == 'GET':
        elemento_dto = el.get_medicamento(id)
        elemento = serializers.serialize('json', [elemento_dto,])
        return HttpResponse(elemento, 'application/json')
    
    elif request.method == 'PUT':
        elemento_dto = el.update_medicamento(id, json.loads(request.body))
        elemento = serializers.serialize('json', [elemento_dto,])
        return HttpResponse(elemento, 'application/json')
    
    elif request.method == 'DELETE':
        el.delete_medicamento(id)
        return HttpResponse("Borrado exitoso con id: " + str(id))
    
