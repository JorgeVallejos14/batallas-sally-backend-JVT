from django.shortcuts import render
from django.http import Http404

# Create your views here.
batallas_resistencia = [
    {"id": 1, "nombre": "Batalla de Robotropolis", "ubicacion": "Robotropolis",
     "bajas": 3, "victoria": True, "lider": "Sally Acorn",
     "descripcion": "Ataque directo a la fortaleza principal de Robotnik."},

    {"id": 2, "nombre": "Emboscada en el Bosque", "ubicacion": "Bosque de Knothole",
     "bajas": 0, "victoria": True, "lider": "Sonic",
     "descripcion": "La Resistencia repelio una patrulla de SWATbots sin bajas."},

    {"id": 3, "nombre": "Defensa del Puente Colgante", "ubicacion": "Puente del Rio Mobius",
     "bajas": 5, "victoria": False, "lider": "Antoine",
     "descripcion": "Retirada forzada tras un ataque aereo masivo de la Legion."},

    {"id": 4, "nombre": "Rescate en la Prision de Robotnik", "ubicacion": "Prision Robotropolis",
     "bajas": 1, "victoria": True, "lider": "Sally Acorn",
     "descripcion": "Liberacion de prisioneros mobianos capturados."},

    {"id": 5, "nombre": "Escaramuza en las Montañas", "ubicacion": "Montañas de Mobius",
     "bajas": 2, "victoria": False, "lider": "Bunnie Rabbot",
     "descripcion": "Enfrentamiento con robots de reconocimiento, sin resultado claro."},

    {"id": 6, "nombre": "Toma de la Torre de Comunicaciones", "ubicacion": "Torre Central",
     "bajas": 0, "victoria": True, "lider": "Rotor",
     "descripcion": "Sabotaje exitoso a las comunicaciones de Robotnik sin bajas."},
]


def inicio(request):
    contexto = {"batallas": batallas_resistencia, "total": len(batallas_resistencia)}
    return render(request, "batallas/inicio.html", contexto)


def detalle(request, id):
    batalla = next((b for b in batallas_resistencia if b["id"] == id), None)
    if batalla is None:
        raise Http404("Batalla no encontrada")
    return render(request, "batallas/detalle.html", {"batalla": batalla})