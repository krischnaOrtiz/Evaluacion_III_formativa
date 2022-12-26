from django.shortcuts import render

def listarEquipos(request):
    datos = {
        "Equipos": [
            {"nombre": "real madrid", "año_creacion": "1902", "Campeon": True, "imagen": "img/check.png"},
            {"nombre": "barcelona", "año_creacion":"1899", "Campeon": False, "imagen": "img/false.png"},
            {"nombre": "la roja", "año_creacion": "1895", "Campeon": True, "imagen": "img/check.png"}
        ]
    }
    return render(request, 'Equipos_app/listar_equipo.html', datos)



def verEquipos(request):
    return render(request, 'Equipos_app/Ver_equipo.html')
