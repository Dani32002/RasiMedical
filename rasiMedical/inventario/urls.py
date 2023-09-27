from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('dispositivos/', views.dispositivos_view, name='dispositivos_view'), # type: ignore
    path('dispositivos/<int:id>', views.dispositivo_view, name = 'elemento_view'), # type: ignore
    path('medicamentos/', views.medicamentos_view, name='medicamentos_view'), # type: ignore
    path('medicamentos/<int:id>', views.medicamento_view, name = 'medicamento_view'), # type: ignore
    path('insumos/', views.insumos_view, name='insumos_view'), # type: ignore
    path('insumos/<int:id>', views.insumo_view, name = 'insumo_view') # type: ignore
]