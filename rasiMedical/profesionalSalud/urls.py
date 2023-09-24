from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.profesionalesSalud_view, name='profesionalesSalud_view'), 
    path('<int:pk>', views.profesionalSalud_view, name='profesionalSalud_view')
]
