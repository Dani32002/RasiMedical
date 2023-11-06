from django.urls import path
from . import views

urlpatterns = [
    path('cita', views.citas_view, name='citas_view'), # type: ignore
    path('cita/<int:pk>', views.cita_view, name = 'cita_view'), # type: ignore
]