from django.http import HttpResponse
from django.shortcuts import render
from inventario.logic import inventario_logic
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
from usuario.logic import usuario_logic
from inventario import views

def home(request):
    return HttpResponse("Hello world! Django views")

def asignar(request):
    return render(request, 'asignar.html')

@csrf_exempt
def mostrarTipo(request):
    if request.method == 'POST':
        if request.POST["elemento"] == "Dispositivo":
            disps = inventario_logic.get_dipositivos()
            medicos = usuario_logic.get_medicos()
            template = loader.get_template('mostrarDispositivos.html')
            context = {
                "dispositivos": disps,
                "medicos": medicos
            }
            return HttpResponse(template.render(context, request))
        elif request.POST["elemento"] == "Insumo":
            insus = inventario_logic.get_insumos()
            medicos = usuario_logic.get_medicos()
            template = loader.get_template('mostrarInsumos.html')
            context = {
                "insumos": insus,
                "medicos": medicos
            }
            return HttpResponse(template.render(context, request))
        else:
            meds = inventario_logic.get_medicamentos()
            medicos = usuario_logic.get_medicos()
            template = loader.get_template('mostrarMedicamentos.html')
            context = {
                "medicamentos": meds,
                "medicos": medicos
            }
            return HttpResponse(template.render(context, request))

@csrf_exempt
def asociarInsumo(request):
    views.anadirMedicoInsumo(request, request.POST["insumo"], request.POST["medico"])
    return render(request, 'asignar.html')

@csrf_exempt
def asociarMedicamento(request):
    views.anadirMedicoMedicamento(request, request.POST["medicamento"], request.POST["medico"])
    return render(request, 'asignar.html')

@csrf_exempt
def asociarDispositivo(request):
    views.anadirMedicoDispositivo(request, request.POST["dispositivo"], request.POST["medico"])
    return render(request, 'asignar.html')