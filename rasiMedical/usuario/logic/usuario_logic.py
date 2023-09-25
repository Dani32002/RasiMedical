from ..models import Medico

def get_medicos():
    meds = Medico.objects.all()
    return meds

def get_medico(med_pk):
    med = Medico.objects.get(pk = med_pk)
    return med