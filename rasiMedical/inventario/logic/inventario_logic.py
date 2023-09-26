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
