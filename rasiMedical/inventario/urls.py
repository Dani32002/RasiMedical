from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dispositivos_view, name='dispositivos_view'), # type: ignore
    path('<int:id>', views.dispositivo_view, name = 'elemento_view') # type: ignore
]