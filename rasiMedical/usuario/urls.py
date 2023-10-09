from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.medicos_view, name='medicos_view'), # type: ignore
    path('<int:pk>', views.medico_view, name='medico_view'), # type: ignore
    path('dispositivo/', views.pacientes_view, name='dispositivos_view'), 
    path('dispositivo/<int:id>', views.paciente_view, name='elemento_view'), 
]
