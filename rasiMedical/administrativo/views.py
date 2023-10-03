from django.shortcuts import render
from .logic import administrativo_logic as fl
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def facturas_view(request):
    if request.method == 'GET':
        facturas_dto = fl.get_facturas()
        facturas = serializers.serialize('json', facturas_dto)
        return HttpResponse(facturas, 'application/json')
    elif request.method == 'POST':
        factura_dto = fl.create_factura(json.loads(request.body))
        factura = serializers.serialize('json', [factura_dto,])
        return HttpResponse(factura, 'application/json')

@csrf_exempt
def factura_view(request, id):
    if request.method == 'GET':
        factura_dto = fl.get_factura(id)
        factura = serializers.serialize('json', [factura_dto,])
        return HttpResponse(factura, 'application/json')
    elif request.method == 'PUT':
        factura_dto = fl.update_factura(id, json.loads(request.body))
        factura = serializers.serialize('json', [factura_dto,])
        return HttpResponse(factura, 'application/json')
    elif request.method == 'DELETE':
        fl.delete_factura(id)
        return HttpResponse("Borrado exitoso con id: " + str(id))