from ..models import ProfesionalSalud

def get_profesionalesSalud():
    profs = ProfesionalSalud.objects.all()
    return profs

def get_profesionalSalud(prof_pk):
    prof = ProfesionalSalud.objects.get(pk = prof_pk)
    return prof