from .logic import elemento_logic as el
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def elementos_view(request):
    if request.method == 'GET':
            elementos_dto = el.get_elementos()
            elementos = serializers.serialize('json', elementos_dto)
            return HttpResponse(elementos, 'application/json')

@csrf_exempt
def elemento_view(request, pk):
    if request.method == 'GET':
        elemento_dto = el.get_elemento(pk)
        elemento = serializers.serialize('json', [elemento_dto,])
        return HttpResponse(elemento, 'application/json')