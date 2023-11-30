from ..models import Medico

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