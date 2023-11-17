from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #path('', views.entradasClinicas_view, name='entradasClinicas_view'), # type: ignore
    #path('<int:pk>', views.entradaClinica_view, name='entradaClinica_view'), # type: ignore
    path('<int:pk>/medico/<int:pkEntidad>', views.anadirMedico, name='anadirMedico'), # type: ignore
    path('<int:pk>/enfermera/<int:pkEntidad>', views.anadirEnfermera, name='anadirEnfermera'), # type: ignore
    path('<int:pk>/farmaceutico/<int:pkEntidad>', views.anadirFarmaceutico, name='anadirFarmaceutico'), # type: ignore
    path('view/<int:pk>', views.pacientes_historias, name = "pacientes_historias"),  # type: ignore
    path('view/<int:pk>/crear/nueva-historia/', views.nueva_historia , name = "nueva-historia"), # type: ignore
    path('view/<int:pk>/crear/', views.crear, name = "crear") # type: ignore
]