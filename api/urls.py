from django.urls import path  # Corrección en la importación
from .views import obtener_agregar_items, obtener_editar_eliminar_item  # Corrección en la importación

urlpatterns = [
    path('items/', obtener_agregar_items, name ='obtener_agregar_items'),
    path('items/<int:pk>', obtener_editar_eliminar_item, name="obtener_editar_eliminar_item"),
    ]
