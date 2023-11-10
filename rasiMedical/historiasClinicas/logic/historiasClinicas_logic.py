from ..models import EntradaClinica

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
    entradaClinica.fecha = new_ent["fecha"]
    entradaClinica.save()
    return entradaClinica

def create_entradaClinica(ent):
    entradaClinica = EntradaClinica(
        diagnostico=ent["diagnostico"], 
        tratamiento=ent["tratamiento"], 
        fecha=ent["fecha"]
    )
    entradaClinica.save()
    return entradaClinica

def delete_entradaClinica(ent_pk):
    entradaClinica = get_entradaClinica(ent_pk)
    entradaClinica.delete()
