from django.urls import path

from mundial_api import views

urlpatterns = [
    path('equipos/', views.listaEquipos),
    path('mostrarJugador/<int:id>', views.mostrarJugador),
    path('jugador/editar/<int:id>', views.gestionarJugador)
]
