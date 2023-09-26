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

@csrf_exempt
def medicamento_view(request, pk):
    if request.method == 'GET':
        elemento_dto = el.get_medicamento(pk)
        elemento = serializers.serialize('json', [elemento_dto,])
        return HttpResponse(elemento, 'application/json')
    
