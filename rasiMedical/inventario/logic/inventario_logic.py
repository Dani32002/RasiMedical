from ..models import Dispositivo


def get_dipositivos():
    elementos = Dispositivo.objects.all()
    return elementos

def get_dispositivo(epk):
    elemento = Dispositivo.objects.get(pk = epk)
    return elemento
