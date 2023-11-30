from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('medico/', views.medicos_view, name='medicos_view'),
    path('medico/<int:pk>', views.medico_view, name='medico_view'),
]
