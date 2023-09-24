from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.elementos_view, name='elementos_view'),
    path('<int:id>', views.elemento_view, name = 'elemento_view')
]