from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dispositivos_view, name='dispositivos_view'), # type: ignore
    path('<int:id>', views.dispositivo_view, name = 'elemento_view'), # type: ignore
    path('', views.medicamentos_view, name='medicamentos_view'), # type: ignore
    path('<int:id>', views.medicamento_view, name = 'medicamento_view') # type: ignore
]