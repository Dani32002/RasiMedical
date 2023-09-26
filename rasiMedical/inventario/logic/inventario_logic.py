from ..models import Dispositivo
from ..models import Medicamento


def get_dipositivos():
    elementos = Dispositivo.objects.all()
    return elementos

def get_dispositivo(epk):
    elemento = Dispositivo.objects.get(pk = epk)
    return elemento

def get_medicamentos():
    elementos = Medicamento.objects.all()
    return elementos

def get_medicamento(epk):
    elemento = Medicamento.objects.get(pk=epk)
    return elemento

def update_medicamento(epk, new):
    act = get_medicamento(epk)
    act.nombre = new["nombre"]
    act.estado = new["estado"]
    act.cantidad = new["cantidad"]
    act.descripcion = new["descripcion"]
    act.medico = new["medico"]
    act.fabricante = new["fabricante"]
    act.concentracion = new["concentracion"]
    act.administracion = new["administracion"]
    act.save()
    return act
    
def create_medicamento(new):
    medicamento = Medicamento(nombre = new["nombre"], estado = new["estado"], cantidad = new["cantidad"], descripcion = new["descripcion"], medico = new["medico"], fabricante = new["fabricante"], concentracion = new["concentracion"], administracion = new["administracion"])
    medicamento.save()
    return medicamento

def delete_medicamento(pk):
    medicamento = get_medicamento(pk)
    medicamento.delete()
    
