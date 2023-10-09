from django.shortcuts import render
from .logic import administrativo_logic as fl
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt
from datetime import date

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

@csrf_exempt
def emitirFactura(request, id):
    factura_dto = fl.get_factura(id)
    factura_dto.fechaEmision = date.today()
    factura_dto.save()
    factura = serializers.serialize('json', [factura_dto,])
    return HttpResponse(factura, 'application/json')
    
@csrf_exempt
def EPSs_view(request):
    if request.method == 'GET':
        epss = fl.get_EPSs()
        epssDTO = serializers.serialize('json', epss)
        return HttpResponse(epss, content_type = 'application/json')
    
    if request.method == 'POST':
        epsDTO = fl.create_EPS(json.loads(request.body))
        eps = serializers.serialize('json', [epsDTO,])
        return HttpResponse(eps, 'application/json')
    

@csrf_exempt
def EPS_view(request, pk):
    if request.method == 'GET':
        eps = fl.get_EPS(pk)
        epsDTO = serializers.serialize('json', [eps])
        return HttpResponse(epsDTO, content_type = 'application/json')
    
    if request.method == 'PUT':
        epsDTO = fl.update_EPS(pk, json.loads(request.body))
        eps = serializers.serialize('json', [epsDTO,])
        return HttpResponse(eps, 'application/json')
    
    if request.method == 'DELETE':
        fl.delete_EPS(pk)
        return HttpResponse("Borrado exitoso con id: " + str(pk))
