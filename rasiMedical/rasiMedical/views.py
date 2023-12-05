from datetime import date
from django.http import HttpResponse
from django.shortcuts import render
import requests
from inventario.logic import inventario_logic
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
from usuario.logic import usuario_logic
from usuario import views as uv
from inventario import views
from django.contrib.auth.decorators import login_required
from rasiMedical.auth0backend import getToken

def home(request):
    return render(request, 'home.html')

@login_required
def asignar(request):
    return render(request, 'asignar.html')

@csrf_exempt
@login_required
def mostrarTipo(request):
    rMeds = requests.get("http://10.128.0.6:8080/usuario/medico/", headers={"Accept":"application/json"})
    medicos = rMeds.json()
    if request.method == 'POST':
        if request.POST["elemento"] == "Dispositivo":
            r = requests.get("http://10.182.0.6:8080/inventario/dispositivo/", headers={"Accept":"application/json"})
            disps = r.json()
            print(disps)
            template = loader.get_template('mostrarDispositivos.html')
            context = {
                "dispositivos": disps,
                "medicos": medicos
            }
            return HttpResponse(template.render(context, request))
        elif request.POST["elemento"] == "Insumo":
            r = requests.get("http://10.182.0.6:8080/inventario/insumo/", headers={"Accept":"application/json"})
            insus = r.json()
            template = loader.get_template('mostrarInsumos.html')
            context = {
                "insumos": insus,
                "medicos": medicos
            }
            return HttpResponse(template.render(context, request))
        else:
            r = requests.get("http://10.182.0.6:8080/inventario/medicamento/", headers={"Accept":"application/json"})
            meds = r.json()
            template = loader.get_template('mostrarMedicamentos.html')
            context = {
                "medicamentos": meds,
                "medicos": medicos
            }
            return HttpResponse(template.render(context, request))

@csrf_exempt
@login_required
def asociarInsumo(request):
    obj = {
        "tipo": "Insumo",
        "fecha": str(date.today()),
        "activo": True,
        "elemento": request.POST["insumo"],
        "medico": request.POST["medico"]
    }
    accessToken = getToken(request)
    print(accessToken)
    headers = {'authorization': 'Bearer ' + accessToken}
    requests.post("http://10.182.0.7:8000/asignacion", json = obj, headers=headers)
    return render(request, 'asignar.html')

@csrf_exempt
@login_required
def asociarMedicamento(request):
    obj = {
        "tipo": "Medicamento",
        "fecha": str(date.today()),
        "activo": True,
        "elemento": request.POST["medicamento"],
        "medico": request.POST["medico"]
    }
    accessToken = getToken(request)
    print(accessToken)
    headers = {'authorization': 'Bearer ' + accessToken}
    requests.post("http://10.182.0.7:8000/asignacion", json = obj, headers=headers)
    return render(request, 'asignar.html')

@csrf_exempt
@login_required
def asociarDispositivo(request):
    obj = {
        "tipo": "Dispositivo",
        "fecha": str(date.today()),
        "activo": True,
        "elemento": request.POST["dispositivo"],
        "medico": request.POST["medico"]
    }
    accessToken = getToken(request)
    print(accessToken)
    headers = {'authorization': 'Bearer ' + accessToken}
    requests.post("http://10.182.0.7:8000/asignacion", json = obj, headers=headers)
    return render(request, 'asignar.html')


@csrf_exempt
def estadisticas(request):
    template = loader.get_template('estadisticas.html')
    context = uv.estadisticas(request)
    return HttpResponse(template.render(context, request))

@csrf_exempt
def healthCheck(request):
    return HttpResponse('ok')
