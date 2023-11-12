from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.entradasClinicas_view, name='entradasClinicas_view'), # type: ignore
    path('<int:pk>', views.entradaClinica_view, name='entradaClinica_view'), # type: ignore
]