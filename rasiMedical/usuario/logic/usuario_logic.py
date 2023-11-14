from ..models import Medico, Enfermera, Farmaceutico
from ..models import Paciente
from ..models import Administrador

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
    paciente.eps = new_pac["eps"]
    paciente.save()
    return paciente

def update_pacienteEps(new):
    new.save()
    return new

def create_paciente(pac):
    paciente = Paciente(
        nombre=pac["nombre"], 
        correo=pac["correo"], 
        clave=pac["clave"], 
        identificacion=pac["identificacion"], 
        numeroDeSeguro=pac["numeroDeSeguro"],
        eps = pac["eps"]
    )
    paciente.save()
    return paciente

def delete_paciente(pac_pk):
    paciente = get_paciente(pac_pk)
    paciente.delete()
    
def get_admins():
    admins = Administrador.objects.all()
    return admins

def get_admin(admin_pk):
    admin = Administrador.objects.get(pk=admin_pk)
    return admin

def update_admin(admin_pk, new_admin):
    admin = get_admin(admin_pk)
    admin.nombre = new_admin["nombre"]
    admin.correo = new_admin["correo"]
    admin.clave = new_admin["clave"]
    admin.identificacion = new_admin["identificacion"]
    admin.cargo = new_admin["cargo"]
    admin.save()
    return admin

def create_admin(admin):
    administrador = Administrador(nombre = admin["nombre"], correo = admin["correo"], clave = admin["clave"], identificacion = admin["identificacion"], cargo = admin["cargo"])
    administrador.save()
    return administrador

def delete_admin(admin_pk):
    admin = get_admin(admin_pk)
    admin.delete()

def delete_enfermera(enf_pk):
    enf = get_Enfermera(enf_pk)
    enf.delete()

def get_Enfermeras():
    enfs = Enfermera.objects.all()
    return enfs

def get_Enfermera(enf_pk):
    enf = Enfermera.objects.get(pk = enf_pk)
    return enf

def update_Enfermera(enf_pk, new_enf):
    enf = get_Enfermera(enf_pk)
    enf.nombre = new_enf["nombre"]
    enf.correo = new_enf["correo"]
    enf.clave = new_enf["clave"]
    enf.identificacion = new_enf["identificacion"]
    enf.area = new_enf["area"]
    enf.save()
    return enf

def create_Enfermera(enf):
    enf = Enfermera(nombre = enf["nombre"], correo = enf["correo"], clave = enf["clave"], identificacion = enf["identificacion"], area = enf["area"])
    enf.save()
    return enf

def delete_farmaceutico(far_pk):
    far = get_farmaceutico(far_pk)
    far.delete()

def get_farmaceuticos():
    fars = Farmaceutico.objects.all()
    return fars

def get_farmaceutico(far_pk):
    far = Farmaceutico.objects.get(pk = far_pk)
    return far

def get_medicoEmail(email):
    med = Medico.objects.get(correo = email)
    return med

def update_farmaceutico(far_pk, new_far):
    far = get_farmaceutico(far_pk)
    far.nombre = new_far["nombre"]
    far.correo = new_far["correo"]
    far.clave = new_far["clave"]
    far.identificacion = new_far["identificacion"]
    far.area = new_far["area"]
    far.save()
    return far

def create_farmaceutico(far):
    far = Farmaceutico(nombre = far["nombre"], correo = far["correo"], clave = far["clave"], identificacion = far["identificacion"], area = far["area"])
    far.save()
    return far