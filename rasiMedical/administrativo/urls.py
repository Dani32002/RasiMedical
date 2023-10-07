from django.urls import path
from . import views

urlpatterns = [
    path('factura/', views.facturas_view, name='facturas_view'), # type: ignore
    path('factura/<int:id>', views.factura_view, name = 'factura_view'), # type: ignore
    path('factura/<int:id>/emitir', views.emitirFactura, name = 'emitirFactura'), # type: ignore
]