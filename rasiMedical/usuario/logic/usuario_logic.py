from ..models import Medico
from ..models import Paciente

def get_medicos():
    meds = Medico.objects.all()
    return meds

def get_medico(med_pk):
    med = Medico.objects.get(pk = med_pk)
    return med

def update_medico(med_pk, new_med):
    med = get_medico(med_pk)
    med.nombre = new_med["nombre"]
    med.correo = new_med["correo"]
    med.clave = new_med["clave"]
    med.identificacion = new_med["identificacion"]
    med.especialidad = new_med["especialidad"]
    med.licencia = new_med["licencia"]
    med.save()
    return med

def create_medico(med):
    medico = Medico(nombre = med["nombre"], correo = med["correo"], clave = med["clave"], identificacion = med["identificacion"], especialidad = med["especialidad"], licencia = med["licencia"])
    medico.save()
    return medico

def delete_medico(med_pk):
    med = get_medico(med_pk)
    med.delete()
    
def get_pacientes():
    pacientes = Paciente.objects.all()
    return pacientes

def get_paciente(pac_pk):
    paciente = Paciente.objects.get(pk=pac_pk)
    return paciente

def update_paciente(pac_pk, new_pac):
    paciente = get_paciente(pac_pk)
    paciente.nombre = new_pac["nombre"]
    paciente.correo = new_pac["correo"]
    paciente.clave = new_pac["clave"]
    paciente.identificacion = new_pac["identificacion"]
    paciente.numeroDeSeguro = new_pac["numeroDeSeguro"]
    paciente.save()
    return paciente

def create_paciente(pac):
    paciente = Paciente(
        nombre=pac["nombre"], 
        correo=pac["correo"], 
        clave=pac["clave"], 
        identificacion=pac["identificacion"], 
        numeroDeSeguro=pac["numeroDeSeguro"]
    )
    paciente.save()
    return paciente

def delete_paciente(pac_pk):
    paciente = get_paciente(pac_pk)
    paciente.delete()