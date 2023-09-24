
from ..models import Elemento


def get_elementos():
    elementos = Elemento.objects.all()
    return elementos

def get_elemento(epk):
    elemento = Elemento.objects.get(pk = epk)
    return elemento
