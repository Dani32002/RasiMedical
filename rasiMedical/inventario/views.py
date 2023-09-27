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
    elif request.method == 'POST':
        elemento_dto = el.create_dispositivo(json.loads(request.body))
        elemento = serializers.serialize('json', [elemento_dto,])
        return HttpResponse(elemento, 'application/json')

@csrf_exempt
def dispositivo_view(request, pk):
    if request.method == 'GET':
        elemento_dto = el.get_dispositivo(pk)
        elemento = serializers.serialize('json', [elemento_dto,])
        return HttpResponse(elemento, 'application/json')
    elif request.method == 'PUT':
        elemento_dto = el.update_dispositivo(pk, json.loads(request.body))
        elemento = serializers.serialize('json', [elemento_dto,])
        return HttpResponse(elemento, 'application/json')
    elif request.method == 'DELETE':
        el.delete_dispositivo(pk)
        return HttpResponse("Borrado exitoso con id: " + str(pk))
    
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

@csrf_exempt
def insumos_view(request):
    if request.method == 'GET':
        elementos_dto = el.get_insumos()
        elementos = serializers.serialize('json', elementos_dto)
        return HttpResponse(elementos, 'application/json')
    elif request.method == 'POST':
        elemento_dto = el.create_insumo(json.loads(request.body))
        elemento = serializers.serialize('json', [elemento_dto,])
        return HttpResponse(elemento, 'application/json')

@csrf_exempt
def insumo_view(request, id):
    if request.method == 'GET':
        elemento_dto = el.get_insumo(id)
        elemento = serializers.serialize('json', [elemento_dto,])
        return HttpResponse(elemento, 'application/json')
    elif request.method == 'PUT':
        elemento_dto = el.update_insumo(id, json.loads(request.body))
        elemento = serializers.serialize('json', [elemento_dto,])
        return HttpResponse(elemento, 'application/json')
    elif request.method == 'DELETE':
        el.delete_insumo(id)
        return HttpResponse("Borrado exitoso con id: " + str(id))
