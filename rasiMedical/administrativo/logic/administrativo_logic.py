from ..models import Factura

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