from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse  # Importación corregida
from django.views.decorators.csrf import csrf_exempt
import json

# Base de datos en memoria (simulación)
items = [{"id": 1, "nombre": "Laptop"}, {"id": 2, "nombre": "Teléfono"}]

@csrf_exempt  # Desactiva la verificación CSRF para pruebas
def obtener_agregar_items(request):
    if request.method == 'GET':  # Devolver la lista de ítems en formato JSON
        return JsonResponse(items, safe=False)

    elif request.method == 'POST':
        try:
            data = json.loads(request.body)  # Convertir JSON en diccionario
            max_id = max((item["id"] for item in items), default=0)
            nuevo_item = {
                #"id": len(items) + 1, #ERROR (permite ids duplicados)
                "id": max_id + 1,
                "nombre": data.get("nombre", "Sin nombre")
            }
            items.append(nuevo_item)  # Agregar el nuevo ítem a la lista
            return JsonResponse(nuevo_item, status=201)  # Respuesta exitosa
        except json.JSONDecodeError:
            return JsonResponse({"error": "Formato JSON inválido"}, status=400)

@csrf_exempt  # Desactiva la verificación CSRF para pruebas
def obtener_editar_eliminar_item(request, pk):
    item = None
    for dic in items:
        if dic["id"] == pk:
            item = dic
            break

    if not item:
        return JsonResponse({"error": "Item no encontrado"}, status=404)

    if request.method == 'GET':  # Devolver la lista de ítems en formato JSON
        return JsonResponse(item)

    elif request.method == 'PATCH':
        try:
            data = json.loads(request.body)  # Convertir JSON en diccionario
            if "nombre" in data:
                item["nombre"] = data["nombre"]
            return JsonResponse(item, status=200)  # Respuesta exitosa
        except json.JSONDecodeError:
            return JsonResponse({"error": "Formato JSON inválido"}, status=400)

    elif request.method == 'DELETE':  # Eliminar ítem
        items.remove(item)
        return JsonResponse({"mensaje": "Ítem eliminado exitosamente"}, status=204)
