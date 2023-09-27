from ..models import Dispositivo
from ..models import Medicamento
from ..models import Insumo

# CRUD DISPOSITIVOS

def create_dispositivo(new):
    dispositivo = Dispositivo(nombre = new["nombre"], estado = new["estado"], descripcion = new["descripcion"], funcion = new["funcion"])
    dispositivo.save()
    return dispositivo

def update_dispositivo(epk, new):
    act = get_dispositivo(epk)
    act.nombre = new["nombre"]
    act.estado = new["estado"]
    act.descripcion = new["descripcion"]
    act.funcion = new["funcion"]
    act.save()
    return act

def update_dispositivoMedico(new):
    new.save()
    return new

def delete_dispositivo(pk):
    dispositivo = get_dispositivo(pk)
    dispositivo.delete()
    
def get_dipositivos():
    elementos = Dispositivo.objects.all()
    return elementos

def get_dispositivo(epk):
    elemento = Dispositivo.objects.get(pk = epk)
    return elemento

# FINALIZA CRUD DISPOSITIVOS

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
    act.descripcion = new["descripcion"]
    act.medico = new["medico"]
    act.fabricante = new["fabricante"]
    act.concentracion = new["concentracion"]
    act.administracion = new["administracion"]
    act.save()
    return act

def update_medicamentoMedico(new):
    new.save()
    return new
    
def create_medicamento(new):
    medicamento = Medicamento(nombre = new["nombre"], estado = new["estado"], descripcion = new["descripcion"], medico = new["medico"], fabricante = new["fabricante"], concentracion = new["concentracion"], administracion = new["administracion"])
    medicamento.save()
    return medicamento

def delete_medicamento(pk):
    medicamento = get_medicamento(pk)
    medicamento.delete()

# CRUD INSUMOS

def get_insumos():
    elementos = Insumo.objects.all()
    return elementos

def get_insumo(epk):    
    elemento = Insumo.objects.get(pk=epk)
    return elemento

def update_insumo(epk, new):
    act = get_insumo(epk)
    act.nombre = new["nombre"]
    act.estado = new["estado"]
    act.descripcion = new["descripcion"]
    act.proposito = new["proposito"]
    act.unidad = new["unidad"]
    act.save()
    return act

def update_insumoMedico(new):
    new.save()
    return new

def create_insumo(new):
    insumo = Insumo(nombre = new["nombre"], estado = new["estado"], descripcion = new["descripcion"], proposito = new["proposito"], unidad = new["unidad"])
    insumo.save()
    return insumo

def delete_insumo(pk):
    insumo = get_insumo(pk)
    insumo.delete()
