from ..models import Factura
from ..models import EPS

def create_factura(new):
    factura = Factura(numero = new["numero"], fechaEmision = new["fechaEmision"], fechaPago = new["fechaPago"], total = new["total"])
    factura.save()
    return factura

def update_factura(epk, new):
    act = get_factura(epk)
    act.numero = new["numero"]
    act.fechaEmision = new["fechaEmision"]
    act.fechaPago = new["fechaPago"]
    act.total = new["total"]
    act.save()
    return act

def delete_factura(pk):
    dispositivo = get_factura(pk)
    dispositivo.delete()
    
def get_facturas():
    elementos = Factura.objects.all()
    return elementos

def get_factura(epk):
    elemento = Factura.objects.get(pk = epk)
    return elemento


def create_EPS(new):
    eps = EPS(nombre = new["nombre"], nit = new["nit"])
    eps.save()
    return eps

def get_EPSs():
    elementos = EPS.objects.all()
    return elementos

def get_EPS(epk):
    elemento = EPS.objects.get(pk = epk)
    return elemento

def update_EPS(epk, new):
    act = get_EPS(epk)
    act.nombre = new["nombre"]
    act.nit = new["nit"]
    act.save()
    return act

def delete_EPS(pk):
    eps = get_EPS(pk)
    eps.delete()