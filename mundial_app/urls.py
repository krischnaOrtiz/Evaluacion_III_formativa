from django.urls import path

from mundial_app import views


urlpatterns = [
    path('equipo/listaEquipos', views.listarEquipos),
    path('equipo', views.verEquipos)
]