from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('dispositivo/', views.dispositivos_view, name='dispositivos_view'), # type: ignore
    path('dispositivo/<int:id>', views.dispositivo_view, name = 'elemento_view'), # type: ignore
    path('medicamento/', views.medicamentos_view, name='medicamentos_view'), # type: ignore
    path('medicamento/<int:id>', views.medicamento_view, name = 'medicamento_view'), # type: ignore
    path('insumo/', views.insumos_view, name='insumos_view'), # type: ignore
    path('insumo/<int:id>', views.insumo_view, name = 'insumo_view'), # type: ignore
    path('medicamento/<int:id>/medico/<int:id2>', views.anadirMedicoMedicamento, name = 'nadirMedicoMedicamento'), # type: ignore
    path('dispositivo/<int:id>/medico/<int:id2>', views.anadirMedicoDispositivo, name = 'anadirMedicoDispositivo'), # type: ignore
    path('insumo/<int:id>/medico/<int:id2>', views.anadirMedicoInsumo, name = 'anadirMedicoInsumo'), # type: ignore
]