from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.medicos_view, name='medicos_view'), # type: ignore
    path('<int:pk>', views.medico_view, name='medico_view'), # type: ignore
    path('paciente/', views.pacientes_view, name='pacientes_view'),  # type: ignore
    path('paciente/<int:id>', views.paciente_view, name='paciente_view'),  # type: ignore
    path('paciente/<int:id>/eps/<int:id2>', views.anadirEpsPaciente, name='paciente_view'), # type: ignore
    path('admin/', views.admins_view, name='admins_view'), # type: ignore
    path('admin/<int:pk>', views.admin_view, name='admin_view'), # type: ignore
    path('admin/estadisticas', views.estadisticas, name='adminStats_view'),  # type: ignore
    path('enfermera/', views.enfermeras_view, name='enferemas_view'), # type: ignore
    path('enfermera/<int:pk>', views.enfermera_view, name='enfermera_view'), # type: ignore
    path('farmaceutico/', views.farmaceuticos_view, name='farmaceuticos_view'), # type: ignore
    path('farmaceutico/<int:pk>', views.farmaceutico_view, name='farmaceutico_view'), # type: ignore
    path('historiaclinica/view/', views.pacientesHC_view, name = "pacientesHC_view"), # type: ignore
    path('historiaclinica/view/<int:pk>', views.pacientes_historias, name = "pacientes_historias"),  # type: ignore
    path('historiaclinica/view/<int:pk>/nueva-historia/', views.nueva_historia , name = "nueva-historia") # type: ignore
]
