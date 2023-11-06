from ..models import Cita
from usuario.logic import usuario_logic as ul
from administrativo.logic import administrativo_logic as al


def create_cita(new):
    pacienteN = ul.get_paciente(new["paciente"])
    profesionalN = ul.get_medico(new["medicoCita"])
    factura = Cita(fecha = new["fecha"], completada = False, medicoCita = profesionalN, paciente = pacienteN)
    factura.save()
    return factura

def update_cita(epk, new):
    act = get_cita(epk)
    act.fecha = new["fecha"]
    act.completada = new["completada"]
    profesionalN = ul.get_medico(new["medicoCita"])
    act.medicoCita = profesionalN
    pacienteN = ul.get_paciente(new["paciente"])
    act.paciente = pacienteN
    facturaN = al.get_factura(new["factura"])
    act.factura = facturaN # type: ignore
    act.save()
    return act

def delete_cita(pk):
    dispositivo = get_cita(pk)
    dispositivo.delete()
    
def get_citas():
    elementos = Cita.objects.all()
    return elementos

def get_cita(epk):
    elemento = Cita.objects.get(pk = epk)
    return elemento