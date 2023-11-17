from datetime import datetime
from ..models import EntradaClinica
from usuario.logic import usuario_logic as ul
from agenda.logic import agenda_logic as al

def get_entradasClinicas():
    entradasClinicas = EntradaClinica.objects.all()
    return entradasClinicas

def get_entradaClinica(ent_pk):
    entradaClinica = EntradaClinica.objects.get(pk=ent_pk)
    return entradaClinica

def update_entradaClinica(ent_pk, new_ent):
    entradaClinica = get_entradaClinica(ent_pk)
    entradaClinica.diagnostico = new_ent["diagnostico"]
    entradaClinica.tratamiento = new_ent["tratamiento"]
    entradaClinica.paciente = ul.get_paciente(new_ent["paciente"])
    entradaClinica.autor = ul.get_medico(new_ent["autor"])
    date_format = '%Y-%m-%d'
    date_obj = datetime.strptime(new_ent["fecha"], date_format)
    entradaClinica.fecha = date_obj
    entradaClinica.save()
    return entradaClinica

def create_entradaClinica(ent):
    date_format = '%Y-%m-%d'
    date_obj = datetime.strptime(ent["fecha"], date_format)
    entradaClinica = EntradaClinica(
        diagnostico=ent["diagnostico"], 
        tratamiento=ent["tratamiento"],
        paciente=ul.get_paciente(ent["paciente"]),
        autor=ul.get_medico(ent["autor"]),
        fecha=date_obj,
    )
    entradaClinica.cita = al.get_cita(ent["cita"])  # type: ignore
    entradaClinica.save()
    return entradaClinica

def delete_entradaClinica(ent_pk):
    entradaClinica = get_entradaClinica(ent_pk)
    entradaClinica.delete()
